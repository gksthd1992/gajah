#!python
# -*- coding: utf-8 -*-

print("content-type: text/html; charset-utf-8\n")

import cgi
import cgitb    #스크립트 오류 등의 에러발생시 브라우저에 에러 내용을 보여준다.
cgitb.enable()
import matplotlib.pyplot as plt
import numpy as np

import cv2


input_im = "input/for_ob.jpg"
img2 = cv2.imread(input_im)
cv2.imwrite('input/Final.jpg', img2)

"""
import cgi
import os
import json
import sys
"""

OUTPUT_DIR = 'input/output11/'
MEAN_VALUES = np.array([123.68, 116.779, 103.939]).reshape((1,1,1,3))

get_object = "input/get_object.jpg"
mix_img = "input/opencv.jpg"
water = "input/water.jpg"


"""
name = ["C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret0.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret1.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret2.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret3.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret4.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret5.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret6.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret7.jpg"]
"""
name = ["input/ret0.jpg",
        "input/ret1.jpg",
        "input/ret2.jpg",
        "input/ret3.jpg",
        "input/ret4.jpg",
        "input/ret5.jpg",
        "input/ret6.jpg",
        "input/ret7.jpg",
        "input/ret8.jpg",
        "input/ret9.jpg",
        "input/ret10.jpg",
        "input/ret11.jpg",
        "input/ret12.jpg",
        "input/ret13.jpg"]

def wartershed(input_im):
    img = cv2.imread(input_im)
    img = cv2.resize(img, dsize=(300, 400))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)

    unknown = cv2.subtract(sure_bg, sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)
    print("the ret is ",ret)
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv2.watershed(img, markers)
    img[markers == -1] = [0, 0, 0]

    #want = input("원하는 번호를 입력하세요: ")
    want = 2
    ret = int(ret)
    for i in range(ret + 1):
        if i != int(want):
            img[markers == i] = [0, 0, 0]

    cv2.imwrite(name[want], img)
    return img

    """
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(ret)
    # markers==1 이면 배경
    ret = int(ret)
    for i in range(ret + 1):
        if i != 3:
            img[markers == i] = [0, 0, 0]
    """
    cv2.imwrite('input/water.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #return "get_object.jpg"
def obj_wartershed(input_im,want):
    img = cv2.imread(input_im)
    img = cv2.resize(img, dsize=(300, 400))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)

    unknown = cv2.subtract(sure_bg, sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)
    total_ret = ret
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv2.watershed(img, markers)
    img[markers == -1] = [0, 0, 0]

    ret = int(ret)
    for i in range(ret + 1):
        if i != int(want):
            img[markers == i] = [0, 0, 0]

    cv2.imwrite(name[want], img)
    return img

    """
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(ret)
    # markers==1 이면 배경
    ret = int(ret)
    for i in range(ret + 1):
        if i != 3:
            img[markers == i] = [0, 0, 0]
    """
    cv2.imwrite('input/water.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # return "get_object.jpg"
def make_obj_img(input, ret) :
    for i in range(ret):
        obj_wartershed(input,i+1)
#    print(ret)

def get_total_ret(input_im):
    img = cv2.imread(input_im)
    img = cv2.resize(img, dsize=(300, 400))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)

    unknown = cv2.subtract(sure_bg, sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)
    return ret

total_ret = get_total_ret(input_im)
make_obj_img(input_im,total_ret)
print(total_ret)
