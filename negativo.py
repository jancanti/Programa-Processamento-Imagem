import cv2
import matplotlib

img = cv2.imread('img/ingrid.jpg')
img2 = cv2.bitwise_not(img)

cv2.imshow('img2',img2)
cv2.waitKey(0)