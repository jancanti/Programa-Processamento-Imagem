import cv2
from matplotlib import pyplot as plt

# Carregar Imagem
img = cv2.imread('img/ingrid.jpg')

# Aplicando Filtro Media
dst = cv2.blur(img,(51,51))

# Gerar a imagem original + imagem desfocada
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Filtro Média')
plt.xticks([]), plt.yticks([])
plt.show()