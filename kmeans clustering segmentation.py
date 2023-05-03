#k-mean segmentation
import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

#import and show the image
img=cv.imread("C:/Users/student/Downloads/pexels-simon-berger-1323550.jpg",1)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.subplot(2,2,1)
plt.title('original image')
plt.imshow(img)

#AS img is 3d we convert it in 2d for applying kmean seg by using rehape
pel_values=img.reshape((-1,3))
#converting into float
pel_values=np.float32(pel_values)

criteria=(cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,100,0.85)
#PERfORMING K-MEANS CLUSTERING WITH n NUMBER of clusters with random centers
#chosen initially
k=3
retval,labels,centers=cv.kmeans(pel_values,k,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
print('retval',retval)
print('labels',labels )
print('centers',centers)
#convert data into 8 bit vals
centers=np.uint8(centers)
segmented_data=centers[labels.flatten()]
#reshape data into the original image dimensions
segmented_image=segmented_data.reshape((img.shape))
plt.subplot(2,2,2)
plt.title('k=3')
plt.imshow(segmented_image)

k=6
retval,labels,centers=cv.kmeans(pel_values,k,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
print('retval',retval)
print('labels',labels )
print('centers',centers)
#convert data into 8 bit vals
centers=np.uint8(centers)
segmented_data=centers[labels.flatten()]
#reshape data into the original image dimensions
segmented_image=segmented_data.reshape((img.shape))
plt.subplot(2,2,3)
plt.title('k=6')
plt.imshow(segmented_image)

k=20
retval,labels,centers=cv.kmeans(pel_values,k,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
print('retval',retval)
print('labels',labels )
print('centers',centers)
#convert data into 8 bit vals
centers=np.uint8(centers)
segmented_data=centers[labels.flatten()]
#reshape data into the original image dimensions
segmented_image=segmented_data.reshape((img.shape))
plt.subplot(2,2,4)
plt.title('k=20')
plt.imshow(segmented_image)
plt.show()
