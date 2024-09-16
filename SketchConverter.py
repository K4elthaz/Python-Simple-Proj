from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
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
    window.geometry("500x500")
    
    c=Canvas(window,bg = "gray16",height=600, width= 600)
    filename = PhotoImage(file = "Thumbnail.jpg")
    background_label= Label(window , image=filename)
    background_label.place(x=0 , y= 0,relwidth= 1, relheight= 1)
    
    import_button = Button(text="Select Jpeg File",command=_import)
    import_button.pack()
    import_button.place(x = 50, y = 20)
    
    convert_button = Button(text="Convert",command=convert)
    convert_button.pack()
    convert_button.place(x = 50, y = 50)
    window.mainloop()
    

    
