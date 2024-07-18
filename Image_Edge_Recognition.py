import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

image = cv.imread("knight_test.jpg")
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray_image, 100,200)

fig, ax = plt.subplots(ncols=2, figsize=(15,5))
ax[0].imshow(gray_image, cmap='gray')
ax[0].set_title('Original Image in BW')
ax[0].axis('off')
ax[1].imshow(edges, cmap = 'grey')
ax[1].set_title('Edge Image')
ax[1].axis('off')

if __name__ == "__main__":

    plt.show()