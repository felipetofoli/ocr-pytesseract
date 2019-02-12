
import sys
import pytesseract as ocr
from PIL import Image


# configuration for windows pytesseract
ocr.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


def getText(imageFileName):
    return ocr.image_to_string(Image.open(imageFileName), lang='por')


def main (argv):
    imageFileName = argv[1]    
    print(getText(imageFileName))

if __name__ == "__main__":
    main(sys.argv)