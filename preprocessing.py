import cv2 as cv
import numpy as np
loaded_image = cv.imread("TestImages/two_apple.png")

# thresholds used in the canny filter
min_threshhold = 70
max_threshold = 90

def image_filter(image, min_threshold = 70, max_threshold = 90):
    # print type of image for debbuging
    #print(type(loaded_image))
    if loaded_image is not None:
        print("image loaded succesfuly")

    else:
        print("ERROR! Failed to load image!")

    #In order, passes the image through BW, Gaussian Blur and Canny filters
    gray_image = cv.cvtColor(loaded_image, cv.COLOR_BGR2GRAY)
    GB_image = cv.GaussianBlur(gray_image, (3,3), 0)
    edges = cv.Canny(GB_image, min_threshhold, max_threshold)

    # Dialates and perfects the exact points of the image. Guarantees that only the outer layer of the object will be counted
    kernel = np.ones((3,3))
    edges = cv.dilate(edges, kernel, iterations=1)
    edges = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel, iterations=2)

    return edges

edges = image_filter(loaded_image)