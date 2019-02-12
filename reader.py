
import pytesseract as ocr
from PIL import Image


# configuration for windows pytesseract
ocr.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


phrase = ocr.image_to_string(Image.open('images\\phrase.jpg'), lang='por')
print(phrase)