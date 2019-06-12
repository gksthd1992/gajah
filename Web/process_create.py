#!python
# -*- coding: utf-8 -*-

print("content-type: text/html; charset-utf-8\n")
print()

import cgi, os
# import matplotlib.pyplot as plt
from PIL import Image
import cv2

form = cgi.FieldStorage()
contentsImage = form["Contents"].value
StyleImage = form["Style"].value

# print(contentsImage,"hi",  StyleImage)

# 이름으로 불러온  사진 준비
Contents2 = cv2.imread(StyleImage)
Contents1 = cv2.imread(contentsImage)
cv2.imwrite('input/for_ob.jpg',Contents1)

Contents2 = cv2.resize(Contents2, dsize=(500, 600))
cv2.imwrite('ART123.jpg', Contents2)



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

      <script src="makeobject.js?ver=1"></script>
      <script src="https://cdn.jsdelivr.net/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://cdn.jsdelivr.net/respond/1.4.2/respond.min.js"></script>
      <script src="http://code.jquery.com/jquery-latest.js"></script>
        <meta http-equiv="Expires" content="Mon, 06 Jan 1990 00:00:01 GMT">
        <meta http-equiv="Expires" content="-1">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Cache-Control" content="no-cache">
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
     <form action="enter_number2.py">
            <b><h1 style = "color:rgb(0,0,0)">DO YOU WANT TO SKIP?</b></br>
            <a href = "enter_number2.py">
                  
                  <input type = "submit" value ="SKIP" >
            </a href>
      </form>
      
    <form action="a.html">
        <b><h1 style = "color:rgb(0,0,0)">part image transfer</b></br>
        <input type="button" id="makeob" value="create object!!" >
    </form>
        </br></br>

        <b><h1 style = "color:rgb(0,0,0)">which one you want to choose?</b></br>
    <form action="enter_number.py">
          <p><input type = "text" name = "input_num" size="20" placeholder = "ex) 1,2,3...">
          <input type = "submit" ></p></br></br></br></br></br></br>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <script src="makeobject.js?ver=1"></script>
        <!-- <input type="button" name="btn2" value="버튼2" onclick="alert('Hi~~!!')">-->
    </form>

  </head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <script src="upload-image.js"></script>
    

</html>'''
      )
