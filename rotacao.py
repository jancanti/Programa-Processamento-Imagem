import cv2
import numpy as np

img = cv2.imread('img/ingrid.jpg', 0)
img90 = np.rot90(img)
cv2.imshow('', img90)
cv2.waitKey(0)
