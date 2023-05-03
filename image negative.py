import cv2
import matplotlib.pyplot as plt
#read image in grayscale
img2=cv2.imread("D:\IPMV files\IPMV images\light1.jpg",0)
#display grayscale image
#cv2.imshow("Gray scale image",img2)
plt.subplot(2,2,1)
plt.title("Gray scale image")
plt.imshow(img2,cmap='gray')
#negation
abc=255-img2
plt.subplot(2,2,2)
plt.title("negative image")
plt.imshow(abc,cmap='gray')

xyz=~img2 #another way
plt.subplot(2,2,3)
plt.title("2nd method")
plt.imshow(xyz,cmap='gray')

pqr=cv2.bitwise_not(img2)
plt.subplot(2,2,4)
plt.title("3rd method")
plt.imshow(pqr,cmap='gray')

#display size and shape of the image
print("\n Size of Gray scale image: ",img2.size)
print("\n Shape of Gray scale image: ",img2.shape)


plt.show()
