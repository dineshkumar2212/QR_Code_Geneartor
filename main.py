import tkinter as tk
import qrcode
from PIL import Image, ImageTk
import tkinter.filedialog as filedialog

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def display_qr_code():
    url = entry.get()
    if not url:
        label.config(text="Please enter a URL.")
        return
    try:
        img = generate_qr_code(url)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label.config(image=img, text="")
        label.image = img
    except Exception as e:
        label.config(text="Error generating QR code.")
        print(e)

def download_qr_code():
    url = entry.get()
    if not url:
        label.config(text="Please enter a URL.")
        return
    try:
        img = generate_qr_code(url)
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            img.save(file_path)
    except Exception as e:
        label.config(text="Error generating QR code.")
        print(e)

def refresh_qr_code():
    entry.delete(0, tk.END)
    label.config(image=None, text="")

root = tk.Tk()
root.title("QR Code Generator")

frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame)
entry.pack()

generate_button = tk.Button(frame, text="Generate QR Code", command=display_qr_code)
generate_button.pack(side="left")

download_button = tk.Button(frame, text="Download QR Code", command=download_qr_code)
download_button.pack(side="right")

refresh_button = tk.Button(frame, text="Refresh", command=refresh_qr_code)
refresh_button.pack(side="right")

label = tk.Label(root)
label.pack()

root.mainloop()
