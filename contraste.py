import cv2

img = cv2.imread('img/ingrid-color.jpg', 1)

# CLAHE (Contraste Limitado Adaptado a Equalização do Histograma)
clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
l, a, b = cv2.split(lab)  # separar os 3 canais diferentes

l2 = clahe.apply(l)  # aplicar CLAHE no canal L

lab = cv2.merge((l2, a, b))  # mesclar canais
img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # converter de LAB para BGR
cv2.imshow('Increased contrast', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()