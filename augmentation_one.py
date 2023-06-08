import os
import cv2
import shutil
# import zipfile
from tqdm import tqdm
from os.path import join
import numpy as np
import imgaug.augmenters as iaa
from pathlib import Path
import multiprocessing as mp

from multiprocessing import Process

seq = iaa.Sequential([
    iaa.Crop(px=(0, 8), keep_size=True),  # Dla obrazka 64px więcej niż 8 to dużo
    # iaa.Fliplr(0.5),
    iaa.GaussianBlur(sigma=(0, 0.5)),  # Większy blur polepszy uogólnianie?
    iaa.Sharpen(alpha=(0, 0.5), lightness=(0.75, 1.25)),

    # iaa.SimplexNoiseAlpha(iaa.OneOf([
    #     iaa.EdgeDetect(alpha=(0.0, .3)),
    #     iaa.DirectedEdgeDetect(alpha=(0.0, .5), direction=(0.0, 0.5)),
    # ])),

    # iaa.Emboss(alpha=(0, 1.0), strength=(0, 0.4)),  # Taka maska wyciagajaca fakturę
    # iaa.Dropout((0.01, 0.1), per_channel=0.5),  # Robi czarne kropki
    # iaa.CoarseDropout((0.03, 0.15), size_percent=(0.01, 0.03), per_channel=0.2), #Robi czarny kwadrat
    # iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05 * 255), per_channel=0.5),
    # iaa.PiecewiseAffine(scale=(0.01, 0.05)),  # Lekkie zniekształcenia
    # iaa.PerspectiveTransform(scale=(0.01, 0.1)),

    iaa.Add((-10, 10), per_channel=0.5),  # Brightness
    #     iaa.FrequencyNoiseAlpha(
    #         exponent=(-1, 0),
    #         first=iaa.Multiply((0.7, 1.3), per_channel=True),
    #         second=iaa.LinearContrast((0.8, 1.3))
    #     ),
])
seq.seed_(1234)

def augment_images(src, dst, i):
    for x in tqdm(os.listdir(src)):
        filename, extension = x.split('.')
        filename_aug = filename + f'_aug{i}' + '.'
        if extension != 'png':
            filename_xml = filename_aug + extension
            shutil.copyfile(os.path.join(src, x), os.path.join(dst, filename_xml))
            continue
        img = cv2.imread(join(src, x))
        if img is None:
            continue
        imgs = np.array([img])
        image_aug = seq(images=imgs)[0]
        filename_img = filename_aug + 'jpg'
        cv2.imwrite(join(dst, filename_img), image_aug)


if __name__ == '__main__':
    train_original = os.path.join('Augmentation', 'yolo', 'train')
    train_aug = "Augmentation/augmented_one/train"
    Path(train_aug).mkdir(parents=True, exist_ok=True)

    mp.set_start_method('spawn')
    q = mp.Queue()
    processes = []
    for n in range(3):
        p = mp.Process(target=augment_images, args=(train_original, train_aug, n))
        p.start()
        processes.append(p)
    # print(q.get())
    for y in processes:
        y.join()
