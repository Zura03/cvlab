import cv2
import numpy as np

image = cv2.imread('Resources\zonda1.jpg', 0)
image = cv2.resize(image, (800, 800))

kernel1 = np.array([-1, 0, 1])
kernel2 = kernel1.transpose()

im1 = cv2.filter2D(image, -1, kernel1)
im2 = cv2.filter2D(image, -1, kernel2)

img = np.sqrt((np.square(im1) + (np.square(im2))))
img = ((img-np.amin(img))/(np.amax(img) - np.amin(img)))*255
final_img = np.uint8(img)
images = [image, final_img]
concat = cv2.hconcat(images)
cv2.imshow('gradient', concat)
cv2.waitKey(0)