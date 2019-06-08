#!python
# -*- coding: utf-8 -*-

print("Content-Type: text/html; charset-utf-8\n")


import cgi
import os
# import matplotlib.pyplot as plt
from PIL import Image
import cv2


form = cgi.FieldStorage()
contentsImage = form["aa"].value
print(contentsImage)
print("hello world!")
#StyleImage = form["Style"].value
