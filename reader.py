
import sys
import pytesseract as ocr
import numpy as np
import cv2 as cv

from PIL import Image


# configuration for windows pytesseract
ocr.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


def getText (imageFileName):
    # loading image
    image = Image.open(imageFileName)

    optimizedImage = optimizeImage(image)

    return ocr.image_to_string(optimizedImage, lang='por')


def optimizeImage (image):
    # channel RGB
    image = image.convert('RGB')

    # converting to an editable numpy array [x, y, channels]
    npImage = np.asarray(image).astype(np.uint8)  

    # decreasing noisy before binarization
    npImage[:, :, 0] = 0 # eliminating channel R (red)
    npImage[:, :, 2] = 0 # eliminating channel B (blue)

    # sets gray scale
    grayImage = cv.cvtColor(npImage, cv.COLOR_RGB2GRAY) 

    # Binary truncate for intensity
    # Pixels with color intensity below 127 will be converted to 0 (black)
    # Pixels with color intensity above 127 will be converted to 1 (white)    
    # THRESH_OTSU uses intelligent analysisof truncate levels
    ret, thresh = cv.threshold(grayImage, 127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    # Returns optimized image
    return Image.fromarray(thresh) 


def main (argv):
    imageFileName = argv[1]    
    print(getText(imageFileName))


if __name__ == "__main__":
    main(sys.argv)