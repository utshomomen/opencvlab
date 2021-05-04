import cv2
import numpy
import numpy as np
import math
import sys
import random
from os import path
import matplotlib.pyplot as plt
import scipy.ndimage
import numpy as np

from scipy.ndimage.filters import convolve



def loadingImageFilter():
    srcImage = cv2.imread("imagehh.jpg")
    # kernel = np.ones((5, 5), np.uint8)



    cv2.imshow("frame1", srcImage)
    cv2.waitKey(0)




loadingImageFilter()


def convolve(image, kernel, filter=0, strides=1):
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * filter) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * filter) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if filter != 0:
        imagePadded = np.zeros((image.shape[0] + filter*2, image.shape[1] + filter*2))
        imagePadded[int(filter):int(-1 * filter), int(filter):int(-1 * filter)] = image
        print(imagePadded)
    else:
        imagePadded = image

    # Iterate through image
    for y in range(image.shape[1]):
        # Exit Convolution
        if y > image.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(image.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > image.shape[0] - xKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break

    return output

def processImage(image):
  image = cv2.imread(image)
  image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
  return image


if __name__ == '__main__':
    # Grayscale Image
    image = processImage('imagehh.jpg')

    kernel = np.array([[1, 0, -1], [0, 0, 0], [-1, 0, 1]])
    output = convolve(image, kernel, filter=3)
    cv2.imshow('edge1.jpg', output)

    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    output = convolve(image, kernel, filter=3)
    cv2.imshow('edge2.jpg', output)

    kernel = (1/16)*np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    output = convolve(image, kernel, filter=3)
    cv2.imshow('blur.jpg', output)


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

