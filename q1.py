import cv2
import numpy as np

image = cv2.imread('Resources\zonda1.jpg')
image = cv2.resize(image, (400, 400))
# cv2.imshow('original image', image)
# cv2.waitKey(0)

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
# cv2.imshow('Gaussian Blurring', Gaussian)
# cv2.waitKey(0)

details = cv2.subtract(image, Gaussian)
sharpened = cv2.add(image, details)

images = [image, Gaussian, sharpened]
concat = cv2.hconcat(images)
cv2.imshow('unsharp masking', concat)
cv2.waitKey(0)