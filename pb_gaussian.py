import cv2
from matplotlib import pyplot as plt

# Carregar Imagem
img = cv2.imread('img/ingrid.jpg')

# Aplicando Filtro Gaussiano
dst = cv2.GaussianBlur(img,(51,51),0)

# Gerar a imagem original + imagem desfocada
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Desfoque Gaussiano')
plt.xticks([]), plt.yticks([])
plt.show()