from ultralytics import YOLO
import datetime


def save(model):
    try:
        success1 = model.export(format="onnx")  # export the model to ONNX format
    except:
        pass
    try:
        success2 = model.export(format="tflite")  # export the model to ONNX format
    except:
        pass
    try:
        success3 = model.export(format="engine")  # export the model to ONNX format
    except:
        pass
    try:
        success4 = model.export(format="saved_model")  # export the model to ONNX format
    except:
        pass
    try:
        success5 = model.export(format="tfjs")  # export the model to ONNX format
    except:
        pass


def run_train(yaml):
    now = datetime.datetime.now()
    print('Start', yaml, now)
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    model.train(data=yaml, epochs=100)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set
    save(model)
    now = datetime.datetime.now()
    print('End', yaml, now)


if __name__ == '__main__':
    # run_train("original.yaml")
    # run_train("strong_augumented_2.yaml")
    run_train("strong_augumented_5.yaml")

    import os

    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
