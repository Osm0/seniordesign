import cv2
import numpy as np
import imutils

img = cv2.imread('sdImages/IMG_0310.JPG')
#img = cv2.imread('sdImages/IMG_0310.JPG')
im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

edges = cv2.Canny(im_gray,40,50)
#cv2.dilate(edges, 2);

#ret, im_th = cv2.threshold(edges, 90, 255, cv2.THRESH_BINARY_INV)
im2, contours, h = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
area = 20

for cntr in contours:
    if cv2.contourArea(cntr) > area:
        im3 = cv2.drawContours(img, [cntr], 0, (0,255,0), 3)


"""
ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)
im2, contours,h = cv2.findContours(im_th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
"""

cv2.imwrite('imgray.png', im_gray)
cv2.imwrite('wha2t.png',im2)
cv2.imwrite('what3.png',im3)

"""
boundingBoxes = [cv2.boundingRect(cnt) for cnt in contours]
print(len(contours))


count = 0
for rect in boundingBoxes:
    leng = int(rect[3]*1.2)
        
    pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
    pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
    roi = edges[pt1:pt1+leng, pt2:pt2+leng]
    
    if( roi.shape[1] > 107 and roi.shape[0] > 107 and roi.shape[1] == roi.shape[0]):
        count += 1


        cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
        cv2.imwrite('trash/test' + str(count)+'.png', roi)



#resized_img = imutils.resize(img, width = 28, height = 28)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
"""

"""
ret, thresh = cv2.threshold(gray, 127, 255, 1)
contours,h = cv2.findContours(thresh,1,2)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print(len(approx))
    if len(approx)==5:
        print("pentagon")
        cv2.drawContours(img,[cnt],0,255,-1)
    elif len(approx)==3:
        print("triangle")
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print("square")
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    elif len(approx) == 9:
        print("half-circle")
        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
        print("circle")
        cv2.drawContours(img,[cnt],0,(0,255,255),-1)
        
"""

#cv2.imshow('img',img)