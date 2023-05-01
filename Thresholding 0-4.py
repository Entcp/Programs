#Thresholding 0-4
import cv2
import numpy as np
import matplotlib.pylab as plt

#Read Image
abc=cv2.imread("E:\IPMV images\photo-1533109721025-d1ae7ee7c1e1.jfif",0)

plt.subplot(2,3,1)
plt.title('Original Image')
plt.imshow(abc,cmap='gray')

B,a=cv2.threshold(abc,127,255,0)
plt.subplot(2,3,2)
plt.title('Binary')
plt.imshow(a,cmap='gray')

B,a=cv2.threshold(abc,127,255,1)
plt.subplot(2,3,3)
plt.title('Inverted Binary')
plt.imshow(a,cmap='gray')

B,a=cv2.threshold(abc,127,255,2)
plt.subplot(2,3,4)
plt.title('Truncated')
plt.imshow(a,cmap='gray')

B,a=cv2.threshold(abc,127,255,3)
plt.subplot(2,3,5)
plt.title('To Zero')
plt.imshow(a,cmap='gray')

B,a=cv2.threshold(abc,127,255,4)
plt.subplot(2,3,6)
plt.title('To Zero Inverted')
plt.imshow(a,cmap='gray')
plt.show()
