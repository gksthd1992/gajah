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
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

%matplotlib inline

#참고 : https://bradbury.tistory.com/64

# 색상 범위 설정

lower_orange = (100, 200, 200)
upper_orange = (140, 255, 255)

lower_green = (30, 80, 80)
upper_green = (70, 255, 255)

lower_blue = (0, 180, 55)
upper_blue = (20, 255, 200)

#change this part -> google drive mount
from google.colab import drive
drive.mount('/content/drive')


#change this part -> google drive mount
import os
os.chdir("/content/drive/My Drive/image transfer")
!ls

# 이미지 파일을 읽어온다
img = mpimg.imread("rabbit2.jpg", cv2.IMREAD_COLOR)

imgplot = plt.imshow(img)
plt.show()

height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]


# BGR to HSV 변환
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(img_hsv[399][1])
imgplot = plt.imshow(img_hsv)
#print(img_hsv[img_hsv.__len__()-1]) # last array
plt.show()

#img_result = cv2.bitwise_and(img, img, img_hsv)
#imgplot = plt.imshow(img_result)
#plt.show()
middle = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
imgplot = plt.imshow(middle)
plt.show()

enter_sat = int(input("채도를 입력하세요 (-100 ~ 100): "))
print(enter_sat)

middle = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
img_change = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imgplot = plt.imshow(middle)
plt.show()
def change_saturation(width,height,img_hsv,enter_sat):
    for x in range(width-1) :
        for i in range(height-1) :
            if(enter_sat < 0) :
                img_change[i][x][1] = img_hsv[i][x][1] - img_hsv[i][x][1] * (abs(enter_sat)/100)
            if(enter_sat >= 0) :
                img_change[i][x][1] = img_hsv[i][x][1] + img_hsv[i][x][1] * (enter_sat/100)
            #img_change[i][x][1] = img_hsv[i][x][1] + img_hsv[i][x][1] * enter_sat
            img_change[i][x][0] = img_hsv[i][x][0]
            img_change[i][x][2] = img_hsv[i][x][2]


    imgplot = plt.imshow(img_change)
    plt.show()

    img_result = cv2.cvtColor(img_change, cv2.COLOR_HSV2BGR)
    imgplot = plt.imshow(img_result)
    plt.show()

    cv2.imwrite('Final_sat.jpg', img_result)
    
change_saturation(width,height,img_hsv,enter_sat)

enter_value = int(input("명도를 입력하세요 (-100 ~ 100): "))
print(enter_value)

def change_value(width,height,img_hsv,enter_value):
    for x in range(width-1) :
        for i in range(height-1) :
            if(enter_value < 0) :
                img_change[i][x][0] = img_hsv[i][x][0] - img_hsv[i][x][0] * (abs(enter_value)/100)
            if(enter_value >= 0) :
                img_change[i][x][0] = img_hsv[i][x][0] + img_hsv[i][x][0] * (enter_value/100)
            #img_change[i][x][1] = img_hsv[i][x][1] + img_hsv[i][x][1] * enter_sat
            img_change[i][x][2] = img_hsv[i][x][2]
            img_change[i][x][1] = img_hsv[i][x][1]


    imgplot = plt.imshow(img_change)
    plt.show()

    img_result = cv2.cvtColor(img_change, cv2.COLOR_HSV2BGR)
    imgplot = plt.imshow(img_result)
    plt.show()

    cv2.imwrite('Final_value.jpg', img_result)
    
change_value(width,height,img_hsv,enter_value)

