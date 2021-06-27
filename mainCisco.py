from tkinter import *
from PIL import Image, ImageTk

#awal mainwindow
root = Tk()
root.title("Gunting Batu Kertas")
root.configure(background="#F0B7A4")

#gambar
batuGambar = ImageTk.PhotoImage(Image.open("batu_user.png"))
kertasGambar = ImageTk.PhotoImage(Image.open("katu_user.png"))
guntingGambar = ImageTk.PhotoImage(Image.open("gunting_user.png"))
batuGambarkomp = ImageTk.PhotoImage(Image.open("batu.png"))
kertasGambarKomp = ImageTk.PhotoImage(Image.open("kertas.png"))
guntingGambarKomp = ImageTk.PhotoImage(Image.open("gunting.png"))

# memasukkan gambar
userLabel = Label(root,image=guntingGambar, bg="86E3CE")
kompLabel = Label(root,image=guntingGambarKomp, bg="86E3CE")
kompLabel.grid(row=1, coloumn=0)
userLabel.grid(row=1, coloumn=4)

root.mainloop()
