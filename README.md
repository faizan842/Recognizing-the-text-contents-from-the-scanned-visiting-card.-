
# Recognizing the text contents from a scanned visiting card.

The application which is used to recognize the text from scanned images,printeddocuments,receipt,visitingand business cards. The project involves the creation of real-time text recognition from a scanned document or image and then text is displayed on the screen using tesseract OCR engine.


# Introduction -
OCR = Optical Character Recognition. In other words, OCR systems transform a two-dimensional image of text that could contain machine printed or handwritten text from its image representation into machine-readable text. OCR as a process generally consists of several sub-processes to perform as accurately as possible.
## Features

- PreprocessingoftheImage 
- TextLocalization
- CharacterSegmentation
- CharacterRecognition
- PostProcessing

In OCR software, it’s main aim is to identify and capture all the unique
words using different languages from written text characters.
# Tesseract OCR -
Tesseract is an open source text recognition (OCR) Engine, available under the Apache 2.0 license. It can be used directly, or (for programmers) using an API to extract printed text from images. It supports a wide variety of languages.. It can be used with the existing layout analysis to recognize text within a large document, or it can be used in conjunction with an external text detector to recognize text from an image of a single text line.
#  Packages And Modules Used  
## Pytesseract -
Python-tesseract is an optical character recognition (OCR) tool for
python. That is, it will recognize and “read” the text from an image.
It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, including jpeg, png, gif, bmp, tiff, and others.

INSTALLATION (Python-tesseract requires Python 3.6+)
### Installation

Install my-project with npm

```bash
  pip install pytesseract
```
**Method used** -

**pytesseract.image_to_string()** -
Returns the result of a Tesseract OCR run on the provided image to string

**pytesseract.image_to_data()** -
Returns string containing box boundaries, confidences,and other information .
##  Opencv  -
OpenCV is an open-source library for computer vision, machine learning, and image processing.
It can process images and videos to identify objects, faces, or even the handwriting of a human.
When it is integrated with various libraries, such as Numpy which is a highly optimized library for numerical python, then the number of weapons increases in your Arsenal i.e whatever operations one can do in Numpy can be combined with OpenCV.
### Installation
Install my-project with npm

```bash
  pip install opencv-python
```
**Methods used** - 

**cv2.imread()**
The function imread loads an image from the specified file and returns it. If the image cannot be read (because of missing file, improper permissions, unsupported or invalid format), the function returns an empty matrix ( Mat::data==NULL )

**cv2.resize()**
The function resizes the image src down to or up to the specified size. note that the initial dst type or size are not taken into account. Instead, the size and type are derived from the `src`,`dsize`,`fx`, and `fy`.

**cv2.cvtcolor()**
The function converts an input image from one color space to another. In case of a transformation to-from RGB color space, the order of the channels should be specified explicitly (RGB or BGR). Note that the default color
format in OpenCV is often referred to as RGB but it is actually BGR (thebytes are reversed).

**cv2.thresh()** -
The function applies fixed-level thresholding to a multiple-channel array. The function is typically used to get a bi-level (binary) image out of a grayscale image ( compare could be also used for this purpose) or for removing a noise, that is, filtering out pixels with too small or too large
values.

**cv2.imshow()** -
The function imshow displays an image in the specified window. If the window was created with the cv::WINDOW_AUTOSIZE flag, the image is shown with its original size, however it is still limited by the screen resolution.Otherwise,theimageisscaledtofitthewindow.

**cv2.waitkey()**-
The function waitKey waits for a key event infinitely when it is 0 or for delay milliseconds, when it is positive. Since the OS has a minimum time between switching threads, the function will not wait exactly to delay ms, it will wait at least delay ms, depending on what else is running on your computer at that time.

cv2.rectangle() -
The function cv::rectangle draws a rectangle outline or a filled rectangle whose two opposite corners are pt1 and pt2.
# Conclusion -
It was a simple approach to process the image or scanned document and
extract the contents in the that, using pytesseract and openCV libraries.
We successfully performed the activity according to the given problem statement.
