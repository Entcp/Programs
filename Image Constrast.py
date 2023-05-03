#Changing the image constrast
import cv2
import numpy as np
import matplotlib .pylab as plt

abc=cv2.imread("F:/nature img.jpg",0)
xyz=np.zeros(abc.size,abc.dtype)

constrast=6.0
xyz=np.clip(constrast*abc,0,255)

plt.subplot(1,2,1)
plt.title("original image")
plt.imshow(abc,cmap='gray')

plt.subplot(1,2,2)
plt.title("constrast image")
plt.imshow(xyz,cmap='gray')
plt.show()

