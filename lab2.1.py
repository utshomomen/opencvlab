import cv2
import numpy as np
import math
import sys
import random
from os import path

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