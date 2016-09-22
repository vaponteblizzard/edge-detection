import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bear.jpg',0)
edges = cv2.Canny(img,200,200)

plt.subplot(121),plt.imshow(img,cmap = 'white')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'white')
plt.title('Edged'), plt.xticks([]), plt.yticks([])

plt.show()

