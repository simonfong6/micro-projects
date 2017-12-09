import cv2
from random import randint
from time import sleep
from sys import argv

image = cv2.imread('noise.png')
max_y, max_x, channels= image.shape
print(image.shape)
NOISE_POINTS = int(argv[1])

for i in range(NOISE_POINTS):
    temp = image[:,-1,:]
    image[:,1:,:] =  image[:,:-1,:]
    image[:,0,:] = temp
    cv2.imshow('noisy',image)
    cv2.waitKey(1)


