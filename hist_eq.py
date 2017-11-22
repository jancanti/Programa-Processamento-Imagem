import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/ingrid.jpg', 0)
res = cv2.imread('img/res.png', 0)
equ = cv2.equalizeHist(img)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Imagem'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histograma')
plt.subplot(2,2,3),plt.imshow(res,cmap = 'gray')
plt.title('Imagem Equalizada'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.hist(res.ravel(), 256, [0, 256])
plt.title('Histograma Equalizado')
plt.show()
