import cv2

abc = cv2.imread('bike.jpeg',1)


xyz = 255-abc
cv2.imshow('negative',xyz)
cv2.waitKey(0)
cv2.destroyAllWindows()
