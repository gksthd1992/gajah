#!python
# -*- coding: utf-8 -*-

print("content-type: text/html; charset-utf-8\n")
print()

import os
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from PIL import Image
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
import cgi


form = cgi.FieldStorage()
points = int(form["points"].value)
points2 = int(form["points2"].value)

# 참고 : https://bradbury.tistory.com/64

# 이미지 파일을 읽어온다
img = mpimg.imread("Final.jpg", cv2.IMREAD_COLOR)


height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

# BGR to HSV 변환
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#print(img_hsv[399][1])
#imgplot = plt.imshow(img_hsv)

plt.show()

# img_result = cv2.bitwise_and(img, img, img_hsv)
# imgplot = plt.imshow(img_result)
# plt.show()
middle = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
#imgplot = plt.imshow(middle)
#plt.show()

enter_sat = points
#print(enter_sat)

middle = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
img_change = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#imgplot = plt.imshow(middle)
#plt.show()


def change_saturation(width, height, img_hsv, enter_sat):
    for x in range(width - 1):
        for i in range(height - 1):
            if (enter_sat < 0):
                img_change[i][x][1] = img_hsv[i][x][1] - img_hsv[i][x][1] * (abs(enter_sat) / 100)
            if (enter_sat >= 0):
                img_change[i][x][1] = img_hsv[i][x][1] + img_hsv[i][x][1] * (enter_sat / 100)
            # img_change[i][x][1] = img_hsv[i][x][1] + img_hsv[i][x][1] * enter_sat
            img_change[i][x][0] = img_hsv[i][x][0]
            img_change[i][x][2] = img_hsv[i][x][2]

    #imgplot = plt.imshow(img_change)
    #plt.show()

    img_result = cv2.cvtColor(img_change, cv2.COLOR_HSV2BGR)
    #imgplot = plt.imshow(img_result)
    #plt.show()

    cv2.imwrite('Final_sat.jpg', img_result)


change_saturation(width, height, img_hsv, enter_sat)

#enter_value = int(input("명도를 입력하세요 (-100 ~ 100): "))
#print(enter_value)
enter_value = points2
#print(enter_value)

def change_value(width, height, img_hsv, enter_value):
    for x in range(width - 1):
        for i in range(height - 1):
            if (enter_value < 0):
                img_change[i][x][0] = img_hsv[i][x][0] - img_hsv[i][x][0] * (abs(enter_value) / 100)
            if (enter_value >= 0):
                img_change[i][x][0] = img_hsv[i][x][0] + img_hsv[i][x][0] * (enter_value / 100)
            # img_change[i][x][1] = img_hsv[i][x][1] + img_hsv[i][x][1] * enter_sat
            img_change[i][x][2] = img_hsv[i][x][2]
            img_change[i][x][1] = img_hsv[i][x][1]

    #imgplot = plt.imshow(img_change)
    #plt.show()

    img_result = cv2.cvtColor(img_change, cv2.COLOR_HSV2BGR)
    imgplot = plt.imshow(img_result)
    #plt.show()

    cv2.imwrite('Final_value.jpg', img_result)


change_value(width, height, img_hsv, enter_value)


print('CHROMA : ')
print(enter_sat)
print('BRIGHTNESS : ')
print(enter_value)

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
        <h1 class="page-header">CHROMA & BRIGHTNESS </h1>
            <img class="img-fluid mb-3 mb-lg-0" src="Final_value.jpg" alt="">
            <img class="img-fluid mb-3 mb-lg-0" src="Final_sat.jpg" alt="">
         </div>
      </div>
    </div>

    <div class="container">
      <!-- Featured Project Row -->
      <div class="row align-items-center no-gutters mb-4 mb-lg-5">
        <div class="mx-auto text-center">
        <h1 class="page-header">Original Image </h1>
            <img class="img-fluid mb-3 mb-lg-0" src="Final.jpg" alt="">
            
        <form action="index.html">
            <b><h3 style = "color:rgb(0,0,255)"> SAVE ? </h2></br>
            <a href = "index.html">
            <input type = "submit" value ="SAVE" >
             </a href>
        </form>
         </div>
      </div>
    </div>
            



  </head>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <script src="upload-image.js"></script>
</html>'''
      )
