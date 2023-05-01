#HISTOGRAM OF AN IMAGE
import cv2
import numpy as np
import matplotlib .pyplot as plt
abc=cv2.imread('bike.jpeg',0)

plt.subplot(2,2,1)
plt.title('Original image')
plt.imshow(abc,cmap='gray')

plt.subplot(2,2,2)
plt.xlim(0,255)
plt.ylim(0,800)
plt.hist(abc.flatten(),255,[0,255],color='r')
plt.legend(['Histogram'])


xyz=cv2.equalizeHist(abc)
plt.subplot(2,2,3)
plt.title('Second Image')
plt.imshow(xyz,cmap='gray')

plt.subplot(2,2,4)
plt.xlim(0,255)
plt.ylim(0,800)
plt.hist(xyz.flatten(),255,[0,255],color='b')
plt.legend([' Equalize Histogram'])
plt.show()
