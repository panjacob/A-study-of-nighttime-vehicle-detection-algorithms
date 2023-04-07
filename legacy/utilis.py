from pathlib import Path
import os

def create_path(directory):
    Path(directory).mkdir(parents=True, exist_ok=True)
    return directory

CUSTOM_MODEL_NAME = 'my_ssd_mobnet_15000'
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
LABEL_MAP_NAME = 'label_map.pbtxt'
labels = [{'name': 'car', 'id': 1}]

VIDEOS_DICT = {
    0: 'rec_0722220000.mp4', 1: 'rec_190919223000.mp4', 2: 'rec_190701233000.avi', 3: 'rec_190919220001.mp4',
    4: 'rec_190919233001.mp4', 5: 'rec_0722230001.mp4', 6: 'rec_0722030003.mp4', 7: 'rec_190919210001.mp4',
    8: 'rec_190701230000.avi', 9: 'rec_0722010001.mp4', 10: 'rec_0722000001.mp4', 11: 'rec_190702000000.avi',
    12: 'rec_0722020002.mp4', 13: 'rec_20191216T173000.mp4', 14: 'rec_190919230002.mp4', 15: 'rec_190919213002.mp4'
}



paths = {
    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
    'SCRIPTS_PATH': os.path.join('Tensorflow', 'scripts'),
    'APIMODEL_PATH': os.path.join('Tensorflow', 'models'),
    'ANNOTATION_PATH': os.path.join('Tensorflow', 'workspace', 'annotations'),
    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace', 'images'),
    'TRAIN_PATH': os.path.join('Tensorflow', 'workspace', 'images', 'train'),
    'TRACK_PATH': os.path.join('Tensorflow', 'workspace', 'images', '4_tracking'),
    'MODEL_PATH': os.path.join('Tensorflow', 'workspace', 'models'),
    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow', 'workspace', 'pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME),
    'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'export'),
    'TFJS_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'tfjsexport'),
    'TFLITE_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'tfliteexport'),
    'PROTOC_PATH': os.path.join('Tensorflow', 'protoc'),
    'TFLITEEXPORT': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'export',
                                 'checkpoint', 'checkpoint')
}

files = {
    'PIPELINE_CONFIG': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], TF_RECORD_SCRIPT_NAME),
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}



