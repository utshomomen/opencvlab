import cv2
import numpy as np
import math
import sys
import random
from os import path
import matplotlib.pyplot as plt

def loadingImageFilter():
    srcImage = cv2.imread("imagehh.jpg")
   # kernel = np.ones((5, 5), np.uint8)



    cv2.imshow("frame1", srcImage)
    cv2.waitKey(0)




loadingImageFilter()

def convolution():
    srcImage = cv2.imread("imagehh.jpg")


    # edge detection filter
    kernel = np.array([[1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1]])
    kernel = kernel / sum(kernel)

    img_rst = cv2.filter2D(srcImage, -1, kernel)

    cv2.imshow("edgedetecton", img_rst)
    cv2.waitKey(0)
    srcImage = grayImg = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)




    #highpasfilter
    kernel = np.array([[0.0, -1.0, 0.0],
                       [-1.0, 4.0, -1.0],
                       [0.0, -1.0, 0.0]])

    kernel = kernel / (np.sum(kernel) if np.sum(kernel) != 0 else 1)



    img_rst2 = cv2.filter2D(srcImage, -1, kernel)

    cv2.imshow("highpassfilter", img_rst2)
    cv2.waitKey(0)

    #  lowpassfilter


    kernel = np.array([[0.0, -1.0, 0.0],
                       [-1.0, 4.0, -1.0],
                       [0.0, -1.0, 0.0]])

    kernel = kernel / (np.sum(kernel) if np.sum(kernel) != 0 else 1)



    img_rst2 = cv2.filter2D(srcImage, -1, kernel)

    cv2.imshow("lowpasfilter", img_rst2)
    cv2.waitKey(0)


     #sharpened
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    kernel = kernel / (np.sum(kernel) if np.sum(kernel) != 0 else 1)

    img_rst2 = cv2.filter2D(srcImage, -1, kernel)

    cv2.imshow("sharpened", img_rst2)
    cv2.waitKey(0)


    #blur
    kernel = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]])

    kernel = kernel / (np.sum(kernel) if np.sum(kernel) != 0 else 1)

    img_rst2 = cv2.filter2D(srcImage, -1, kernel)

    cv2.imshow("blur", img_rst2)
    cv2.waitKey(0)







convolution()

def relu(x):
    return max(0.0, x)

def ReluAndMaxPool(x):




    srcImage = cv2.imread("imagehh.jpg")

    b, g, r = cv2.split(srcImage)
    tir = cv2.imread("imagehh.jpg", 0)
    qb = cv2.imread("imagehh.jpg", 0)
    channel_img = np.zeros((b.shape[0], b.shape[1], 5))

    channel_img[:, :, 0] = b
    channel_img[:, :, 1] = g
    channel_img[:, :, 2] = r
    channel_img[:, :, 3] = tir
    channel_img[:, :, 4] = qb
    cv2.imshow("ch1", b)
    cv2.waitKey(0)

    cv2.imshow("ch2", g)
    cv2.waitKey(0)

    cv2.imshow("ch3", r)
    cv2.waitKey(0)

    cv2.imshow("ch4", tir)
    cv2.waitKey(0)

    cv2.imshow("ch5", qb)
    cv2.waitKey(0)



    mat = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]])

    mat = mat / sum(mat)
    relu = max(0.0, x)
    M, N = mat.shape
    K = 2
    L = 2

    MK = M // K
    NL = N // L
    print(mat[:MK * K, :NL * L].reshape(MK, K, NL, L).max(axis=(1, 3)))

    max_pool = cv2.filter2D(srcImage, -1, mat )

    cv2.imshow("max pool", max_pool)
    cv2.waitKey(0)


ReluAndMaxPool(relu(x=1))

# def channels ():
#     srcImage = cv2.imread("imagehh.jpg")
#     Mat  srcImage(5, 5, CV_64FC3);
#     Mat ch1, ch2, ch3;
#
#     vector < Mat > channels(3);
#
#     split(img, channels);
#
#     ch1 = channels[0];
#     ch2 = channels[1];
#     ch3 = channels[2];
#
#
#
#     channels()