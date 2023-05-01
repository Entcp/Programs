#thresholds
import cv2
import numpy as np
import matplotlib .pylab as plt

abc=cv2.imread("pubg.jpg",0)
xyz=np.zeros(abc.shape,abc.dtype)
print(abc.shape)
 
xyz=np.zeros(abc.shape,abc.dtype)
x,xyz=cv2.threshold(abc,127,255,0)

plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(abc,cmap='gray')

plt.subplot(1,2,2)
plt.title('Threshold image')
plt.imshow(xyz,cmap='gray')
plt.show()
