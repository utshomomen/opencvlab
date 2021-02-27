import cv2
import imutils as imutils
import numpy as np
import random
import sys
from os import path
import matplotlib.pyplot as plt


def readFileAndResize():
    srcImage = cv2.imread("imagehh.jpg")

    srcImage = cv2.resize(srcImage, (1080, 1080))# default image
    img = np.uint16(srcImage)
    img = np.clip(2.0 * img, 0, 255)
    img = np.uint8(img)
    cv2.imshow(" imagemain", img)

    cv2.waitKey(0)
    return srcImage

readFileAndResize()

def halfTone():
    srcImage = cv2.imread("imagehh.jpg")
    grayImg = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
    cv2.imshow("hanlfTone", grayImg)
    cv2.waitKey(0)
    return grayImg

halfTone()

def increasingContrast():


    # srcImage = cv2.imread("imagehh.jpg")

    # # img = np.uint16(srcImage)
    # # img = np.clip(2.0 * img, 0, 255)
    # # img = np.uint8(img)
    # # cv2.imshow(" contrast", img)
    # cv2.waitKey(0)


    srcImage = cv2.imread('imagehh.jpg')
    cv2.imshow('test', srcImage)
    cv2.waitKey(0)
    imghsv = cv2.cvtColor(srcImage, cv2.COLOR_BGR2HSV)

    imghsv[:, :, 2] = [[max(pixel - 25, 0) if pixel < 190 else min(pixel + 25, 255) for pixel in row] for row in
                       imghsv[:, :, 2]]
    cv2.imshow('integralcontrast', cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR))
    cv2.waitKey(0)


increasingContrast()

def cannyImg():
    srcImage = cv2.imread("imagehh.jpg")
    grayImg = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grayImg, 60, 120)
    cv2.imshow("Canny", edges)
    cv2.waitKey(0)
    return edges

cannyImg()

def aroundCorners():
    srcImage = cv2.imread("imagehh.jpg")
    grayImg = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(grayImg, 5, 3, 0.04)
    tmp = np.empty(dst.shape, dtype=np.float32)
    cv2.normalize(dst, tmp, 0.0, 1.0, norm_type=cv2.NORM_MINMAX)
    srcImage = cv2.imread("imagehh.jpg")
    grayImg = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.cvtColor(grayImg, cv2.COLOR_GRAY2BGR)


    for i in range(dst.shape[0]):
        for j in range(dst.shape[1]):
            if tmp[i,j] > 0.3:
                cv2.circle(imgCanny, (j, i), 2, (255, 0, 0), 2)

    cv2.imshow("Corners", imgCanny)
    cv2.waitKey(0)
    imgCanny = cv2.cvtColor(imgCanny, cv2.COLOR_BGR2GRAY)
    return imgCanny

aroundCorners()


def distanceTransform():
    srcImage = cv2.imread("imagehh.jpg")
    gray = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    c = max(cnts, key=cv2.contourArea)
    mask = cv2.drawContours(gray, [c], -1, 255, 2)  # Edit: Changed from img to gray

    dist = cv2.distanceTransform(mask, distanceType=cv2.DIST_L2, maskSize=5)

    # Normalize the distance image for range = {0.0, 1.0}
    # so we can visualize and threshold it
    dist = cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)

    cv2.imshow("distance-transform", dist)
    cv2.waitKey(0)
    return dist

distanceTransform()


def Bluring():
    srcImage = cv2.imread("imagehh.jpg")

    gaussian_blur  = cv2.GaussianBlur(srcImage, (101,101),0)
    cv2.imshow(" bluring" , gaussian_blur )
    cv2.waitKey(0)
    return gaussian_blur

Bluring()


cv2.destroyAllWindows()

