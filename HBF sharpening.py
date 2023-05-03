#Applying filters on an image
import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

#reading and showing the image
img=cv.imread("F:/nature img.jpg",0)
plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(img,cmap='gray')

#creating a hbf
hbf=np.array([[-1,-1,-1],[-1,9.1,-1],[-1,-1,-1]])

#applying filter to ip image
img2=cv.filter2D(img,-1,hbf)
plt.subplot(1,2,2)
plt.title('Filteredl image')
plt.imshow(img2,cmap='gray')
plt.show()
