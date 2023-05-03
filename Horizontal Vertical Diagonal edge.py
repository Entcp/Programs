#Applying filters on an image(horizontledge,vertical ,diagonal)
import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

#reading and showing the image
img=cv.imread("F:/nature img.jpg",0)
plt.subplot(2,2,1)
plt.title('original image')
plt.imshow(img,cmap='gray')

#creating a Horizontal mask
hor=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
#applying filter to ip image
img2=cv.filter2D(img,-1,hor)
plt.subplot(2,2,2)
plt.title('horizontal image')
plt.imshow(img2,cmap='gray')

#creating a vertical mask 
hbf=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
#applying filter to ip image
img2=cv.filter2D(img,-1,hbf)
plt.subplot(2,2,3)
plt.title('vertical image')
plt.imshow(img2,cmap='gray')

#creating a diagonal mask
dia=np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
#applying filter to ip image
img2=cv.filter2D(img,-1,dia)
plt.subplot(2,2,4)
plt.title('diagonal filtered image')
plt.imshow(img2,cmap='gray')
plt.show()


