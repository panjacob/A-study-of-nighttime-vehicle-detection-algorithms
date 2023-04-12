import cv2
from tqdm import tqdm
import os

from ultralytics import YOLO

video_list_files = os.listdir('videos')
print(video_list_files)

# model_yolo8n = os.path.join('..', 'yolov8', 'n50_50_100.onnx')
# model = YOLO(model_yolo8n)
# results = model.predict(source=)
# print(results)
# for result in results:
#     boxes = result.boxes  # Boxes object for bbox outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     probs = result.probs  # Class probabilities for classification outputs
#     print(boxes)
#     print(masks)
#     print(probs)
i = 2
for _, video_name in enumerate(video_list_files[i:]):

    filename = video_name.split('.')[0]
    video_path = os.path.join('videos', video_name)
    cap = cv2.VideoCapture(video_path)
    frames_count = (cap.get(cv2.CAP_PROP_FRAME_COUNT) - 3500) / 25
    fps = cap.get(cv2.CAP_PROP_FPS)
    video_time = frames_count / fps
    frames_light_time = []

    if not cap.isOpened():
        print("Error opening video stream or file")

    pbar = tqdm(total=frames_count)
    success_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue
        success_count += 1
        if success_count == frames_count - 500:
            # if success_count == 2:
            break
        if success_count < 3000:
            continue

        if success_count % 25:
            continue

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        frame = cv2.resize(frame, (640, 640))
        # cv2.imwrite(os.path.join('frames', f"{i}_{success_count}.png"), frame,[cv2.IMWRITE_PNG_COMPRESSION, 9])

        # crop_img = frame[20:600, 0:800]
        # frame = cv2.resize(frame, (640, 640))

        # results = model.predict(source=frame[:, :, ::-1])
        # result = model.predict(source=frame)
        # for x in result[0].boxes.xyxy:
        #     y = x.numpy().astype(int)
        #     print(y)
        #     if 640 < y[0] < 700 and 320 < y[1] < 360 and 690 < y[2] < 740 and 330 < y[3] < 370:
        #         print('pomijam lampe')
        #         continue
        #
        #     frame = cv2.rectangle(frame, (y[0], y[1]), (y[2], y[3]), (255, 0, 0), 2)

        # print(result[0].boxes)

        pbar.update(1)
        cv2.imshow('Frame', frame)

        key = cv2.waitKey(0)
        if key == 32:
            print('False')
            cv2.imwrite(os.path.join('frames_classified', 'false', f"{i}_{success_count}.jpg"), frame)
        if key == 13:
            print('True')
            cv2.imwrite(os.path.join('frames_classified', 'true', f"{i}_{success_count}.jpg"), frame)
        if key == 8:
            print('Skip')
            continue
        if key == ord('q'):
            print('success_count: ', success_count)
            break
        # if cv2.waitKey(999999) & 0xFF == 13:
        #     print('enter')
        #     continue
        # if cv2.waitKey(999999) & 0xFF == ord('q'):
        #     break

    # print(succ, fail)
    cap.release()
    cv2.destroyAllWindows()
