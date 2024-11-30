'''
geeks

'''
# Python program to explain cv2.erode() method 

# importing cv2 
import cv2 

# importing numpy 
import numpy as np 

# path 
path = '.venv/images/Images/baboon.jpg'

# Reading an image in default mode 
image = cv2.imread(path) 

# Window name in which image is displayed 
window_name = 'Image'

# Creating kernel 
kernel = np.ones((1, 1), np.uint8) 
imageCanny=cv2.Canny(image,3,100)
# Using cv2.erode() method 
imageErode = cv2.erode(imageCanny, kernel) 

# Displaying the image 
cv2.imshow('canny',imageCanny)
cv2.imshow(window_name, image) 
cv2.imshow('erode',imageErode)
cv2.waitKey(0)
