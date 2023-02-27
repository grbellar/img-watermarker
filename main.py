import tkinter as tk
import tkinter.filedialog
from PIL import ImageTk, Image
# TODO: 1. Refactor functionality into classes. Main.py is confusing
#       2. Error handling for clicking 'cancel' on upload box
#       3. file save imrovements, default and allowed filetypes

global image_to_save


def resize_img_for_display(img: Image):
    tmp = img.copy()
    tmp.thumbnail((800, 800))
    return tmp


def update_img_display():
    global image_to_save

    fp = tkinter.filedialog.askopenfilename(parent=frame, title="Choose your image to watermark")
    image = Image.open(fp)
    width = image.width
    height = image.height

    x_coord = int(width * 0.8)  # aiming for bottom right corner of image
    y_coord = int(height * 0.8)

    watermark = Image.open("./upload/watermark.jpg").copy()
    watermark.thumbnail((600, 600))

    result = image.copy()
    result.paste(watermark, (x_coord, y_coord))
    image_to_save = result

    resized_new_img = resize_img_for_display(result)
    # create tk photo image for passing to Label
    photo_img = ImageTk.PhotoImage(resized_new_img)
    # update the label with new image
    img_display.configure(image=photo_img)
    img_display.image = photo_img  # for some reason I have to keep a reference to the new image


def save_image():
    file_path = tkinter.filedialog.asksaveasfile(initialfile="watermarked_image.jpg")
    image_to_save.save(file_path)


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


upload_btn = tk.Button(win, text="Upload", height=1, width=15, command=update_img_display)
upload_btn.pack()

download_btn = tk.Button(win, text="Download image", height=1, width=30, command=save_image)
download_btn.pack()


# Start the event loop.
win.mainloop()
