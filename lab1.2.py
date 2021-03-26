import cv2
import imutils as imutils
import numpy as np
import random
import sys
from os import path
import matplotlib.pyplot as plt
import matplotlib.colors
import scipy


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


def build_is_hist(img):
    pass
    hei = img.shape[0]
    wid = img.shape[1]
    ch = img.shape[2]
    Img = np.zeros((hei+4, wid+4, ch))
    for i in range(ch):
        Img[:,:,i] = np.pad(img[:,:,i], (2,2), 'edge')
    hsv = (matplotlib.colors.rgb_to_hsv(Img))
    hsv[:,:,0] = hsv[:,:,0] * 255
    hsv[:,:,1] = hsv[:,:,1] * 255
    hsv[hsv>255] = 255
    hsv[hsv<0] = 0
    hsv = hsv.astype(np.uint8).astype(np.float64)
    fh = np.array([[-1.0,0.0,1.0],[-2.0,0.0,2.0],[-1.0,0.0,1.0]])
    fv = fh.conj().T

    H = hsv[:,:,0]
    S = hsv[:,:,1]
    I = hsv[:,:,2]



    h = H[2:hei+2,2:wid+2]
    s = S[2:hei+2,2:wid+2]
    i = I[2:hei+2,2:wid+2].astype(np.uint8)



    Rho = np.zeros((hei+4,wid+4))
    for p in range(2,hei+2):
        for q in range(2,wid+2):
            tmpi = I[p-2:p+3,q-2:q+3]
            tmps = S[p-2:p+3,q-2:q+3]
            corre = np.corrcoef(tmpi.flatten('F'),tmps.flatten('F'))
            Rho[p,q] = corre[0,1]

    rho = np.abs(Rho[2:hei+2,2:wid+2])
    rho[np.isnan(rho)] = 0
    # rd = (rho*ds).astype(np.uint32)
    Hist_I = np.zeros((256,1))
    Hist_S = np.zeros((256,1))

    # for n in range(0,255):
        # temp = np.zeros(di.shape)
        # temp[i==n] = di[i==n]
        # Hist_I[n+1] = np.sum(temp.flatten('F'))
        # # temp = np.zeros(di.shape)
        # temp[i==n] = rd[i==n]
        # Hist_S[n+1] = np.sum(temp.flatten('F'))

    return Hist_I, Hist_S





def increasingContrast():
    img = cv2.imread('imagehh.jpg')
    cv2.imshow('test', img)
    cv2.waitKey(0)
    # alpha = 0.5
    # hist_i, hist_s = build_is_hist(img)
    # hist_c = alpha * hist_s + (1 - alpha) * hist_i
    # hist_sum = np.sum(hist_c)
    # hist_cum = hist_c.cumsum(axis=0)
    #
    # hsv = matplotlib.colors.rgb_to_hsv(img)
    # h = hsv[:, :, 0]
    # s = hsv[:, :, 1]
    # i = hsv[:, :, 2].astype(np.uint8)
    #
    # c = hist_cum / hist_sum
    # s_r = (c * 255)
    # i_s = np.zeros(i.shape)
    # for n in range(0, 255):
    #     i_s[i == n] = s_r[n + 1] / 255.0
    # i_s[i == 255] = 1
    # hsi_o = np.stack((h, s, i_s), axis=2)
    # result = matplotlib.colors.hsv_to_rgb(hsi_o)
    #
    # result = result * 255
    # result[result > 255] = 255
    # result[result < 0] = 0
    # return result.astype(np.uint8)
    img = np.uint16(img)
    img = np.clip(2.0 * img, 0, 255)
    img = np.uint8(img)
    cv2.imshow("High contrast", img)
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


def Bluring(dist):

    img = cv2.imread("imagehh.jpg")
    integral = cv2.integral(img)
    h = img.shape[0]
    w = img.shape[1]
    c = img.shape[2]
    blur = np.zeros(img.shape, dtype=np.uint8)
    for x in range(h):
        for y in range(w):
            for ch in range(c):
                d = dist[x, y]
                kernelX2 = min(int(x + 3 * d), h - 1)
                kernelX1 = max(int(x - 3 * d), 0)
                kernelY1 = max(int(y - 3 * d), 0)
                kernelY2 = min(int(y + 3 * d), w - 1)

                blur[x, y, ch] = (integral[kernelX2 + 1, kernelY2 + 1, ch] + integral[kernelX1, kernelY1, ch] -
                                     integral[kernelX1, kernelY2 + 1, ch] - integral[kernelX2 + 1, kernelY1, ch]) // ((kernelX2 - kernelX1 + 1) * (kernelY2 - kernelY1 + 1))

    cv2.imshow("Average blur" , blur)
    cv2.waitKey(0)
    return blur


Bluring(distanceTransform())


cv2.destroyAllWindows()

