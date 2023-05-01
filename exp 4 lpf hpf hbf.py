#LPF 
import cv2
import numpy as np
import matplotlib .pyplot as plt

abc=cv2 .imread('E:\Ruturaj 40\OIP.jpeg', 0)

plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(abc,cmap='gray')

lpf=np.ones((5,5))/25
xyz=cv2.filter2D(abc, -1, lpf)


plt.subplot(1,2,2)
plt.title('blur image')
plt.imshow(xyz,cmap='gray')
plt.show()



#HPF
import cv2
import numpy as np
import matplotlib .pyplot as plt

abc=cv2 .imread("E:\Ruturaj 40\OIP (2).jpeg", 0)

plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(abc,cmap='gray')

HPF=np.array([[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,24,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]])/9
xyz=cv2.filter2D(abc, -1,HPF)


plt.subplot(1,2,2)
plt.title('Edge image')
plt.imshow(xyz,cmap='gray')
plt.show()



#diagonal edge image
import cv2
import numpy as np
import matplotlib .pyplot as plt

abc=cv2 .imread('E:/IPMV images/blobs.png', 0)

plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(abc,cmap='gray')

HPF=np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])/9
xyz=cv2.filter2D(abc, -1,HPF)


plt.subplot(1,2,2)
plt.title(' Diagonal Edge image')
plt.imshow(xyz,cmap='gray')
plt.show()


#HIGH BOOST
import cv2
import numpy as np
import matplotlib .pyplot as plt

abc=cv2 .imread('E:/IPMV images/blobs.png', 0)

plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(abc,cmap='gray')

HPF=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])/9
xyz=cv2.filter2D(abc, -1,HPF)


plt.subplot(1,2,2)
plt.title('Edge image')
plt.imshow(xyz,cmap='gray')
plt.show()
