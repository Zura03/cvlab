import cv2
import numpy as np

image = cv2.imread('Resources\zonda1.jpg', 0)
image = cv2.resize(image, (600, 600))

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
img = cv2.Laplacian(Gaussian, -1, 3)

# images = np.array([image, img])
cv2.imshow('edges using laplacian', img)
cv2.waitKey(0)