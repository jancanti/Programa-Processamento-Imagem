import cv2
from matplotlib import pyplot as plt

# Carregar Imagem
img = cv2.imread('img/ingrid.jpg')

# Aplicando Filtro Mediano
dst = cv2.medianBlur(img,25)

# Gerar a imagem original + imagem desfocada
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Filtro Mediano')
plt.xticks([]), plt.yticks([])
plt.show()