import cv2
import numpy as n
import matplotlib.pyplot as plt

abc = cv2.imread('bike.jpeg',0)
xyz = np.zeros(abc.size,abc.dtype)
contrast=3.0
xyz = np.clip(constrast*abc,0,255)

plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(abc,cmap='gray')

plt.subplot(1,2,2)
plt.title('contrast')
plt.imshow(xyz,cmap='gray')

plt.show()
