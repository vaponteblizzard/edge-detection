import cv2
import numpy as np

img = cv2.imread('bear.jpg')
print(img)
edges = cv2.Canny(img,100,200)

print (img)

cv2.imshow('bear',edges)

cv2.waitKey(0)
