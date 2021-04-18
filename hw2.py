"""
Title: CMPE 465 HW2
Author: Ahmet Cemal Sert
"""

from cv2 import cv2 
import numpy as np


# The function that reads given image and calls the showImage function to display it 
# Returns the image that has been read 
def readImage(image):
    image = cv2.imread(image) 
    return image


# This function makes the given image a grayscale image
# Displays the grayscale image
# Returns grayscale image 
def makeImageGrayscale(image):     
    grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    return grayScaleImage


def applySobel(image):

        # Creates vertical and horizontal mask as described in the pdf using numpy
        sobelKernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobelKernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

        # Applies masks to the image horizontally and vertically 
        sobelGradient_x = cv2.filter2D(image, -1, sobelKernel_x)
        sobelGradient_y = cv2.filter2D(image, -1, sobelKernel_y)

        # Combines the image and masks using bitwise operator or 
        sobelApplied = cv2.bitwise_or(sobelGradient_x,sobelGradient_y)
        
    
        return sobelApplied
        

    
# Main function that calls all the other functions  
def main():

    # Reads images into variables
    cardinal1 = readImage("cardinal1.jpg")    
    cardinal2 = readImage("cardinal2.jpg")
    panda1 = readImage("panda1.jpg")
    panda2 = readImage("panda2.jpg")
    
    # Makes images grayscale and assigns into variables 
    grayScaleCardinal1 = makeImageGrayscale(cardinal1)
    grayScaleCardinal2 = makeImageGrayscale(cardinal2)
    grayScalePanda1 = makeImageGrayscale(panda1)
    grayScalePanda2 = makeImageGrayscale(panda2)

 
    sobelAppliedGrayScaleCardinal1 = applySobel(grayScaleCardinal1)
    cv2.imshow("Sobel Applied Cardinal1",grayScaleCardinal1)

   
    sobelAppliedGrayScaleCardinal2 = applySobel(grayScaleCardinal2)
    cv2.imshow("Sobel Applied Cardinal2",grayScaleCardinal2)

   
    sobelAppliedGrayScalePanda1 = applySobel(grayScalePanda1)
    cv2.imshow("Sobel Applied Panda1",grayScalePanda1)

   
    sobelAppliedGrayScalePanda2 = applySobel(grayScalePanda2)
    cv2.imshow("Sobel Applied Panda2",grayScalePanda2)

main()

cv2.waitKey(0) #Prevents the window to close immediately 
cv2.destroyAllWindows   
