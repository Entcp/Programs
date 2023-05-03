import cv2 as cv
import numpy as np
import matplotlib.pylab as plt
from sklearn import datasets,svm,metrics
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

digits=datasets.load_digits()
print('digits datasets keys\n {}'.format(digits.keys()))

#to show shape of digits
digits=load_digits()
print('shape of data',digits.data.shape)

print('dataset target name:\n{}\n'.format(digits.target_names))
print('shape of dataset:{}'.format(digits.data.shape))
print('shape of target:{}'.format(digits.target.shape))
print('shape of images:{}',digits.images.shape)
#loop to give image pixel value
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.axis('off')
    plt.imshow(digits.images[i],cmap='gray_r',interpolation='nearest')
    plt.title('target {}'.format(i))
plt.show()
