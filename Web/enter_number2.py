#!python
# -*- coding: utf-8 -*-

print("content-type: text/html; charset-utf-8\n")

import cgi
import cgitb  # 스크립트 오류 등의 에러발생시 브라우저에 에러 내용을 보여준다.

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


img2 = cv2.imread('ART123.jpg')


cv2.imwrite('Final.jpg', img2)
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
            <img class="img-fluid mb-3 mb-lg-0" src="ART123.jpg" alt="">
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
