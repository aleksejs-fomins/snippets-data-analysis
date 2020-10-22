import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = mpimg.imread('../../../Pictures/testrec.png')
imgGray = rgb2gray(img)

imgGray -= 1

kernel = np.ones((10,10),np.float32)/100
imgGray = cv2.filter2D(imgGray,-1,kernel)

imgGray += 1
imgGray[imgGray < 0] = 0

# for i in range(50):
#     img = cv2.GaussianBlur(img,(5,5), 0)

#imgGray[imgGray<0.7] = 0

plt.axis('off')
plt.imshow(imgGray)
plt.show()