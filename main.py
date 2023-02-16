import tkinter as tk
import tkinter.filedialog
from PIL import ImageTk, Image


def resize_img_for_display(img: Image):
    tmp = img.copy()
    tmp.thumbnail((2000, 2000))
    return tmp


def update_img_display():
    fp = tkinter.filedialog.askopenfilename(parent=frame, title="Choose your image to watermark")
    new_image = Image.open(fp)
    resized_new_img = resize_img_for_display(new_image)
    # create tk photo image for passing to Label
    photo_img = ImageTk.PhotoImage(resized_new_img)
    # update the label with new image
    img_display.configure(image=photo_img)
    img_display.image = photo_img  # for some reason I have to keep a reference to the new image


root = tk.Tk()
root.title("Image Watermarker")
root.geometry('1200x800')

frame = tk.Frame(root)
frame.grid(column=0, row=0)
frame.place(anchor='center')

# This creates the image the first time the program is run.
image = Image.open('./upload/samp.jpg')
resized_img = resize_img_for_display(image)
# create tk photo image for passing to Label
photo_image = ImageTk.PhotoImage(resized_img)
# create label using the image as the display
img_display = tk.Label(frame, image=photo_image)
img_display.grid(row=0, column=0)


button = tk.Button(frame, text="Upload", height=1, width=15, command=update_img_display)
button.grid(column=1, row=1)


# Start the event loop.
root.mainloop()
