import pytesseract
import cv2

#set path of tesseract application
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#read image
image = cv2.imread("image\ocr_image2.png")
img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#reading and positioning of each image detected
results = pytesseract.image_to_data(img_RGB)
for id, line in enumerate(results.splitlines()):
    if id != 0:
# separate the results line by line
        line = line.split()
#only the word is detected
        if len(line) == 12:
#read the coordinate data and provide the location of boxes of detection
            x, y, w, h = int(line[6]), int(line[7]), int(line[8]), int(line[9])
            cv2.rectangle(image, (x, y), (w+x, h+y), (0, 255, 0), 2)
            cv2.putText(image,line[11],(x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

cv2.imshow("Input", image)
cv2.waitKey(0)
