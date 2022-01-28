"""Importing OpenCV module,Pytesseract """
import cv2
import pytesseract
from pytesseract import Output

""""Tesseract engine path"""
pytesseract.pytesseract.tesseract_cmd=r"C:\\Users\\Acer\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

"""Reading image path amd resizing it for better accuracy"""
img = cv2.imread('D:\\Python_Project\\1.png')
img = cv2.resize(img, (1000,600))

"""Functions for preprocessing image"""

# get grayscale image
def get_grayscale(image):
    return  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# Preprocess image
gray = get_grayscale(img)
rn=remove_noise(gray)#optional
thresh = thresholding(gray)
canny = canny(gray)#optional

"""Showing Image Sample after preprocessing it and display its text conversion in console"""
custom_config = r'--oem 3 --psm 6'
cv2.imshow('||Original Image||',img)
cv2.waitKey(0)

print('-----------------------------------------')
print('TESSERACT OUTPUT --> ORIGINAL IMAGE')
print('-----------------------------------------')
print(pytesseract.image_to_string(img,config=custom_config))

cv2.imshow('||Thresholded Image||',thresh)
cv2.waitKey(0)

print('\n-----------------------------------------')
print('TESSERACT OUTPUT --> THRESHOLDED IMAGE')
print('-----------------------------------------')
print(pytesseract.image_to_string(thresh,config=custom_config))

cv2.imshow('||Gray Image||',gray)
cv2.waitKey(0)

print('\n-----------------------------------------')
print('TESSERACT OUTPUT --> GRAY IMAGE')
print('-----------------------------------------')
print(pytesseract.image_to_string(gray,config=custom_config))


"""Detecting Character's"""
d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())
n_boxes = len(d['text'])
for i in range(n_boxes):
    if float(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x+w,y+h), (0,0,255))

cv2.imshow('img', img)
cv2.waitKey(0)

