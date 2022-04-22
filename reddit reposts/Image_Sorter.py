import numpy as np
import cv2
import glob
from skimage.filters import gaussian
from skimage import img_as_ubyte
import os


def sorter():
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    images_list = []
    size = 440

    path2 = path+"/reddit reposts/scraped images/*.*"

    for file in glob.glob(path2):
        try:
            img = cv2.imread(file, 0)
            img = cv2.resize(img, (size, size))
            images_list.append(img)
        except Exception:
            continue

    images_list = np.array(images_list)

    img_number = 1
    for image in range(images_list.shape[0]):
        input_img = images_list[image, :, :]
        smoothed_image = img_as_ubyte(gaussian(input_img, sigma=5, mode="constant", cval=0.0))
        cv2.imwrite(path+"/reddit reposts/sorted images/""sorted images" + str(img_number) + ".jpg", smoothed_image)
        img_number += 1
