import csv

import cv2
from tqdm import tqdm
import os

from pathlib import Path

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)

data_dict = dict()
for x in data:
    data_dict[x[0]] = x[6] == 'True'

print(data_dict)

true_path = "ground_truth_sensor/true"
false_path = "ground_truth_sensor/false"
Path(true_path).mkdir(parents=True, exist_ok=True)
Path(false_path).mkdir(parents=True, exist_ok=True)

video_list_files = os.listdir('videos')
for video_id, video_name in enumerate(video_list_files):
    filename = video_name.split('.')[0]
    video_path = os.path.join('videos', video_name)
    cap = cv2.VideoCapture(video_path)
    frames_count = (cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if not cap.isOpened():
        print("Error opening video stream or file")

    pbar = tqdm(total=frames_count)
    frame_id = 0
    while cap.isOpened():
        ret, frame = cap.read()
        frame_id += 1
        if not ret:
            continue

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        frame = cv2.resize(frame, (640, 640))
        pbar.update(1)

        id_ = f"{video_id}_{frame_id}"
        if id_ in data_dict:
            # print(type(data_dict[id_]), data_dict[id_], id_)
            if data_dict[id_]:
                cv2.imwrite(os.path.join(true_path, f"{id_}.jpg"), frame)
            else:
                cv2.imwrite(os.path.join(false_path, f"{id_}.jpg"), frame)

        if frame_id >= frames_count:
            break

    cap.release()
    cv2.destroyAllWindows()
