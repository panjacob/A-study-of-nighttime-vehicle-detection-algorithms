import cv2
import numpy as np
import os
import shutil
from tqdm import tqdm

num_colors = 4  # Adjust the number of colors as needed
yolo_16 = f"yolo_{num_colors}"
if not os.path.isdir(f'datasets/{yolo_16}'):
    os.makedirs(f'datasets/{yolo_16}')
yolo_16_train = f'datasets/{yolo_16}/train'
yolo_16_test = f'datasets/{yolo_16}/test'
if not os.path.isdir(yolo_16_train):
    os.makedirs(yolo_16_train)
if not os.path.isdir(yolo_16_test):
    os.makedirs(yolo_16_test)

train_files = os.listdir('datasets/yolo/train')
test_files = os.listdir('datasets/yolo/test')

for x in tqdm(train_files):
    if x.split('.')[1] == 'txt':
        shutil.copyfile(f'datasets/yolo/train/{x}', f'datasets/{yolo_16}/train/{x}')
        continue
    image = cv2.imread(f'datasets/yolo/train/{x}')
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image_rgb.reshape((-1, 3))

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels.astype(np.float32), num_colors, None, criteria, 10,
                                    cv2.KMEANS_RANDOM_CENTERS)
    quantized_colors = np.uint8(centers)
    quantized_image = quantized_colors[labels.flatten()].reshape(image_rgb.shape)
    quantized_image_bgr = cv2.cvtColor(quantized_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'datasets/{yolo_16}/train/{x}', quantized_image_bgr)

    # cv2.imshow('Quantized Image', quantized_image_bgr)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

for x in tqdm(test_files):
    if x.split('.')[1] == 'txt':
        shutil.copyfile(f'datasets/yolo/test/{x}', f'datasets/{yolo_16}/test/{x}')
        continue
    image = cv2.imread(f'datasets/yolo/test/{x}')
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image_rgb.reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels.astype(np.float32), num_colors, None, criteria, 10,
                                    cv2.KMEANS_RANDOM_CENTERS)
    quantized_colors = np.uint8(centers)
    quantized_image = quantized_colors[labels.flatten()].reshape(image_rgb.shape)
    quantized_image_bgr = cv2.cvtColor(quantized_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'datasets/{yolo_16}/test/{x}', quantized_image_bgr)

    # cv2.imshow('Quantized Image', quantized_image_bgr)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
