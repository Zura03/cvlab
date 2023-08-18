import numpy as np
import cv2

image = cv2.imread('Resources\zonda1.jpg', 0)
image = cv2.resize(image, (800, 800))

edges = cv2.Canny(image, 100, 200)
images = [image, edges]
concat = cv2.hconcat(images)
cv2.imshow('canny edge', concat)
cv2.waitKey(0)
