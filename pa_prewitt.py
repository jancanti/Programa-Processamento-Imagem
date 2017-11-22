import matplotlib.pyplot as plt

from skimage.data import camera
from skimage.filters import prewitt, sobel

image = camera()
edge_prewitt = prewitt(image)
edge_sobel = sobel(image)

fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True,
                       figsize=(8, 4))

ax[0].imshow(edge_prewitt, cmap=plt.cm.gray)
ax[0].set_title('Prewitt')

ax[1].imshow(edge_sobel, cmap=plt.cm.gray)
ax[1].set_title('Sobel')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()