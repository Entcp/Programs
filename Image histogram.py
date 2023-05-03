#Histogram using cv2,matplotlib.pylab
import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

#read the image
img=cv.imread("F:/overexposed.jpg",0)

#show the img
plt.subplot(2,2,1)
plt.title('original image')
plt.imshow(img,cmap='gray')

#histogram of input img
plt.subplot(2,2,2)
plt.xlim([0,255])
plt.ylim([0,11500])
plt.hist(img.flatten(),256,[0,255],color='r')
plt.legend(['Histogram of img'])
plt.title("Histogram of input image")

#performing modification on img to equilize the img
img2=cv.equalizeHist(img)
plt.subplot(2,2,3)
plt.title("Equalized img")
plt.imshow(img2,cmap='gray')

#histogram of equilized img
plt.subplot(2,2,4)
plt.hist(img2.flatten(),256,[0,255],color='r')
plt.legend(['Histogram of img'])
plt.title("Histogram of equilized image")
plt.show()

