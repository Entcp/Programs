import cv2

abc=cv2.imread('bike.jpeg',0)
cv2.imshow('bike',abc)

print(' size of the aimage',abc.size)
print(' shape of the image',abc.shape)
print(' type of the image ',abc.dtype)
print('brightness of image',abc[100,100,0])
print(abc)

cv2.waitkey(0)
cv2.destroyAllWindows()
