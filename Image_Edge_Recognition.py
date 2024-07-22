import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

image = cv.imread("CT_frente.jpg")

if image is not None:
    print("image loaded succesfuly")

else:
    print("ERROR! Failed to load image!")
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
GB_image = cv.GaussianBlur(gray_image, (3,3), 0)
edges = cv.Canny(GB_image, 100,200)


# fig, ax = plt.subplots(ncols=2, figsize=(15,5))
# ax[0].imshow(image, cmap='gray')
# ax[0].set_title('Original Image in BW')
# ax[0].axis('off')
# ax[1].imshow(edges, cmap = 'gray')
# ax[1].set_title('Edge Image')
# ax[1].axis('off')
# #plt.subplot(121)
# plt.imshow(image,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# #plt.subplot(122)
# plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
 
if __name__ == "__main__":
    cv.imshow("Edge Detected Image", edges)
    # plt.show()
    #cv.imwrite('grayscaleimage.jpg', gray_image)
    cv.waitKey(0)
    cv.destroyAllWindows()