import cv2
import numpy as np
import os
from datetime import datetime as time

tstart = time.now()

imgpath = "C:\Users\Hiranya\Desktop/apples.png"
bright = "C:\Users\Hiranya\Desktop/brightapples.png"

img = cv2.imread(imgpath)
b1 = cv2.imread(bright)

cv2.imshow("Bright", b1)
cv2.imshow("Original Apples", img)

#resized the image to 50% to take lesser time processing and taking a copy of the image to display it later
#img = cv2.resize(img, (img.shape[1]/2,img.shape[0]/2))


# A black image
black_rgb = np.zeros((img.shape[0],img.shape[1], img.shape[2]))
black_bright = np.zeros((img.shape[0],img.shape[1], img.shape[2]))

#A list to store the coordinates of red pixels
center_hsv = []
center_bright = []

#Sums of coordinates of all the detected red pixels adn the number of red pixels detected
iSum = jSum = pix = 0
iBSum = jBSum = Bpix = 0
h, w, c = img.shape
#print w, h, c
iMin = h
iMax = 0
iBMin = h
iBMax = 0

for i in range (0, h):       #Iterating thru all pixels in the image
    for j in range (0, w):

        # Detecting Red pixels in normal image
        [b, g, r] = img[i][j]
        if ((150 <= r <= 255) and (0 <= g <= 50) and (0 <= b <=  50)):
            # print "found red at: ", i, j
            center_hsv.append([i, j])
            black_rgb[i][j] = [255, 255, 255]
            iSum += i
            jSum += j
            pix += 1
            if i < iMin:
                iMin = i
            if i > iMax:
                iMax = i

        # Detecting Red pixels in bright image
        [b, g, r] = b1[i][j]
        if ((200 <= r <= 255) and (0 <= g <= 120) and (0 <= b <=  120)):
            # print "found red at: ", i, j
            center_bright.append([i, j])
            black_bright[i][j] = [255, 255, 255]
            iBSum += i
            jBSum += j
            Bpix += 1
            if i < iBMin:
                iBMin = i
            if i > iBMax:
                iBMax = i

            #print "processing pixel: ", i, j
    print "percentage completed: ", (i+1)*100/img.shape[0], "%"

r = (iMax - iMin)/2
Br = (iBMax - iBMin)/2
print pix, Bpix, r, Br
#Average of all the detected red pixels approximates the location of center of the circle to be drawn
iAvg = iSum/pix
jAvg = jSum/pix
iBAvg = iBSum/Bpix
jBAvg = jBSum/Bpix

cv2.circle(black_rgb, (jAvg, iAvg), r, (0,255,0), 2)
cv2.circle(img, (jAvg, iAvg), r, (0,255,0), 2)

cv2.circle(black_bright, (jBAvg, iBAvg), Br, (0,0,255), 2)
cv2.circle(b1, (jBAvg, iBAvg), Br, (0,0,255), 2)

cv2.imshow("Circled red Apple", img)
cv2.imshow("Filtered and circled Binary Image", black_rgb)
cv2.imshow("Circled bright red Apple", b1)
cv2.imshow("Filtered and circled bright Binary Image", black_bright)

tend = time.now()
t = tend-tstart
print "Time taken = ", t, " seconds"

cv2.waitKey(0)
cv2.destroyAllWindows()

