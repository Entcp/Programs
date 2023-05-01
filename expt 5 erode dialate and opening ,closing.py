#dilation
import cv2
import numpy as np
import matplotlib .pylab as plt

abc=cv2.imread("E:\Ruturaj 40\OIP (4).jpeg",0)

plt.subplot(2,2,1)
plt.title('original image')
plt.imshow(abc,cmap = "gray")


strct =np.ones((3,3),np.uint8)
xyz=cv2.dilate(abc,strct,iterations=4)
plt.subplot(2,2,2)
plt.title('Output  image')
plt.imshow(xyz,cmap = "gray")
plt.show()



#opening image
import cv2
import numpy as np
import matplotlib .pylab as plt

abc=cv2.imread("E:\Ruturaj 40\download.jpeg",0)

plt.subplot(2,2,1)
plt.title('original image')
plt.imshow(abc,cmap = "gray")


strct =np.ones((3,3),np.uint8)
xyz=cv2.erode(abc,strct,iterations=2)
plt.subplot(2,2,2)
plt.title('eroded  image')
plt.imshow(xyz,cmap = "gray")

x=abc-xyz
plt.subplot(2,2,3)
plt.title('opening   image')
plt.imshow(x,cmap = "gray")
plt.show()


#direct closing
import cv2
import numpy as np
import matplotlib .pylab as plt

abc=cv2.imread("E:\Ruturaj 40\OIP (6).jpeg",0)

plt.subplot(2,2,1)
plt.title('original image')
plt.imshow(abc,cmap = "gray")


strct =np.ones((3,3),np.uint8)
xyz=cv2.dilate(abc,strct,iterations=1)
plt.subplot(2,2,2)
plt.title('Dilate image')
plt.imshow(xyz,cmap = "gray")

strct =np.ones((3,3),np.uint8)
x=cv2.erode(xyz,strct,iterations=1)
plt.subplot(2,2,3)
plt.title('Erode  image')
plt.imshow(x,cmap = "gray")



closing2=cv2.morphologyEx(x,cv2.MORPH_CLOSE,strct)
plt.subplot(2,2,4)
plt.title('Direct closing image')
plt.imshow(x,cmap = "gray")
plt.show()

