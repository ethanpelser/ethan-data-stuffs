
import numpy as np
import cv2
import math
import glob
from PIL import Image as Pilmg
from PIL import ImageChops
from skimage.filters import gaussian
from skimage import img_as_ubyte
import os


def compare():
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    image_list1 = []
    image_list2 = []

    for filename in glob.glob(path+"/reddit reposts/sorted images/*.*"):
        try:
            im = cv2.imread(filename, 0)
            image_list1.append(im)
            image_list2.append(im)
        except Exception:
            continue
    vounter = 1

    for i in image_list1:l;

        counter = 0

        i = Pilmg.fromarray(i)

        for q in image_list2:

            q = Pilmg.fromarray(q)
            diff = ImageChops.difference(i, q)
            h = diff.histogram()
            sq = (value * (idx ** 2) for idx, value in enumerate(h))
            sum_of_squares = sum(sq)
            rms = math.sqrt(sum_of_squares / float(i.size[0] * i.size[1]))

            if rms == 0:
                continue
            elif rms <= 50:
                counter += 1
            else:
                continue

        noompeez = np.array(i)
        img = img_as_ubyte(gaussian(noompeez, sigma=5, mode="constant", cval=0.0))
        cv2.imwrite(path+"/reddit reposts/images with amount similar/""image number "+str(vounter)+" is similar to "
                    + str(counter) + " others.jpg", img)
        vounter += 1
