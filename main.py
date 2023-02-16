import tkinter as tk
from PIL import ImageTk, Image


def resize_img_for_display(img: Image):
    tmp = img.copy()
    tmp.thumbnail((2000, 2000))
    return tmp


root = tk.Tk()
root.title("Image Watermarker")
root.geometry('1200x800')

frame = tk.Frame(root)
frame.grid(column=0, row=0)
frame.place(anchor='center')

image = Image.open('./upload/samp.jpg')
resized_img = resize_img_for_display(image)

photo_image = ImageTk.PhotoImage(resized_img)


img_display = tk.Label(frame, image=photo_image)
img_display.grid(row=0, column=0)


button = tk.Button(frame, text="Upload", height=1, width=15)
button.grid(column=1, row=1)

# Start the event loop.
root.mainloop()
