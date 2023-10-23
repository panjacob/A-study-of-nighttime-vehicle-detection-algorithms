import os.path
import time
import numpy as np
import cv2
import tensorflow as tf


def test_network(name, run_times=11):
    # Load the TFLite model and allocate tensors
    model_path = os.path.join('exported_coral', name)
    interpreter = tf.lite.Interpreter(model_path=name)
    interpreter.allocate_tensors()

    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    #first frame
    frame = np.zeros((640, 640, 3), dtype=np.float32)
    input_data = cv2.resize(frame, (input_details[0]['shape'][2], input_details[0]['shape'][1]))
    input_data = np.expand_dims(input_data, axis=0)
    input_data = (input_data - input_details[0]['quantization'][0]) / input_details[0]['quantization'][1]
    input_data = input_data.astype('uint8')  # float32
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Initialize FPS calculation
    frame_count = 0
    start_time = time.time()

    # Loop through frames from the video capture
    confidence_threshold = 0.5
    all_fps = 0
    print('starting test', name)
    for i in range(run_times):
        frame = np.zeros((640, 640, 3), dtype=np.float32)
        input_data = cv2.resize(frame, (input_details[0]['shape'][2], input_details[0]['shape'][1]))
        input_data = np.expand_dims(input_data, axis=0)
        input_data = (input_data - input_details[0]['quantization'][0]) / input_details[0]['quantization'][1]
        input_data = input_data.astype('uint8') #float32

        # Set the input tensor
        interpreter.set_tensor(input_details[0]['index'], input_data)

        # Perform the inference
        interpreter.invoke()

        # Get the output tensor and postprocess the results
        output_data = interpreter.get_tensor(output_details[0]['index'])

        frame_count += 1
        if frame_count % 100 == 0:
            print(frame_count)
            end_time = time.time()
            fps = 100 / (end_time - start_time)
            start_time = end_time
            all_fps += fps

    average = all_fps / run_times * 100
    print(name, average)



test_network('coral/pycoral/test_data/mobilenet_v2_1.0_224_inat_bird_quant.tflite', 1000)
