import numpy as np
import cv2
from matplotlib import pyplot as plt

ims=cv2.imread('rabit.jpg')
im = cv2.imread("rabit.jpg",0)
im_flat = np.reshape(im,(im.shape[0]*im.shape[1]))

[hist, _] = np.histogram(im, bins=256, range=(0, 255))
# Normalization so we have probabilities-like values (sum=1)
hist = 1.0*hist/np.sum(hist)

val_max = -999
thr = -1
for t in range(1,255):
    # Non-efficient implementation
    q1 = np.sum(hist[:t])
    q2 = np.sum(hist[t:])
    m1 = np.sum(np.array([i for i in range(t)])*hist[:t])/q1
    m2 = np.sum(np.array([i for i in range(t,256)])*hist[t:])/q2
    val = q1*(1-q1)*np.power(m1-m2,2)
    if val_max < val:
        val_max = val
        thr = t

print("Threshold: {}".format(thr))


plt.subplot(131)
plt.imshow(ims)
#plt.subplot(132)
#plt.hist(im_flat, bins=256, range=(0, 255))
plt.subplot(133)
plt.imshow(im > thr, cmap = 'gray')
plt.show()
