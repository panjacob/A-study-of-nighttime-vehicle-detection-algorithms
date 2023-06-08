import csv

import cv2
from tqdm import tqdm
import os

from ultralytics import YOLO

video_list_files = os.listdir('videos')
print(video_list_files)

model_yolo8n = os.path.join('..', 'yolov8', 'n_50_50_100.pt')
model = YOLO(model_yolo8n)
blocking_lines = [280, 150]
data = []
for i, video_name in enumerate(video_list_files):
    # if i < 2:
    #     continue
    video_path = os.path.join('videos', video_name)
    cap = cv2.VideoCapture(video_path)
    frames_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    video_time = frames_count / fps
    frames_light_time = []

    if not cap.isOpened():
        print("Error opening video stream or file")

    pbar = tqdm(total=frames_count / 25)
    success_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue
        success_count += 1
        if success_count == frames_count:
            break
        # if success_count < 3000:
        #     continue
        if success_count % 25 != 0:
            continue

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        frame = cv2.resize(frame, (640, 640))
        result = model.predict(source=frame, classes=[0])
        found = 0
        print(result[0].boxes, result[0].boxes.xyxy)
        for x in result[0].boxes.xyxy:

            y = x.cpu().numpy().astype(int)
            if i >= 2:
                frame = cv2.line(frame, (0, blocking_lines[0]), (640, blocking_lines[0]), (255, 0, 0), 1)
                frame = cv2.line(frame, (blocking_lines[1], 0), (blocking_lines[1], 640), (255, 0, 0), 1)
                if y[1] < blocking_lines[0]:
                    color = (0, 0, 255)
                elif y[0] < blocking_lines[1]:
                    color = (0, 255, 255)
                else:
                    color = (0, 255, 0)
                    found += 1
            else:
                color = (0, 255, 0)
                found += 1
            frame = cv2.rectangle(frame, (y[0], y[1]), (y[2], y[3]), color, 2)

        # print(result[0].boxes)
        is_car = found > 0
        data.append([f"{i}_{success_count}", is_car])

        pbar.update(1)
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1)
        # if key == 13:
        #     pass
        # if key == ord('q'):
        #     print('success_count: ', success_count)
        #     break

    # print(succ, fail)
    cap.release()
    cv2.destroyAllWindows()

f = open(f"inference.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(f)
writer.writerows(data)
f.close()
