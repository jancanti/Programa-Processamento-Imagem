import numpy as np
import cv2

img = cv2.imread('img/ingrid.jpg')
imgv = np.flipud(img)
cv2.imshow('', imgv)
cv2.waitKey(0)