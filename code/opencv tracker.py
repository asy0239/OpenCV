import numpy as np
import cv2

def change_color(x):
    r = cv2.getTrackbarPos('R', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    b = cv2.getTrackbarPos('B', 'Image')
    image[:] = [b,g,r]
    cv2.imshow('Image', image)

image = np.zeros((600,400,3), np.uint8)
cv2.namedWindow('Image')

cv2.createTrackbar("R", "Image", 0, 255, change_color)
cv2.createTrackbar('G', 'Image', 0, 255, change_color)
cv2.createTrackbar("B", "Image", 0, 255, change_color)

cv2.imshow('image', image)
cv2.waitKey(0)

# 주피터로 가능하지 않으므로 파이참이나 다른 개발환경에서 실행 해야함.