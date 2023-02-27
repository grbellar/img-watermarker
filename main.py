import tkinter as tk
import tkinter.filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
# TODO: 1. Add ability to download watermarked images.
#       2. Fix sizing and display issues with image. Needs to be centered. Same with buttons.
#       3. Refactor functionality into classes. Main.py is confusing


def resize_img_for_display(img: Image):
    tmp = img.copy()
    tmp.thumbnail((800, 800))
    return tmp


def update_img_display():
    fp = tkinter.filedialog.askopenfilename(parent=frame, title="Choose your image to watermark")
    new_image = Image.open(fp)

    draw = ImageDraw.Draw(new_image)
    text = "Grant Bellar"

    font = ImageFont.truetype('arial.ttf', 72)
    draw.text((3000, 3000), text=text, font=font)

    resized_new_img = resize_img_for_display(new_image)
    # create tk photo image for passing to Label
    photo_img = ImageTk.PhotoImage(resized_new_img)
    # update the label with new image
    img_display.configure(image=photo_img)
    img_display.image = photo_img  # for some reason I have to keep a reference to the new image


win = tk.Tk()
win.title("Image Watermarker")
win.geometry('1200x800')

frame = tk.Frame(win)
frame.grid(column=0, row=0)
# frame.place(anchor='center')

# This creates the image the first time the program is run.
image = Image.open('./upload/samp.jpg')
resized_img = resize_img_for_display(image)
# create tk photo image for passing to Label
photo_image = ImageTk.PhotoImage(resized_img)
# create label using the image as the display
img_display = tk.Label(frame, image=photo_image)
img_display.grid(row=0, column=0)


upload_btn = tk.Button(frame, text="Upload", height=1, width=15, command=update_img_display)
upload_btn.grid(row=1, column=0)

watermark_btn = tk.Button(frame, text="Add watermark", height=1, width=15)
watermark_btn.grid(row=2, column=0)

# Start the event loop.
win.mainloop()
