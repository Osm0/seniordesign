
#137 pixels wide
#815 pixels on the left
#984 pixels on the right
#crop 815 to (815+137)

#Up-down -> 374 - 374 + 1915

#each square is 130 px 50 px of white in between

import cv2
import numpy as np
import sys
from color import read_color, read_preg_color
from Writing_Segmentation import seg
from os import listdir, remove



def cutImage(image):
    print("in cutimage: {}".format(image))
    im = cv2.imread(image)
    cropped = im[374:2289,850:922]
    cv2.imwrite('man_cropped.JPG',cropped) #write cropped file to "man_cropped"
    
    
    img = cv2.imread('man_cropped.JPG') #read image from just newly written file (Yea pretty innefficient)
    print(type(img))
    boundaries = ([0,0,0],[230,230,230])
    lower = np.array([230,230,210])
    upper = np.array([255,255,255])

    mask = cv2.inRange(img,lower,upper)
    mask_inv = cv2.bitwise_not(mask)
    output = cv2.bitwise_and(img,img,mask = mask_inv)
    #cv2.imwrite('colorcrop.JPG', np.hstack([img,output]))
    cv2.imwrite('colorcrop2.JPG',output)

    seg('colorcrop2.JPG') #saves to crop_test
    files = listdir('./crop_test')
    
    colors = []
    for filename in files:
        if filename != '.DS_Store':
            colors.append(read_color(filename))
    print(colors)
    #rgbify
    for i in colors:
        temp = i[0]
        i[0] = i[2]
        i[2] = temp

    print(colors)
    return colors


#797 top, 84 length, 1504 left 17 wide
def cut_pregnancy(image):
    print("in pregnant cut: {}".format(image))
    im = cv2.imread(image)
    cropped = im[800:881,1515:1531]
    cv2.imwrite('preg_cut.JPG', cropped)
    
    color = read_preg_color('preg_cut.JPG')
    print(color[1])
    return color
    # if green is less than 200, then preggers


def delete_files(files):
    for filename in files:
        print("removing file: {}".format(filename))
        if filename != '.DS_Store':
            remove("crop_test/" + filename)

#def main():
    #image = cv2.imread('images2/IMG_0295.JPG')
    #cutImage(image)


#if __name__ == "__main__":
#   main()