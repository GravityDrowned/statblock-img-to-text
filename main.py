# convert an image to text
import pytesseract
from PIL import Image
# open the image and convert it to RGB
image = Image.open('./img/test.png').convert('RGB')
# apply OCR
text = pytesseract.image_to_string(image)
# print the recognized text
print(text)

