import os
import cv2
import sys
import numpy as np
import scipy.io
import scipy.misc
import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from PIL import Image
from sklearn.cluster import KMeans

%matplotlib inline

#참고 :  https://inyl.github.io/programming/2017/07/31/opencv_image_color_cluster.html

from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir("/content/drive/My Drive/image transfer")
!ls

image = cv2.imread("rabbit2.jpg")

print(image.shape)
# (92, 272, 3)

# 채널을 BGR -> RGB로 변경
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image = image.reshape((image.shape[0] * image.shape[1], 3)) # height, width 통합
print(image.shape)
# (25024, 3)

k = 5 # 5개로 나눈다
clt = KMeans(n_clusters = k)
clt.fit(image)

#이제 실제 clustering된 컬러값은 다음처럼 확인(RGB가 저장된다.)
for center in clt.cluster_centers_:
    print(center)
    
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
print(hist)
#hist에 색깔별로 비율이 저장된다. 접근 : hist[0], hist[1] ...
#[ 0.68881873  0.09307065  0.14797794  0.04675512  0.02337756]

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
plt.imshow(bar)
plt.show()

def largest_rate_rgb(hist,total,rgb):
    biggest=-1
    num=-1
    for i in range(total) : 
        if(biggest<hist[i]) :
            biggest=hist[i]
            num=i
    return rgb[num]
big = largest_rate_rgb(hist,k,clt.cluster_centers_)
print(big)

def average_rgb(hist, total, rgb):
    average = [0,0,0]
    sum = [0,0,0]
    for i in range(total) :
        sum = (sum + hist[i]*rgb[i]*100)
    average = sum/100
    return average
  
avr = average_rgb(hist, k, clt.cluster_centers_)
print(avr)
