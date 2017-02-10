import cv2
import numpy as np
from datetime import datetime as time

tstart = time.now()

imgpath = "C:\Users\Hiranya\Desktop/apples.png"
bright = "C:\Users\Hiranya\Desktop/brightapples.png"

img = cv2.imread(imgpath)
b1 = cv2.imread(bright)

cv2.imshow("Brightened image", b1)
cv2.imshow("Original Apples", img)
b2 = b1.copy()

#creating copies of the original image for creating HSV and GR swapped versions of the image
img_green2red = img.copy()


for i in range (0, img.shape[0]):       #Iterating thru all pixels in the image
    for j in range (0, img.shape[1]):
            [b, g, r] = img[i][j]
            img_green2red[i][j] = [b, r, g]

            [b, g, r] = b1[i][j]
            # Swapping R and G values
            b2[i][j] = [b, r, g]

    #print "percentage completed original: ", (i + 1) * 100 / img.shape[0], "%"


tend = time.now()
t = tend-tstart
print "Time taken = ", t, " seconds"

cv2.imshow("Brightened and swapped image", b2)
cv2.imshow("Green and Red swapped Apples", img_green2red)
cv2.waitKey(0)
cv2.destroyAllWindows()

