import cv2
import numpy as np

image = cv2.imread('Resources\zonda1.jpg')

cv2.imshow('original image', image)
cv2.waitKey(0)

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)