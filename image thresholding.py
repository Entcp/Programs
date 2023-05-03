#Thresholding  using cv2,matplotlib.pylab and numpy
import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

#read the image
img=cv.imread("F:/nature img.jpg",1)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

#show the img
plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(img,cmap='gray')

#create a dummy varible
img2=np.zeros(img.shape,img.dtype)
a,img2=cv.threshold(img,127,255,0)

#showing result
plt.subplot(1,2,2)
plt.title('Threshold Img')
plt.imshow(img2,cmap='gray')   
plt.show()

