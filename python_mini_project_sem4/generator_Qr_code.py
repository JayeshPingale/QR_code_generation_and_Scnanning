import tkinter as tk 
import qrcode
from PIL import Image,ImageTk
from tkinter import filedialog

def generate_qr():
    data=input_box.get()
    qr=qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img =qr.make_image(fill_colour="black",back_colur="white")
    img= img.resize((350,350),Image.ANTIALIAS)
    img= ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image=img


def save_qr():
    data=input_box.get()
    qr=qrcode.QRCode(version=1,box_size=10,border=5)
    
    qr.add_data(data)
    qr.make(fit=True)
    img =qr.make_image(fill_colour="black",back_colur="white")
    filepath =filedialog.asksaveasfilename(defaultextension="png")
    img.save(filepath)
    print("QR Code saved!!")


root=tk.Tk()
root.title("QR Code Generater")
root.geometry("450x550")

input_box = tk.Entry(root)
input_box.pack()

generate_button = tk.Button(root, text="Generate",command=generate_qr)
generate_button.pack()

save_button= tk.Button(root , text="Save",command=save_qr)
save_button.pack()


exit_button=tk.Button(root , text="Exit" , command=root.destroy)
exit_button.pack()

qr_label = tk.Label(root)
qr_label.pack()

root.mainloop()



