import os
import shutil

import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.builders import model_builder
from object_detection.utils import config_util
import cv2
import numpy as np
from tqdm import tqdm
from utilis import paths, files

# from Tensorflow.deepsort.deep_sort.detection import Detection
from utilis import create_path

MAX_DETECTIONS = 3
IMAGE_SIZE = 320
MIN_SCORE = 0.2


@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections


def detect_from_img(img):
    image_np = np.array(img)
    image_np_expanded = np.expand_dims(image_np, 0)
    input_tensor = tf.convert_to_tensor(image_np_expanded, dtype=tf.float32)
    return detect_fn(input_tensor)


def parse_detections(detections_raw):
    num_detections = int(detections_raw.pop('num_detections'))
    scores = detections_raw['detection_scores']
    score_count = np.count_nonzero(scores.numpy() > MIN_SCORE)
    if num_detections > MAX_DETECTIONS:
        num_detections = MAX_DETECTIONS
    if num_detections > score_count:
        num_detections = score_count

    detections_raw = {key: value[0, :num_detections].numpy()
                      for key, value in detections_raw.items()}

    detections_raw['num_detections'] = num_detections

    detections_raw['detection_classes'] = detections_raw['detection_classes'].astype(np.int64)
    detections_raw['detection_boxes'] *= IMAGE_SIZE
    detections_raw['detection_boxes'] = np.rint(detections_raw['detection_boxes']).astype(int)

    return list(zip(detections_raw['detection_scores'], detections_raw['detection_boxes'],
                    detections_raw['detection_classes']))


def draw_box(detections):
    for score, box, detclass in detections:
        p1 = (box[1], box[0])
        p2 = (box[3], box[2])
        cv2.rectangle(img, p1, p2, (0, 255, 0), 1)


def init_detection_model():
    configs = config_util.get_configs_from_pipeline_file(files['PIPELINE_CONFIG'])
    detection_model = model_builder.build(model_config=configs['model'], is_training=False)
    ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
    ckpt.restore(os.path.join(paths['CHECKPOINT_PATH'], 'ckpt-16')).expect_partial()
    category_index = label_map_util.create_category_index_from_labelmap(files['LABELMAP'])
    return detection_model


def init_video(path):
    vidcap = cv2.VideoCapture(os.path.join(paths['TRACK_PATH'], '1.mp4'))
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, 800)
    success, img = vidcap.read()
    return vidcap, success


def display(img):
    cv2.imshow('hehe', img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        pass


def get_filename(file):
    return file.split('.')[0]


def convert(size, box):
    dr = 1. / size

    c = box[0]
    d = box[1]
    a = box[2]
    b = box[3]

    x = (a + b) / 2.0
    y = (c + d) / 2.0
    w = b - a
    h = d - c

    x = x * dr
    w = w * dr
    y = y * dr
    h = h * dr
    return (x, y, w, h)


def save_detections(detections, file, destination_path_true):
    filename = get_filename(file)
    yolo_file = ""
    for detection in detections:
        acc, box, class_number = detection
        x, y, w, h = convert(320, box)
        value = f"{class_number} {x} {y} {w} {h}\n"
        yolo_file += value
    f = open(os.path.join(destination_path_true, f"{filename}.txt"), "w")
    f.write(yolo_file)
    f.close()


detection_model = init_detection_model()
# vidcap, success = init_video(os.path.join(paths['TRACK_PATH'], '1.mp4'))
MAIN_PATH = os.path.join('Tensorflow', 'workspace', 'images')
source_path = create_path(os.path.join(MAIN_PATH, '2_images'))
destination_path_true = create_path(os.path.join(MAIN_PATH, '4_filtered_ai', 'true'))
destination_path_false = create_path(os.path.join(MAIN_PATH, '4_filtered_ai', 'false'))
filesx = os.listdir(source_path)

for file in tqdm(filesx):
    img_original = cv2.imread(os.path.join(source_path, file))
    img = cv2.resize(img_original, (IMAGE_SIZE, IMAGE_SIZE))
    detections_raw = detect_from_img(img)
    detections = parse_detections(detections_raw)
    if len(detections):
        save_detections(detections, file, destination_path_true)
        shutil.copy2(os.path.join(source_path, file), os.path.join(destination_path_true, file))
    else:
        shutil.copy2(os.path.join(source_path, file), os.path.join(destination_path_false, file))

    # draw_box(detections)
    # display(img)
