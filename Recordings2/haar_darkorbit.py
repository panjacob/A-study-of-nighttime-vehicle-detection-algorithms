import random
import time
from functools import wraps

import mss as mss
import cv2
import numpy as np
import pyautogui

HALF_WIDTH = int(2560 / 2)
BOX_SIZE = 40
HALF_BOX_SIZE = int(BOX_SIZE / 2)
BOX_IMG = cv2.imread('img.png', cv2.IMREAD_UNCHANGED)
MOVING_POINT = (int((2400 - HALF_WIDTH) / 4), int(902 / 4))
MINIMAP_POSITION = [(2315, 920), (2535, 1050)]
MINIMAP_POSITION_HALF = [(MINIMAP_POSITION[0][0] - HALF_WIDTH, MINIMAP_POSITION[0][1]),
                         (MINIMAP_POSITION[1][0] - HALF_WIDTH, MINIMAP_POSITION[1][1])]

dimensions = {
    'left': HALF_WIDTH,
    'top': 0,
    'width': HALF_WIDTH,
    'height': 1080
}
SCT = mss.mss()


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time} seconds')
        return result

    return timeit_wrapper


# @timeit
def get_screenshot():
    scr = SCT.grab(dimensions)
    original = np.array(scr)[:, :, :3]
    img = cv2.resize(original, (320, 270))
    return img, original


# @timeit
def find_box(img):
    result = cv2.matchTemplate(img, BOX_IMG, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= 0.9:
        return min_val, max_val, min_loc, max_loc
    else:
        return None


# @timeit
def is_moving(img):
    # print(img[MOVING_POINT[1]][MOVING_POINT[0]])
    return (img[MOVING_POINT[1]][MOVING_POINT[0]] == 100).any()


# @timeit
def click_box(max_loc, img):
    # img = cv2.rectangle(img, max_loc, (max_loc[0] + BOX_SIZE, max_loc[1] + BOX_SIZE), (255, 255, 0), 2)

    center = ((max_loc[0] * 4) + HALF_BOX_SIZE + HALF_WIDTH, max_loc[1] * 4)
    pyautogui.click(center[0], center[1])
    return center


# @timeit
def loop():
    img, original = get_screenshot()
    # img = np.ascontiguousarray(img, dtype=np.uint8)
    if found_box := find_box(img):
        min_val, max_val, min_loc, max_loc = found_box
        center = click_box(max_loc, img)
        print((center[0]-HALF_WIDTH, center[1]))
        print(original.shape)
        # original = cv2.circle(original, (center[0]-HALF_WIDTH, center[1]), radius=4, color=(0, 0, 255), thickness=1)
        # cv2.imshow("The result", original)
        # if cv2.waitKey(1) & 0xFF == 27:
        #     pass
        time.sleep(3)
    # is_moving(img)
    elif not is_moving(img):
        x = random.randrange(MINIMAP_POSITION[0][0], MINIMAP_POSITION[1][0])
        y = random.randrange(MINIMAP_POSITION[0][1], MINIMAP_POSITION[1][1])
        pyautogui.click(x, y)
    # cv2.imshow("The result", img)
    # cv2.imwrite('xdd.png', img)
    # if cv2.waitKey(10) & 0xFF == 27:
    #     pass


while True:
    loop()
