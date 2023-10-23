import csv
from pprint import pprint

import cv2
from tqdm import tqdm
import os

from ultralytics import YOLO

green = (0, 255, 0)

training_path = os.path.join('dataset', 'test')
training_files_true = [os.path.join(training_path, 'true', x) for x in os.listdir(os.path.join(training_path, 'true'))]
training_files_false = [os.path.join(training_path, 'false', x) for x in
                        os.listdir(os.path.join(training_path, 'false'))]

true_files = [[x, True] for x in training_files_true]
false_files = [[x, False] for x in training_files_false]

dataset = true_files + false_files


def get_keys(x):
    a, b = x[0].split('\\')[3].split('.')[0].split('_')
    # print(int(a), int(b))

    # return ((int(a) + 1) * 100_000) + int(b)
    return int(a), int(b)


dataset = sorted(dataset, key=lambda key: get_keys(key))

model_yolo8n = os.path.join('..', 'YOLOV8 training', 'yolov8s_extended.pt')
# 'yolov8s_extended.pt'
model = YOLO(model_yolo8n)

TP = TN = FP = FN = 0
TP1 = TN1 = FP1 = FN1 = 0
TP2 = TN2 = FP2 = FN2 = 0
pbar = tqdm(total=len(dataset))
dataset_len = len(dataset)
for i, (img_path, etiquette) in enumerate(dataset):
    video_id = int(img_path.split('\\')[3].split('_')[0])

    prediction = False

    frame = cv2.imread(img_path)
    frame = cv2.resize(frame, (640, 640))
    # result = model.predict(source=frame)
    # result = model.track(frame, persist=True)
    result = model.track(frame, persist=True, tracker="bytetrack.yaml")

    for x in result[0].boxes.xyxy:
        prediction = True
        y = x.cpu().numpy().astype(int)
        frame = cv2.rectangle(frame, (y[0], y[1]), (y[2], y[3]), green, 2)
        # cv2.imshow('Frame', frame)
        # key = cv2.waitKey(0)
        # print(img_path)

    if prediction and etiquette:
        TP += 1
    elif prediction and not etiquette:
        FP += 1
    elif not prediction and etiquette:
        FN += 1
    else:
        TN += 1

    if video_id < 2:
        if prediction and etiquette:
            TP1 += 1
        elif prediction and not etiquette:
            FP1 += 1
        elif not prediction and etiquette:
            FN1 += 1
        else:
            TN1 += 1

    if video_id >= 2:
        if prediction and etiquette:
            TP2 += 1
        elif prediction and not etiquette:
            FP2 += 1
        elif not prediction and etiquette:
            FN2 += 1
        else:
            TN2 += 1

    pbar.update(1)
print(TP, TN, FP, FN)
accuracy = (TP + TN) / (TP + FN + TN + FP)
recall = TP / (TP + FN)
precision = TP / (TP + FP)
print(accuracy, recall, precision)

print(TP1, TN1, FP1, FN1)
accuracy1 = (TP1 + TN1) / (TP1 + FN1 + TN1 + FP1)
recall1 = TP1 / (TP1 + FN1)
precision1 = TP1 / (TP1 + FP1)
print(accuracy1, recall1, precision1)

print(TP2, TN2, FP2, FN2)
accuracy2 = (TP2 + TN2) / (TP2 + FN2 + TN2 + FP2)
recall2 = TP2 / (TP2 + FN2)
precision2 = TP2 / (TP2 + FP2)
print(accuracy2, recall2, precision2)

# yolon
# 0.91 0.92 0.91 all
# 0.89 0.98 0.90 city
# 0.93 0.70 0.95 wieś
# botsort
# 0.94 0.80 0.92 wieś
# 0.84 0.99 0.84 city
# 0.89 0.96 0.85
# bytesort
# 0.89 0.96 0.85
# 0.84 0.99 0.84 city
# 0.94 0.80 0.92 wieś

# yolov8s
# 0.90 0.91 0.91
# 0.92 0.70 0.91
# 0.89 0.97 0.91
# botsort
# 0.91 0.95 0.88
# 0.93 0.79 0.89
# 0.88 0.99 0.88
# bytesort
# 0.91 0.95 0.88
# 0.93 0.79 0.89
# 0.88 0.99 0.88
