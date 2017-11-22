import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/ingrid.jpg', 0)

plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Imagem'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.hist(img.ravel(), 256, [0, 256])
plt.title('histograma')
plt.show()
