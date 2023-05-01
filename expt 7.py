import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets ,svm,metrics
from sklearn.datasets import load_digits
from sklearn.model_selection  import  train_test_split

digits = datasets.load_digits()
print('display datasets keys\n {}'.format(digits.keys()))

digits = load_digits()
print('shape of data ',digits.data.shape)

data_flattened = digits.images.reshape((len(digits.images),-1))
print('shape of data', digits.data.shape)

x_train, x_test, y_train, y_test = train_test_split(data_flattened,digits.target,test_size =0.2 ,shuffle = True)
print('x_train =',x_train)
print('x_test =',x_test)
print('y_train =',y_train)
print('y_test =',y_test)

print('training data size={}',format(x_train.shape))
print('training target size={}',format(y_train.shape))
print('test data size={}',format(x_test.shape))
print('test data size={}',format(x_test.shape))

classifier = svm.SVC(gamma = 0.5)

abc = classifier.fit(x_train,y_train)

y.pred = classifier.predict(x_test)
print('y=',y_pred[0])

print("confusion matrix \n %s"% metrics.confusion_matrix(y_test,y_pred))
      

