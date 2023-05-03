#LPF Blurring Smoothning
import cv2 
import numpy as np
import matplotlib.pylab as plt
#reading and showing the image
img=cv2.imread("F:/nature img.jpg",0)
plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(img,cmap='gray')

#creating an dummy variable with all ones to make a lpf
lpf=np.ones((5,5))/25

#applying filter to ip image
img2=cv2.filter2D(img,-1,lpf)
plt.subplot(1,2,2)
plt.title('Filtered image')
plt.imshow(img2,cmap='gray')
plt.show()
