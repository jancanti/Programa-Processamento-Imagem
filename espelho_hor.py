import numpy as np
import cv2

img = cv2.imread('img/ingrid.jpg')
imgh = np.fliplr(img)
cv2.imshow('', imgh)
cv2.waitKey(0)