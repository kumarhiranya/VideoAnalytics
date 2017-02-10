import cv2
import numpy as np
from datetime import datetime as time

tstart = time.now()

imgpath = "C:\Users\Hiranya\Desktop/apples.png"
bright = "C:\Users\Hiranya\Desktop/brightapples.png"
img = cv2.imread(imgpath)
b1 = cv2.imread(bright)
cv2.imshow("Bright", b1)

#creating copies of the original image for creating HSV and GR swapped versions of the image
img_hsv = img.copy()
b2 = b1.copy()

cv2.imshow("Original Apples", img)

for i in range (0, img.shape[0]):       #Iterating thru all pixels in the image
    for j in range (0, img.shape[1]):

        # Calculating hsv for normal image
            [b, g, r] = img[i][j]

            #Filtering red based on RGB values
            ra = round(float(r) / 255, 3)
            ga = round(float(g) / 255, 3)
            ba = round(float(b) / 255, 3)

            # v value calculation
            cmax = max(ra, ga, ba)
            v = max(r, g, b)
            cmin = min(ra, ga, ba)
            delta = cmax - cmin
            # h value calculation
            if delta == 0:
                h = 0
            elif cmax == ra:
                h = 0.5*60 * (((ga - ba) / delta) % 6)
            elif cmax == ga:
                h = 0.5*60 * (((ba - ra) / delta) + 2)
            elif cmax == ba:
                h = 0.5*60 * (((ra - ga) / delta) + 4)

            # s value calculation
            if cmax == 0:
                s = 0
            else:
                s = 255*delta / cmax
            #img[i][j] = [h, s, v]
            img_hsv[i][j] = [v, s, h]


            # Calculating hsv for bright image
            [b, g, r] = b1[i][j]

            # Filtering red based on RGB values
            ra = round(float(r) / 255, 3)
            ga = round(float(g) / 255, 3)
            ba = round(float(b) / 255, 3)

            # v value calculation
            cmax = max(ra, ga, ba)
            v = max(r, g, b)
            cmin = min(ra, ga, ba)
            delta = cmax - cmin
            # h value calculation
            if delta == 0:
                h = 0
            elif cmax == ra:
                h = 0.5 * 60 * (((ga - ba) / delta) % 6)
            elif cmax == ga:
                h = 0.5 * 60 * (((ba - ra) / delta) + 2)
            elif cmax == ba:
                h = 0.5 * 60 * (((ra - ga) / delta) + 4)

            # s value calculation
            if cmax == 0:
                s = 0
            else:
                s = 255 * delta / cmax
            # img[i][j] = [h, s, v]
            b2[i][j] = [v, s, h]

    #print "percentage completed: ", (i + 1) * 100 / img.shape[0], "%"


tend = time.now()
t = tend-tstart
print "Time taken = ", t, " seconds"

cv2.imshow("Bright HSV", b2)
cv2.imshow("HSV Apples", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

