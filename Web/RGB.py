#!python

print("Content-Type: text/html")
print()

import cgi
import os
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans

form = cgi.FieldStorage()
rgb1 = form["iii"].value

image = cv2.imread(rgb1)

# 채널을 BGR -> RGB로 변경
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image = image.reshape((image.shape[0] * image.shape[1], 3))  # height, width 통합

k = 5  # 5개로 나눈다
clt = KMeans(n_clusters=k)
clt.fit(image)

# 이제 실제 clustering된 컬러값은 다음처럼 확인(RGB가 저장된다.)
def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist


hist = centroid_histogram(clt)
#print(hist)


# hist에 색깔별로 비율이 저장된다. 접근 : hist[0], hist[1] ...
# [ 0.68881873  0.09307065  0.14797794  0.04675512  0.02337756]

def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


bar = plot_colors(hist, clt.cluster_centers_)

# show our color bart
plt.figure()
plt.axis("off")
cv2.imwrite('bar.jpg',bar)




def largest_rate_rgb(hist, total, rgb):
    biggest = -1
    num = -1
    for i in range(total):
        if (biggest < hist[i]):
            biggest = hist[i]
            num = i
    return rgb[num]

print('Big : ')
big = largest_rate_rgb(hist, k, clt.cluster_centers_)
print(big)


def average_rgb(hist, total, rgb):
    average = [0, 0, 0]
    sum = [0, 0, 0]
    for i in range(total):
        sum = (sum + hist[i] * rgb[i] * 100)
    average = sum / 100
    return average


avr = average_rgb(hist, k, clt.cluster_centers_)
print('Average : ')
print(avr)



print('''
<!DOCTYPE html>
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
        <div class="mx-auto text-center">
          <img class="img-fluid mb-3 mb-lg-0" src="bg-masthead.jpg" alt="">
        </div>
        <div class="col-xl-4 col-lg-5">
          <div class="featured-text text-center text-lg-left">
            <h4></h4>

          </div>
        </div>
      </div>

      <!-- Header -->
   <header class="masthead">
    <div class="container d-flex h-100 align-items-center">
      <div class="mx-auto text-center">
        <h1 class="mx-auto my-0 text-uppercase"></h1>
        <h2>Image Transfer</h2>
        <h2></h2> Enjoy art however you want !</h2>
        <h2></h2> </h2>

      </div>
    </div>
   </header>



    <div class="container">

      <div style="max-width: 650px; margin: auto;">
        <h1 class="page-header">1.Image Upload</h1>
        <p class="lead">Select Image.</p>

        <form id="upload-image-form" action="" method="post" enctype="multipart/form-data">
          <div id="image-preview-div" style="display: none">
            <label for="exampleInputFile">Selected image:</label>
            <br>
            <img id="preview-img" src="noimage">
          </div>
          <div class="form-group">
            <input type="file" name="file" id="file" required>
          </div>
          <button class="btn btn-lg btn-primary" id="upload-button" type="submit" disabled>Upload image</button>
        </form>

        <br>
        <div class="alert alert-info" id="loading" style="display: none;" role="alert">
          Uploading image...
          <div class="progress">
            <div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
            </div>
          </div>
        </div>
        <div id="message"></div>
      </div>

      <a target="_blank" href="https://github.com/gksthd1992/gajah"><img style="position: absolute; top: 50px; right: 0; border: 0;" src="https://camo.githubusercontent.com/38ef81f8aca64bb9a64448d0d70f1308ef5341ab/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f6461726b626c75655f3132313632312e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png"></a>

    </div><!--여기거 끝 -->


    </div>

    <div style="max-width: 650px; margin: auto;">

<P><SCRIPT language="JavaScript">

</SCRIPT>


   <div class="container">
        <h1 class="page-header">RGB Recommand</h1>

        <a href = "index.html"></a>
        <img class="img-fluid mb-3 mb-lg-0" src="bar.jpg" alt="">


    </div>


    
    <div class="container">
        <form id="upload-image-form" action="" method="post" enctype="multipart/form-data">
          <h1 class="page-header">2. Choose Art</h1>
          <p class="lead">GAJAH Art Default Image</p>
          <div id="image-preview-div" style="display: none">
            <label for="exampleInputFile">Selected image:</label>
            <br>
            <img id="preview-img" src="noimage">
          </div>
          <div class="form-group">
              <p class="lead">==(flower.jpg)=-=-=-=-=-=(woman.jpg)=-=-=-=-=-=(Stary-night.jpg)= </p>
              <input type="image" src ="./a.jpg"  width="200" height="300" type= "summit" >
              <input type="image" src ="./b.jpg" alt = "ff" width="200" height="300" type= "summit" >
              <input type="image" src ="./c.jpg" alt = "Stary-night" width="200" height="300" type= "summit" >
              <p class="lead">===================================================</p>
          </div>
        </form>
    </div>

    <div class="container">
        <h1 class="page-header">GAJAH Mixing</h1>

        <form action="process_create.py">
            <h1 class="lead">Contents Image: </h1>
            <p><input type="text" name="Contents" size="20" placeholder = "ex) myFace.jpg ..."></p>
            <h1 class="lead">Style Image:</h1>
            <p><input type="text" name="Style" size="20" placeholder = "ex) Ss.jpg ..."></p>
            <p class="lead"> Are you sure? </p>

            <p><input type = "submit"></p>
            <p></p>

        </form>


    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <script src="upload-image.js"></script>
  </body>
</html>

''')
