import tkinter as tk
import tkinter.filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
# TODO: 1. Add ability to download watermarked images.
#       2. Fix sizing and display issues with image. Needs to be centered. Same with buttons.
#       3. Refactor functionality into classes. Main.py is confusing
#       4. Error handling for clicking 'cancel' on upload box


def resize_img_for_display(img: Image):
    tmp = img.copy()
    tmp.thumbnail((800, 800))
    return tmp


def update_img_display():
    fp = tkinter.filedialog.askopenfilename(parent=frame, title="Choose your image to watermark")
    image = Image.open(fp)
    width = image.width
    height = image.height

    x_coord = int(width * 0.5)
    y_coord = int(height * 0.5)

    watermark = Image.open("./upload/watermark.jpg").copy()
    watermark.thumbnail((600, 600))

    result = image.copy()
    result.paste(watermark, (x_coord, y_coord))

    resized_new_img = resize_img_for_display(result)
    # create tk photo image for passing to Label
    photo_img = ImageTk.PhotoImage(resized_new_img)
    # update the label with new image
    img_display.configure(image=photo_img)
    img_display.image = photo_img  # for some reason I have to keep a reference to the new image


win = tk.Tk()
win.title("Image Watermarker")
win.geometry('1200x800')

frame = tk.Frame(win)
frame.pack()

# This creates the image the first time the program is run.
image = Image.open('./upload/samp.jpg')
resized_img = resize_img_for_display(image)
# create tk photo image for passing to Label
photo_image = ImageTk.PhotoImage(resized_img)
# create label using the image as the display
img_display = tk.Label(frame, image=photo_image)
img_display.pack()


upload_btn = tk.Button(frame, text="Upload", height=1, width=15, command=update_img_display)
upload_btn.pack()

# watermark_btn = tk.Button(frame, text="Add watermark", height=1, width=15)
# watermark_btn.grid(row=2, column=0)

# Start the event loop.
win.mainloop()
