import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import imread

img = cv2.imread('img\ingrid-color.jpg', cv2.COLOR_RGB2BGR)
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(gimg), plt.title('Preto e Branco')
plt.xticks([]), plt.yticks([])
plt.show()