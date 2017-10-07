

import cv2
import numpy.core._methods
import numpy.lib.format


def resizeImage():
    img = cv2.imread(file_path.get())
    resized_img = cv2.resize(img, (int(height_value.get()), int(width_value.get())))
    cv2.imwrite("resized_img.jpg", resized_img)


#
# resized_img1 = cv2.resize(img1, (100, 100))
#
# cv2.imwrite("1.jpg", resized_img1)


from tkinter import *

window = Tk()

window.wm_title('Image Cutter')

l = Label(window, text="Image")
l.grid(row=0, column=0)

l1 = Label(window, text="Height")
l1.grid(row=1, column=0)

l2 = Label(window, text="Width")
l2.grid(row=2, column=0)

file_path = StringVar()
e = Entry(window, textvariable = file_path)
e.grid(row = 0, column = 1)


height_value = StringVar()
e1 = Entry(window, textvariable = height_value)
e1.grid(row = 1, column = 1)

width_value = StringVar()
e2 = Entry(window, textvariable = width_value)
e2.grid(row = 2, column = 1)


b6 = Button(window, text="Resize", width = 12, command=resizeImage)
b6.grid(row = 7, column = 3);




window.mainloop()
