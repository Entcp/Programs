#Thresholding  using cv2,matplotlib.pylab and numpy
# log transform
import cv2
import numpy as np
import matplotlib .pylab as plt

abc=cv2.imread("F:/nature img.jpg",0)
plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(abc,cmap='gray')

#apply log transform
c=255/np.log(1+np.max(abc))
xyz=np.zeros(abc.shape,abc.dtype)
for i in range(abc.shape[0]):
    for y in range(abc.shape[1]):
        xyz[i,y]=c*np.log(1+abc[i,y])
plt.subplot(1,2,2)
plt.title('log image')
plt.imshow(xyz,cmap='gray')
plt.show()
