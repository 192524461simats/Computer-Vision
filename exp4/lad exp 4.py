import cv2
import numpy as np
image = cv2.imread("C:/Users/MEGALADEVI/OneDrive/Pictures/Screenshots/Screenshot 2026-08-24 094507.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)
cv2.imshow("Original Grayscale Image", gray_image)
cv2.imshow("Histogram Equalized Image", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
