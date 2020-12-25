#
#All the copyright to utshomomen
#


import cv2
import numpy as np
import random
import sys
from os import path
import matplotlib.pyplot as plt

# comment // read the images from the file
img_original = cv2.imread("imagehh.jpg")


# comment // convert to halftone and contrast halftone is already converted but i cannot find a way
# contrast and taskber with the photo is not working at the moment because of some module that i can not install it here in python 3.9
#but basically the code is right here
"""
def haAndcon(x):
    pass
    cv2.namedWindow("contrast")
    cv2.createTrackbar("low", "contrast", 0, 255 , haAndcon)
    cv2.createTrackbar("high", "contrast", 0, 255, haAndcon)
    img_original = cv2.imread("imagehh.jpg")
    halftone = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGBA)
    cv2.imshow("halftoneframe", halftone)
    
    while True:
        
        x = cv2.getTrackbarPos("low", "constrast")
        y = cv2.getTrackbarPos("high", "constrast")
        graycontrast = cv2.cvtColor(halftone,60,120)
        cv2.imshow("halftoneframe", halftone)

haAndcon()

"""
#the grayscale is from here halftone and it converts to canny to detect the edge of the object

gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)


img_original = cv2.Canny(gray, 60, 120)




# this is hardcoded to find circle everywhere and detect circle
circles = cv2.HoughCircles(img_original, cv2.HOUGH_GRADIENT,1,120, param1=100, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    cv2.circle(img_original,(i[0], i[1]) ,i[2],(0,255,0),2)


    cv2.circle(img_original,(i[0], i[1]) ,2 ,(0,255,0),3)


font = cv2.FONT_HERSHEY_COMPLEX_SMALL
img_original = cv2.putText(img_original, "found circle in different angle of r(r=2)", (5, 100), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('frame14', img_original)

cv2.waitKey(0)
cv2.destroyAllWindows()
