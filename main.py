from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

print(pytesseract.image_to_string(Image.open('test_receipt.png')))