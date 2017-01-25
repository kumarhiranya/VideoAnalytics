import cv2
import numpy as np

imgpath = "C:\Users\Hiranya\Desktop/apples.png"


img = cv2.imread(imgpath)
#cv2.imshow("Original Apples", img)
img_hsv = img.copy()
img_green2red = img.copy()
cv2.imshow("Original Apples", img)

cv_bright_img = cv2.add(img, 50)
cv2.imshow("cv Bright Apples", cv_bright_img)

center = []

for i in range (0, img.shape[0]):       #Iterating thru all pixels in the image
    for j in range (0, img.shape[1]):
            [b, g, r] = img[i][j]
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

            if h in range(0,5):
                center.append([i,j])
            # s value calculation
            if cmax == 0:
                s = 0
            else:
                s = 255*delta / cmax
            #img[i][j] = [h, s, v]
            img_hsv[i][j] = [h, s, v]

            #swapping red and green colors
            img_green2red[i][j] = [b, r, g]

sumi = sumj = 0
for i, j in center:
    sumi += i
    sumj += j
c = (sumi/len(center), sumj/len(center))
cv2.circle(img, c, 150, (0,255,0), 2)
cv2.imshow("Circled red Apple", img)

print "Center: " ,c
cv2.imshow("HSV image", img_hsv)
cv2.imshow("Green and red swapped image", img_green2red)



cv2.waitKey(0)
cv2.destroyAllWindows()

#NOTES: OpenCV has different range of values for HSV, H ranges from 0-179, S from 0-255, V from 0-255
# Standard value ranges for HSV:- H from 1-360, S from 0.1-1, V from 0.1 to 1
#   Thus the formulae used have been normalized and adjusted for OpenCV