#Thresholding  using cv2,matplotlib.pylab and numpy
import cv2 as cv
import numpy as np
import matplotlib.pylab as plt
#read the image
img=cv.imread("D:\IPMV files\IPMV images\light1.jpg",0)

#show the img
plt.subplot(2,3,1)
plt.title('original image')
plt.imshow(img,cmap='gray')

#using opencv instruction
a,img2=cv.threshold(img,127,255,0)
#showing result
plt.subplot(2,3,2)
plt.title('Binary')
plt.imshow(img2,cmap='gray')

b,img2=cv.threshold(img,127,255,1)
plt.subplot(2,3,3)
plt.title('Inverted Binary')
plt.imshow(img2,cmap='gray')

c,img2=cv.threshold(img,127,255,2)
plt.subplot(2,3,4)
plt.title('Truncated')
plt.imshow(img2,cmap='gray')

c,img2=cv.threshold(img,127,255,3)
plt.subplot(2,3,5)
plt.title('To zero')
plt.imshow(img2,cmap='gray')

d,img2=cv.threshold(img,127,255,4)
plt.subplot(2,3,6)
plt.title('To zero inverted')
plt.imshow(img2,cmap='gray')
plt.show()

