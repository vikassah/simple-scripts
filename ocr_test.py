from PIL import Image
import pytesseract
 
image_file = "./menu.jpg"
im = Image.open(image_file)
print (pytesseract.image_to_string(im))
