import cv2
import numpy as np

imgpath = "C:\Users\Hiranya\Desktop/apples.png"

img = cv2.imread(imgpath)
cv2.imshow("Original Apples", img)
img_green2red = img.copy()
cv2.imshow("Original Apples", img)




cv2.waitKey(0)
cv2.destroyAllWindows()

#NOTES: OpenCV has different range of values for HSV, H ranges from 0-179, S from 0-255, V from 0-255
# Standard value ranges for HSV:- H from 1-360, S from 0.1-1, V from 0.1 to 1
#   Thus the formulae used have been normalized and adjusted for OpenCV