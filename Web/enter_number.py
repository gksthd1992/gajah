#!python
# -*- coding: utf-8 -*-

print("content-type: text/html; charset-utf-8\n")

import cgi
import cgitb    #스크립트 오류 등의 에러발생시 브라우저에 에러 내용을 보여준다.
cgitb.enable()
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2
import os
import requests
from bs4 import BeautifulSoup
import json
import sys

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

form = cgi.FieldStorage()
number_img = int(form["input_num"].value)
store_name = "middle.jpg"

input_im = "input/opencv_ori.jpg"
total_ret = 0

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
img = cv2.imread(name[number_img])
cv2.imwrite(store_name, img)


# 이름으로 불러온  사진 준비
middle = cv2.imread("middle.jpg")
ImageTrans = cv2.imread("Art123.jpg")
middle = cv2.resize(middle, dsize=(500, 600))
ImageTrans= cv2.resize(ImageTrans, dsize=(500, 600))
cv2.imwrite('middle.jpg',middle)
cv2.imwrite('ImageTrans.jpg',ImageTrans)


def combine_two(input1, input2):
    # combine_two( wartershed(img),original)
    # original이 원본 , img = 변한 화면
    # img1 = cv2.imread(input1, -1)#검은배경화면
    # img2 = cv2.imread(input2, -1)#원본사진
    img1 = cv2.imread(input1)
    img2 = cv2.imread(input2)

    # 사진 크기 조절
    img1 = cv2.resize(img1, dsize=(300, 400))
    img2 = cv2.resize(img2, dsize=(300, 400))

    rows, cols, channels = (img1.shape)

    roi = img2[0:rows, 0:cols]

    img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)

    mask_inv = cv2.bitwise_not(mask)

    img1_fg = cv2.bitwise_and(img1, img1, mask=mask)
    img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # 2개의 이미지를 합치면 바탕은 제거되고 logo부분만 합쳐짐.
    dst = cv2.add(img1_fg, img2_bg)

    # 합쳐진 이미지를 원본 이미지에 추가.
    img2[0:rows, 0:cols] = dst

    plt.imshow(img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(0)
    # 중간 파일 제거
    os.remove('middle.jpg')

    # 마지막 파일 저장
    cv2.imwrite('Final.jpg', img2)

combine_two('middle.jpg', 'ImageTrans.jpg')


# 완성된 사진 출력 화면
print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="How to create an image upload form without page refresh using Bootstrap, jQuery AJAX and PHP.">
    <meta name="author" content="ShinDarth">

    <title>GAJAH</title>

    <link rel="icon" href="11.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
    <style>body { padding-top:50px; }.navbar-inverse .navbar-nav > li > a { color: #DBE4E1; }</style>

    <!--[if IE]>
      <script src="https://cdn.jsdelivr.net/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://cdn.jsdelivr.net/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">GAJAH</a>
        </div>

        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Mixing</a></li>
            <li class="static"><a href = "index.html"> Come Back GAJAH Main</a>  </li>
          </ul>
        </div><!--.nav-collapse -->
      </div>
    </nav>

    <div class="container">
      <!-- Featured Project Row -->
      <div class="row align-items-center no-gutters mb-4 mb-lg-5">
        <img class="img-fluid mb-3 mb-lg-0" src="bg-masthead.jpg" alt="">
        <div class="mx-auto text-center">
            <h1 style = "color:rgb(255,0,0)"> Congratulations~!! </h1>
            <h2 style = "color:rgb(0,0,255)"> Enjoy your Picture!! </h2>

            <img class="img-fluid mb-3 mb-lg-0" src="Final.jpg" alt="">
         </div>
      </div>
    </div>
    
     <form action="ChromaBrightSkip.py">
            <b><h1 style = "color:rgb(0,0,0)">DO YOU WANT TO SKIP?</b></br>
            <a href = "ChromaBrightSkip.py">
                  
                  <input type = "submit" value ="SKIP" >
            </a href>
      </form>
      
<h1 class="page-header">CHROMA & BRIGHTNESS </h1>
<form  method="GET" action="ChromaBrightTest.py">
  <div class="container">
      <a> CHROMA & BRIGHTNESS </a>
      <h1 class="lead"> Chroma : </h1>
      <input type="range" name="points" min="-100" max="100"
        step="1" value="0" oninput="document.getElementById('chroma').innerHTML=this.value;">
     
      <span id="chroma"></span>
      <h1 class="lead"> Brightness : </h1>
      <input type="range" name="points2" min="-100" max="100"
        step="1" value="0" oninput="document.getElementById('brightness').innerHTML=this.value;">
      <span id="brightness"></span>
      <p><input type="submit"></p>
  </div>
</form>


  </head>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <script src="upload-image.js"></script>
</html>'''
      )
