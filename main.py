import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from preprocessing import *
import random
import copy

# Determines the contours of the searched image
contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

OGcopy = copy.copy(loaded_image)

for i in range(len(contours)):
    color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    cv.drawContours(OGcopy, contours, i, color, 2)
    
if __name__ == "__main__":
  

    cv.imshow("Edge Detected Image", edges)
    # plt.show()
    #cv.imwrite('grayscaleimage.jpg', gray_image)
    cv.waitKey(0)
    cv.imshow("Drawed contours image", OGcopy)
    print(len(contours), "objects were found in this image file")

    #print("Image shape:", OGcopy.shape)

    for i, cont in enumerate(contours):
    #     print("Points on contour of object ", i, " ", cont)
        print("Area of object", i, ": ", cv.contourArea(cont), "pixels")
    cv.waitKey(0)
    cv.destroyAllWindows()