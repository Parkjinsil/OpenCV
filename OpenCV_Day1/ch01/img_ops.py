import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = np.empty((480,640), dtype=np.uint8)
img2 = np.zeros((480,640,3), dtype=np.uint8)
img3 = np.ones((480,640),dtype=np.uint8)*255
img4 = np.full((480,640,3),(0,255,255),dtype=np.uint8)

# cv2.namedWindow('img1')
# cv2.imshow('img1',img1)
# cv2.waitKey()

img1 = cv2.imread('HappyFish.jpy')
img2 = img1
img3 = img1.copy()