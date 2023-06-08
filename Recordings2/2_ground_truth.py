import cv2
from tqdm import tqdm
import os

from pathlib import Path
Path("ground_truth/true").mkdir(parents=True, exist_ok=True)
Path("ground_truth/false").mkdir(parents=True, exist_ok=True)

i = 3
previous = False
video_list_files = os.listdir('videos')
video_name = video_list_files[i]
print(video_list_files, video_name)

skip_frames = 0

filename = video_name.split('.')[0]
video_path = os.path.join('videos', video_name)
cap = cv2.VideoCapture(video_path)
frames_count = (cap.get(cv2.CAP_PROP_FRAME_COUNT) - skip_frames)
fps = cap.get(cv2.CAP_PROP_FPS)
video_time = frames_count / fps
frames_light_time = []

if not cap.isOpened():
    print("Error opening video stream or file")

pbar = tqdm(total=frames_count)
success_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    success_count += 1
    if not ret:
        continue

    if success_count == frames_count - 500:
        break
    if success_count < skip_frames:
        continue

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
    frame = cv2.resize(frame, (640, 640))

    pbar.update(1)
    cv2.imshow('Frame', frame)

    if success_count % 25:
        if previous:
            cv2.imwrite(os.path.join('ground_truth', 'true', f"{i}_{success_count}.jpg"), frame)
        else:
            cv2.imwrite(os.path.join('ground_truth', 'false', f"{i}_{success_count}.jpg"), frame)

        continue

    key = cv2.waitKey(0)
    if key == 32:
        print('False')
        cv2.imwrite(os.path.join('ground_truth', 'false', f"{i}_{success_count}.jpg"), frame)
        previous = False
    if key == 13:
        print('True')
        cv2.imwrite(os.path.join('ground_truth', 'true', f"{i}_{success_count}.jpg"), frame)
        previous = True
    if key == 8:
        print('Skip')
        continue
    if key == ord('q'):
        print('success_count: ', success_count)
        break

cap.release()
cv2.destroyAllWindows()
