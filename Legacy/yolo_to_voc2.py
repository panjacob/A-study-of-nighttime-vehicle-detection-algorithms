import os
import shutil
from os.path import join
from tqdm import tqdm
import cv2
import numpy as np

from utilis import create_path


def yolo_labels_to_bbox(path, width, height):
    result = []
    target = (path)
    label_norm = np.loadtxt(target).reshape(-1, 5)
    for i in range(len(label_norm)):
        labels_conv = label_norm[i]
        new_label = unconvert(labels_conv[0], width, height, labels_conv[1], labels_conv[2], labels_conv[3],
                              labels_conv[4])
        result.append(new_label)
    return result


def get_filename_and_extension(file):
    x = file.split('.')
    return x[0], x[1]


def prepare_text(labels_bbox, img_path, file, yolo_classes, width, height, depth=1):
    text = f"""<annotation>
        <folder>train</folder>
        <filename>{file}</filename>
        <path>{os.path.abspath(img_path)}</path>
        <source>
            <database>Unknown</database>
        </source>
        <size>
            <width>{width}</width>
            <height>{height}</height>
            <depth>{depth}</depth>
        </size>
        <segmented>0</segmented>
        """
    for l in labels_bbox:
        class_id, xmin, xmax, ymin, ymax = l
        class_name = yolo_classes[class_id]
        text += f"""        <object>
        <name>{class_name}</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
            <bndbox>
                <xmin>{xmin}</xmin>
                <ymin>{ymin}</ymin>
                <xmax>{xmax}</xmax>
                <ymax>{ymax}</ymax>
            </bndbox>
</object>
"""
    text += """</annotation>"""

    return text


def unconvert(class_id, width, height, x, y, w, h):
    xmax = int((x * width) + (w * width) / 2.0)
    xmin = int((x * width) - (w * width) / 2.0)
    ymax = int((y * height) + (h * height) / 2.0)
    ymin = int((y * height) - (h * height) / 2.0)
    class_id = int(class_id)
    return (class_id, xmin, xmax, ymin, ymax)


def get_yolo_classes(yolo_images_path):
    yolo_classes = {}
    f = open(os.path.join(yolo_images_path, 'classes.txt'), 'r')
    lines = f.read().splitlines()
    for i, x in enumerate(lines):
        yolo_classes[i] = x
    f.close()
    return yolo_classes


def export_yolo_to_voc_2(voc2_images_path, yolo_images_path):
    outpath = join(voc2_images_path, '%s.xml')
    imgpath_out = join(voc2_images_path, '%s.png')
    imgpath_in = join(yolo_images_path, '%s.png')
    inpath = join(yolo_images_path, '%s.txt')
    yolo_classes = get_yolo_classes(yolo_images_path)

    for file in tqdm(os.listdir(yolo_images_path), 'YOLO to VOC2'):
        filename, extension = get_filename_and_extension(file)
        if filename == "classes" or filename == ".temp":
            continue
        if extension == 'txt':
            img = cv2.imread(imgpath_in % filename)
            height, width, channels = img.shape
            labels_bbox = yolo_labels_to_bbox(inpath % filename, width, height)
            text = prepare_text(labels_bbox, imgpath_in % filename, f"{filename}.png", yolo_classes, width, height)

            f = open(outpath % filename, "w", encoding='UTF-8')
            f.write(text)
            f.close()
            shutil.copy2(imgpath_in % filename, imgpath_out % filename)

# if __name__ == "__main__":
#     MAIN_PATH = os.path.join('Tensorflow', 'workspace', 'images')
#     VOC2_IMAGES_PATH = create_path(os.path.join(MAIN_PATH, '5_VOC2_images'))
#     YOLO_IMAGES_PATH = create_path(os.path.join(MAIN_PATH, '4_YOLO_images'))
#     export_yolo_to_voc_2(VOC2_IMAGES_PATH, YOLO_IMAGES_PATH)
