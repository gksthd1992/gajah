#__author__="samsjang@naver.com"
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from scipy.ndimage import label


def wartershed():
    img = cv2.imread('rabbit2.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel, iterations=2)
    #cv2.imshow('watershed', opening)
    #border = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    border = cv2.dilate(opening, kernel, iterations=3)
    border = border - cv2.erode(border, None)


    dt = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    dt = ((dt-dt.min())/ (dt.max()-dt.min())*255).astype(np.uint8)
    ret, dt = cv2.threshold(dt, 180, 255, cv2.THRESH_BINARY)

    marker, ncc = label(dt)
    marker = marker*(255/ncc)

    # ncc = label 수 . coin : 24
    # marker 은 배열.

    #배경, 객체가 아닌 부분 -> 255 흰색 처리
    marker[marker==255] = 255
    marker = marker.astype(np.int32)
    cv2.watershed(img, marker)

    # -1 이면 edge
    marker[marker == -1] = 0
    marker = marker.astype(np.uint8)
    marker = 255-marker

    # 애매한 부분 -> 검정 처리
    marker[marker != 255] = 0
    marker = cv2.dilate(marker, None)
    img[marker==255] = (0,0,255)

    cv2.imshow('watershed', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

wartershed()
