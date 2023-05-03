import cv2
abc= cv2.imread("F:/cameraman.jpg",1)
cv2.imshow('cameraman',abc)
print("size of the image:",abc.size)
print("shape of image:", abc.shape)
a=abc[200:,150:]
cv2.imshow("crop",a)
cv2.waitKey(0)
cv2.destroyAllWindows()


