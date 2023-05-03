#performing morphological operations on an image(edge detection)
import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

#reading the original image
img=cv.imread("E:/IPMV images/blobs.png",0)
#show the img
plt.subplot(2,2,1)
plt.title('original image')
plt.imshow(img,cmap='gray')
#Structuring element
strct=np.ones([3,3],np.uint8)
#dilate the img
imgE=cv.dilate(img,strct,iterations=1)
plt.subplot(2,2,2)
plt.title('dilated image')
plt.imshow(imgE,cmap='gray')
plt.show()

