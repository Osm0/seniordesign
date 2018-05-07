import cv2
import numpy as np
from scipy.stats import itemfreq

def read_color(im_name):
    print("Read Color")
    print(im_name)
    #print(str("crop_test/" + im_name))
    img = cv2.imread("crop_test/" + im_name)
    print(type(img))
    average_color = [img[:, :, i].mean() for i in range(img.shape[-1])]
    
    arr = np.float32(img)
    pixels = arr.reshape((-1, 3))

    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, centroids = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)

    palette = np.uint8(centroids)
    quantized = palette[labels.flatten()]
    quantized = quantized.reshape(img.shape)
    print(type(quantized))
    #cv2.imwrite("colortest.JPG", palette)
    

    dominant_color = palette[np.argmax(itemfreq(labels)[:, -1])]
    print(dominant_color)
    return dominant_color

#note the array comes out as [b,g,r] for some reason
#read_color("crop_test/roi2.png")

def read_preg_color(im_name):
    print("Preg Read Color")
    print(im_name)
    #print(str("crop_test/" + im_name))
    img = cv2.imread(im_name)

    average_color = [img[:, :, i].mean() for i in range(img.shape[-1])]
    
    arr = np.float32(img)
    pixels = arr.reshape((-1, 3))
    
    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, centroids = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    
    palette = np.uint8(centroids)
    quantized = palette[labels.flatten()]
    quantized = quantized.reshape(img.shape)
    print(type(quantized))
    #cv2.imwrite("colortest.JPG", palette)
    
    
    dominant_color = palette[np.argmax(itemfreq(labels)[:, -1])]
    print(dominant_color)
    return dominant_color
