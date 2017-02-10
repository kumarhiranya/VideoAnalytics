import cv2
import numpy as np
from datetime import datetime as time

tstart = time.now()

imgpath = "C:\Users\Hiranya\Desktop/apples.png"
img = cv2.imread(imgpath)
#creating a copy of the original image
b1 = img.copy()

for i in range (0, img.shape[0]):       #Iterating thru all pixels in the image
    for j in range (0, img.shape[1]):
            [b, g, r] = img[i][j]
            b += 50
            g += 50
            r += 50
            if b >255:
                b=255
            if g >255:
                g=255
            if r >255:
                r=255
            b1[i][j] = [b, g, r]
    #print "percentage completed: ", (i + 1) * 100 / img.shape[0], "%"

cv2.imshow("Original Iamage", img)
cv2.imshow("Brightened Image", b1)
#cv2.imwrite("C:\Users\Hiranya\Desktop/brightapples.png", b1)

tend = time.now()
t = tend-tstart
print "Time taken = ", t, " seconds"


cv2.waitKey(0)
cv2.destroyAllWindows()

