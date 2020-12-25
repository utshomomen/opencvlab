#
#All the copyright to utshomomen
#

import cv2
import numpy as np
import random
import sys
from os import path


img_original = cv2.imread("imagehh.jpg")
kernel = np.ones ((5,5),np.uint8)


cv2.imshow("frame1", img_original)

gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGBA)
cv2.imshow("frame2", gray)

canny = cv2.Canny(img_original,150,200)
cv2.imshow("frame3", canny)
#faces =cv2.(gray, 1.3, 5)
 #for (x, y, w, h)
 # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

dialation = cv2.dilate(img_original, kernel, iterations=1)

cv2.imshow("frame4", dialation)

eroded = cv2.erode(img_original, kernel, iterations=1)
cv2.imshow("frame5", eroded)

median = cv2.medianBlur(img_original, 5)
cv2.imshow("frame6", median)


convo = cv2.filter2D(img_original, -1, kernel)

cv2.imshow("frame7", convo)

cv2.waitKey(0)