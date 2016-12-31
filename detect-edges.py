import cv2
import numpy as np

img = cv2.imread('bear.jpg')
print(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
gray = cv2.GaussianBlur(neg_img, (3, 3), 0)
edges = cv2.Canny(img,10,200)

print (img)

cv2.imshow('bear',edges)

cv2.waitKey(0)
