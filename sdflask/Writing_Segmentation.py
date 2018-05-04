import cv2
import numpy as np
import imutils
from skimage.feature import hog
from sklearn import datasets


def get_contour_precedence(contour, cols):
    tolerance_factor = 500
    origin = cv2.boundingRect(contour)
    return ((origin[1] // tolerance_factor) * tolerance_factor) * cols + origin[0]



def seg(img):
    print("segm")
    im = cv2.imread(img)
    #print(im.shape)

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

    ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)

    #print("point5")
    #cv2.imwrite("point5.png", im_th)
    im_1b = cv2.bitwise_not(im_th)
    #cv2.imwrite("point55.png",im_1b)

    im2, ctrs, hier = cv2.findContours(im_1b.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #print("im2")
    #cv2.imwrite("first.png", im2)

    rects = [cv2.boundingRect(ctr) for ctr in ctrs]

    digitCnts=[]

    """
    for rect in rects:
        print(rect)
        if rect[2] >= 20 and (rect[3] >= 30 and rect[3] <= 150):
            digitCnts.append(rect)
    """

#for rect in rects:
        #print(rect[0])

    cnts = sorted(ctrs,key = lambda x:get_contour_precedence(x, im.shape[1]))
    print(type(ctrs[0]))
    #rects = sorted(rects,key = lambda x:x[0])

    boundingBoxes = [cv2.boundingRect(cnt) for cnt in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b:b[1][1], reverse=False))
    print("stuff{}".format(len(boundingBoxes)))

    """
    for i in range(len(cnts)):
        img = cv2.putText(im, str(i), cv2.boundingRect(cnts[i])[:2], cv2.FONT_HERSHEY_COMPLEX, 1, [125])
    cv2.imwrite('ordertest.png',img)
    """


    count = 0
    for rect in boundingBoxes:
        # Make the rectangular region around the digit
        leng = int(rect[3]*1)
        
        pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
        pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
        
        roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
        poi = im[pt1:pt1+leng, pt2:pt2+leng]
        count += 1
        #cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
        #cv2.imwrite('crop_test/roi' + str(count)+'.png', poi)
        #print(roi.shape[1])
        #print("roi a life well lived")
        
        if( poi.shape[1] > 12 and poi.shape[0] > 10): #if shape is large enough
            count += 1
            # Draw the rectangles
            #cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
            cv2.imwrite('crop_test/roi' + str(count)+'.png', poi)
        
            
        """
            print("x:{} , y:{} width: {}, height: {}".format(rect[0], rect[1], roi.shape[0], roi.shape[1]))
            
            # Resize the image
            resized_roi = imutils.resize(roi, width = 28, height = 28)
            #resized_roi = cv2.resize(roi, (28, 28), interpolation = cv2.INTER_CUBIC)
            if(resized_roi.shape != (28,28)):
                resized_roi = resized_roi = cv2.resize(roi, (28, 28), interpolation = cv2.INTER_CUBIC)
            resized_roi = cv2.dilate(resized_roi, (3, 3))
            resized_roi = cv2.bitwise_not(resized_roi)
            
            print("resized shape: {}".format(resized_roi.shape))
            resized_roi_hog = hog(resized_roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
            cv2.imwrite('test_letters3/img00'+str(count)+'.png',resized_roi)
            print(resized_roi.shape)
            print(roi.shape)
        """
        
        
        """
        roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
        roi = cv2.dilate(roi, (3, 3))
        """

    cv2.imwrite('img2.png', im)


if __name__ == '__main__':
    seg('colorcrop2.JPG')