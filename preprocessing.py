import cv2 as cv
import numpy as np
loaded_image = cv.imread("TestImages/two_apple.png")

# print type of image for debbuging
#print(type(loaded_image))
if loaded_image is not None:
    print("image loaded succesfuly")

else:
    print("ERROR! Failed to load image!")
gray_image = cv.cvtColor(loaded_image, cv.COLOR_BGR2GRAY)
GB_image = cv.GaussianBlur(gray_image, (3,3), 0)
edges = cv.Canny(GB_image, 70,90)

kernel = np.ones((3,3))
edges = cv.dilate(edges, kernel, iterations=1)
edges = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel, iterations=4)