import os
import cv2

image_names = os.listdir('.')

for image_name in image_names:
    if image_name.split('.')[-1] != 'jpg':
        continue
    image = cv2.imread(image_name)
    image = cv2.resize(image, (300,450))
    cv2.imwrite(image_name,image)
