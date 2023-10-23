import csv

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

TP = TN = FP = FN = 0
points = [[100, 200, 200, 300]]
for i, (img_path, etiquette) in enumerate(dataset):
    video_id = int(img_path.split('\\')[3].split('_')[0])
    pbar = tqdm(total=len(dataset))
    frame = cv2.imread(img_path)
    frame = cv2.resize(frame, (640, 640))

    frame = cv2.rectangle(frame, (points[0][0], points[0][1]), (points[0][2], points[0][3]), green, 2)


    cv2.imshow('Frame', frame)
    key = cv2.waitKey(0)
    pbar.update(i)

    if prediction and etiquette:
        TP += 1
    elif prediction and not etiquette:
        FP += 1
    elif not prediction and etiquette:
        FN += 1
    else:
        TN += 1

    pbar.update(1)
print(TP, TN, FP, FN)
accuracy = (TP + TN) / (TP + FN + TN + FP)
recall = TP / (TP + FN)
precision = TP / (TP + FP)
print(accuracy, recall, precision)
