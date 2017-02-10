import cv2
import numpy as np
from datetime import datetime as time

tstart = time.now()

def khue(i, j):
    hue = [img_hsv[i - 1][j - 1] ,
           img_hsv[i - 1][j],
           img_hsv[i - 1][j + 1] ,
           img_hsv[i][j - 1] ,
           img_hsv[i][j + 1] ,
           img_hsv[i + 1][j - 1],
           img_hsv[i + 1][j],
           img_hsv[i + 1][j + 1]]


    return hue


imgpath = "C:\Users\Hiranya\Desktop/apples.png"
bright = "C:\Users\Hiranya\Desktop/brightapples.png"
img = cv2.imread(imgpath)
b1 = cv2.imread(bright)

cv2.imshow("Bright", b1)
cv2.imshow("Original Apples", img)

# resized the image to 75% to fit all results to screen and taking a copy of the image to display it later
# img = cv2.resize(img, (img.shape[1]*3/4,img.shape[0]*3/4))
img_original = img.copy()

# creating copies of the original image for creating HSV and GR swapped versions of the image
img_hsv = img.copy()

# A black image
black_bright  = np.zeros((img_hsv.shape[0], img_hsv.shape[1], img_hsv.shape[2]))
black_hsv = np.zeros((img_hsv.shape[0], img_hsv.shape[1], img_hsv.shape[2]))

# A list to store the coordinates of red pixels
center_hsv = []
center_bright = []
height, w, c = img.shape

# Sums of coordinates of all the detected red pixels and the number of red pixels detected
iSum = jSum = pix = 0
iMin = height
iMax = 0
iBSum = jBSum = Bpix = 0
iBMin = height
iBMax = 0


for i in range(0, height):  # Iterating thru all pixels in the image
    for j in range(0, w):

        # Processing Normal image
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
        img_hsv[i][j] = [v, s, h]

        if (0 <= h <= 5 and 150 <= s <= 255 and 0 <= v <= 255):
            # print "found red at: ", i, j
            center_hsv.append([i, j])
            black_hsv[i][j] = [255, 255, 255]
            iSum += i
            jSum += j
            pix += 1
            if j < iMin:
                iMin = j
            if j > iMax:
                iMax = j

         # Processing Bright image
        [b, g, r] = b1[i][j]
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
        img_hsv[i][j] = [v, s, h]

        if (0 <= h <= 5 and 150 <= s <= 255 and 0 <= v <= 255):
            # print "found red at: ", i, j
            center_bright.append([i, j])
            black_bright[i][j] = [255, 255, 255]
            iBSum += i
            jBSum += j
            Bpix += 1
            if j < iBMin:
                iBMin = j
            if j > iBMax:
                iBMax = j


# Average of all the detected red pixels approximates the location of center of the circle to be drawn
iAvg = iSum / pix
jAvg = jSum / pix

iBAvg = iBSum / Bpix
jBAvg = jBSum / Bpix

print Bpix, pix
#radius = center x coordinate - left most red pixel's x coordinate
#r = (jAvg - iMin)
rB = (jBAvg - iBMin)
r = (iMax - iMin) / 2
# print iMin, iMax

cv2.circle(black_hsv, (jAvg, iAvg), r, (0, 255, 0), 2)
cv2.circle(img_original, (jAvg, iAvg), r, (0, 255, 0), 2)

cv2.circle(black_bright, (jBAvg, iBAvg), rB, (0, 0, 255), 2)
cv2.circle(b1, (jBAvg, iBAvg), rB, (0, 0, 255), 2)

cv2.imshow("Circled red Apple", img_original)
cv2.imshow("Filtered Binary Image", black_hsv)
#cv2.imshow("HSV Image", img_hsv)

cv2.imshow("Circled Bright red Apple", b1)
cv2.imshow("Filtered Bright Binary Image", black_bright)

tend = time.now()
t = tend-tstart
print "Time taken = ", t, " seconds"

cv2.waitKey(0)
cv2.destroyAllWindows()

