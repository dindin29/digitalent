from tkinter import *
from PIL import Image, ImageTk
from random import randint


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

# pesan
pesan = Label(root, font=50, bg="#9b59b6", fg="white")
pesan.grid(row=3, column=2)

def updatePesan(x):
    pesan['text'] = x

# update user score


def updateNilaiUser():
    score = int(nilaiPemain["text"])
    score += 1
    nilaiPemain["text"] = str(score)

# update computer score


def updateNilaiKomp():
    score = int(nilaiKomp["text"])
    score += 1
    nilaiKomp["text"] = str(score)
#cek Pemenang


def cekPemenang(pemain, komp):
    if pemain == komp :
        updatePesan("SERIIII!!!!")
    elif pemain == "batu":
        if komp == "kertas":
            updatePesan("Kamu Kalah")
            updateNilaiKomp()
        else:
            updatePesan("Kamu Menang")
            updateNilaiUser()
    elif pemain == "paper":
        if komp == "gunting":
            updatePesan("Kamu Kalah")
            updateNilaiKomp()
        else:
            updatePesan("Kamu Menang")
            updateNilaiUser()
    elif pemain == "gunting":
        if komp == "batu":
            updatePesan("Kamu Kalah")
            updateNilaiKomp()
        else:
            updatePesan("Kamu Menang")
            updateNilaiUser()

    else:
        pass


#update pilihan
Jari = ["batu", "kertas", "gunting"]

def updateChoice(x):

    # komputer
    pilihanKomp = Jari[randint(0, 2)]
    if pilihanKomp == "batu":
        kompLabel.configure(image=batuGambarkomp)
    elif pilihanKomp == "kertas":
        kompLabel.configure(image=kertasGambarKomp)
    else:
        kompLabel.configure(image=guntingGambarKomp)


#pemain
    if x == "batu":
        userLabel.configure(image=batuGambar)
    elif x == "paper":
        userLabel.configure(image=kertasGambar)
    else:
        userLabel.configure(image=guntingGambar)

    cekPemenang(x, pilihanKomp)

# buttons
batu = Button(root, width=20, height=2, text="BATU", bg="#f0b7a4", fg="white", command=lambda: updateChoice("batu")).grid(row=2, column=1)
kertas = Button(root, width=20, height=2, text="KERTAS", bg="#b987cc", fg="white", command=lambda: updateChoice("kertas")).grid(row=2, column=2)
gunting = Button(root, width=20, height=2, text="GUNTING", bg="#b47136", fg="white", command=lambda: updateChoice("gunting")).grid(row=2, column=3)

root.mainloop()
