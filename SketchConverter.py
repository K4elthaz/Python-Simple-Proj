from tkinter import *
from tkinter import filedialog
import cv2

image = None
sketch = None


def _import():
    global image, sketch
    image = cv2.imread(openFile(), 1)

def convert():
    global image, sketch  
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (21,21),0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

    cv2.imwrite("sketch.png", sketch)
    
    scale_percent = 60 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)  
    resized_sketch = cv2.resize(sketch, dim, interpolation = cv2.INTER_AREA) 
    
    cv2.imshow("Output Image", resized_sketch)
    cv2.imshow("Original Photo",resized_image)
    cv2.waitKey(0)

def openFile():
    filepath = filedialog.askopenfilename()
    return filepath


if __name__== "__main__":
    window = Tk()
    window.title("Image to Sketch")
    window.geometry("800x600")
    import_button = Button(text="Select Jpeg File",command=_import)
    import_button.pack()
    
    convert_button = Button(text="Convert",command=convert)
    convert_button.pack()
    window.mainloop()
    

    
