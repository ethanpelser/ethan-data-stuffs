
import numpy as np
import cv2
import math, operator
import glob
from PIL import Image as pilmg
from PIL import ImageChops
from skimage.filters import gaussian
from skimage import img_as_ubyte





def compare():
    image_list1 = []
    image_list2 = []
    print("1")




    for filename in glob.glob("E:/Documents/GitHub/ethan-data-stuffs/reddit reposts/sorted images/*.*"):
        try:
            im = cv2.imread(filename,0)
            image_list1.append(im)
            image_list2.append(im)
            print("2")
        except Exception as e:
            continue
    vounter = 1



    for i in image_list1:

        counter = 0
        print("4")
        i =pilmg.fromarray(i)

        for q in image_list2:

            q =pilmg.fromarray(q)
            diff = ImageChops.difference(i, q)
            h = diff.histogram()
            sq = (value * (idx ** 2) for idx, value in enumerate(h))
            sum_of_squares = sum(sq)
            rms = math.sqrt(sum_of_squares / float(i.size[0] * i.size[1]))

            if rms == 0:
                continue
            elif rms <= 50:
                counter+=1
            else:
                continue


        noompeez = np.array(i)
        img = img_as_ubyte(gaussian(noompeez, sigma=5, mode="constant", cval=0.0))
        cv2.imwrite("E://Documents/GitHub/ethan-data-stuffs/reddit reposts/images with amount similar/""image number "+str(vounter)+" is similar to " + str(counter) + " others.jpg", img)
        vounter += 1























