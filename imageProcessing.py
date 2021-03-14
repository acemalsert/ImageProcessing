"""
Title: CMPE 465 HW1
Author: Ahmet Cemal Sert
Student Number: 43999263780

"""
import cv2
import numpy as np

# The function that displays images with the given message
def showImage(image,message):
    cv2.imshow(message,image) 

# The function that reads given image and calls the showImage function to display it 
# Returns the image that has been read 
def readImage(image):
    image = cv2.imread("batman.jpg") 
    showImage(image,"Original Image")
    return image

# This function makes the given image a grayscale image
# Displays the grayscale image
# Returns grayscale image 
def makeImageGrayscale(image):     
    grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    showImage(grayScaleImage,"Gray Image") 
    return grayScaleImage

# This function resizes the given image with the parameters width and height  
# Displays the image
# Returns the resized image  
def resizeImage(width,height,grayScaleImage):
    dsize = (width,height) # sets the desired size 
    resizedImage = cv2.resize(grayScaleImage,dsize) 
    showImage(resizedImage,"Resized Image")
    return resizedImage

# This function adds random noise to given image 
# First creates noise with cv2.randn method and adds the noise to the image with cv2.add method
# Displays the image
# Returns the noisyImage 
def addRandomNoise(resizedImage):
    randomGaussianNoise = np.zeros((resizedImage.shape[0],resizedImage.shape[1]),dtype = np.uint8)
    cv2.randn(randomGaussianNoise,50,25)
    noisyImage = cv2.add(resizedImage,randomGaussianNoise) 
    showImage(noisyImage,"Noisy Image")
    return noisyImage

# Adds filter to the given image
# Blurs the given image using 3x3 filter
# Displays the filteredImage 
# Returns the filteredImage 
def addFilter(noisyImage):
    filteredImage = cv2.blur(noisyImage,(3,3)) 
    showImage(filteredImage,"Filtered Image") 
    return filteredImage

# Main function that calls all the other functions    
def main():
    image = readImage("batman.jpg")
    grayScaleImage = makeImageGrayscale(image)
    resizedImage = resizeImage(256,256,grayScaleImage)
    noisyImage = addRandomNoise(resizedImage)
    filteredImage = addFilter(noisyImage)

# Calls the function main   
main()    

cv2.waitKey(0) # Prevents the windows to close immediately
cv2.destroyAllWindows