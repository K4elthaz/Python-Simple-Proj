from tkinter import *
from tkinter import filedialog
import cv2

def openFile():
    filepath = filedialog.askdirectory()
    file = open(filepath,'r')

    
window = Tk()
button = Button(text="Select Jpeg File",command=openFile)
button.pack()
window.mainloop()

image = cv2.imread("D:\Programming-Language\OpenCV\ca.jpg",1)
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert, (21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

cv2.imwrite("sketch.png", sketch)

cv2.imshow("Output Image", sketch)
cv2.imshow("Original Photo",image)
cv2.waitKey(0)
