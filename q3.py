import cv2
import numpy as np

image = cv2.imread('Resources\zonda1.jpg')
image = cv2.resize(image, (800, 800))
# cv2.imshow('original image', image)
cv2.waitKey(0)

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
# cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

kernel = np.ones((3,3), np.float32)/9
box_image = cv2.filter2D(image, -1, kernel)

images = [Gaussian, box_image]
concat = cv2.hconcat(images)
cv2.imshow('gaussian vs box filter', concat)
cv2.waitKey(0)