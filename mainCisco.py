from tkinter import *
from PIL import Image, ImageTk

#awal mainwindow
root = Tk()
root.title("Gunting Batu Kertas")
root.configure(background="#F0B7A4")

#gambar
batuGambar = ImageTk.PhotoImage(Image.open('batu_user.png'))
kertasGambar = ImageTk.PhotoImage(Image.open('kertas_user.png'))
guntingGambar = ImageTk.PhotoImage(Image.open('gunting_user.png'))
batuGambarkomp = ImageTk.PhotoImage(Image.open('batu.png'))
kertasGambarKomp = ImageTk.PhotoImage(Image.open('kertas.png'))
guntingGambarKomp = ImageTk.PhotoImage(Image.open('gunting.png'))

# memasukkan gambar
userLabel = Label(root,image=kertasGambar, bg="#F0B7A4")
kompLabel = Label(root,image=kertasGambarKomp, bg="#F0B7A4")
kompLabel.grid(row=1, column=0)
userLabel.grid(row=1, column=4)

#Nilai
nilaiPemain = Label(root, text=0, font=100, bg="#F0B7A4", fg="white")
nilaiKomp = Label(root, text=0, font=100, bg="#F0B7A4", fg="white")
nilaiKomp.grid(row=1, column=1)
nilaiPemain.grid(row=1, column=3)


# indicators
indikatorPemain= Label(root, font=50, text="PEMAIN", bg="#f18c8e", fg="white")
indikatorKomputer = Label(root, font=50, text="KOMPUTER", bg="#f18c8e", fg="white")
indikatorPemain.grid(row=0, column=3)
indikatorKomputer.grid(row=0, column=1)

# buttons
batu = Button(root, width=20, height=2, text="BATU", bg="#f0b7a4", fg="white", command=lambda: updateChoice("batu")).grid(row=2, column=1)
kertas = Button(root, width=20, height=2, text="KERTAS", bg="#b987cc", fg="white", command=lambda: updateChoice("kertas")).grid(row=2, column=2)
gunting = Button(root, width=20, height=2, text="GUNTING", bg="#b47136", fg="white", command=lambda: updateChoice("gunting")).grid(row=2, column=3)

root.mainloop()
