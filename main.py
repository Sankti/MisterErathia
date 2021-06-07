from tkinter import *
from random import choice
from time import sleep

window = Tk()
window.title("Mister Erathia")
window.geometry('320x420')

class Hero:
    def __init__(self, name, img):
        self.name = name
        self.img = PhotoImage(file=img)
        self.photo_label = Label(window, image=self.img)

christian = Hero("Christian", "img\Hero_Christian.png")
edric = Hero("Edric", "img\Hero_Edric.png")
orrin = Hero("Orrin", "img\Hero_Orrin.png")
lord_haart = Hero("Lord Haart", "img\Hero_Lord_Haart_Knight.png")
roland = Hero("Roland", "img\Hero_Roland.png")
sir_mullich = Hero("Sir Mullich", "img\Hero_Sir_Mullich.png")
cuthbert = Hero("Cuthbert", "img\Hero_Cuthbert.png")
ingham = Hero("Ingham", "img\Hero_Ingham.png")
loynis = Hero("Loynis", "img\Hero_Loynis.png")
rion = Hero("Rion", "img\Hero_Rion.png")
clancy = Hero("Clancy", "img\Hero_Clancy.png")
ryland = Hero("Ryland", "img\Hero_Ryland.png")
thorgrim = Hero("Thorgrim", "img\Hero_Thorgrim.png")
ufretin = Hero("Ufretin", "img\Hero_Ufretin.png")
gelu = Hero("Gelu", "img\Hero_Gelu.png")
aeris = Hero("Aeris", "img\Hero_Aeris.png")
ivor = Hero("Ivor", "img\Hero_Ivor.png")
alagar = Hero("Alagar", "img\Hero_Alagar.png")
coronius = Hero("Coronius", "img\Hero_Coronius.png")
elleshar = Hero("Elleshar", "img\Hero_Elleshar.png")
malcom = Hero("Malcom", "img\Hero_Malcom.png")
uland = Hero("Uland", "img\Hero_Uland.png")
fafner = Hero("Fafner", "img\Hero_Fafner.png")
piquedram = Hero("Piquedram", "img\Hero_Piquedram.png")
thane = Hero("Thane", "img\Hero_Thane.png")
torosar = Hero("Torosar", "img\Hero_Torosar.png")
astral = Hero("Astral", "img\Hero_Astral.png")
halon = Hero("Halon", "img\Hero_Halon.png")
solmyr = Hero("Solmyr", "img\Hero_Solmyr.png")
theodorus = Hero("Theodorus", "img\Hero_Theodorus.png")
dracon = Hero("Dracon", "img\Hero_Dracon.png")

heroes = [
        christian, edric, orrin, lord_haart, roland, sir_mullich, cuthbert, ingham, loynis, rion, clancy, ryland,
        thorgrim, ufretin, gelu, aeris, ivor, alagar, coronius, elleshar, malcom, uland, fafner, piquedram, thane,
        torosar, astral, halon, solmyr, theodorus, dracon
    ]

unknown_img = PhotoImage(file="img\Hero_Christian.png")
unknown1_photo_label = Label(window, image=unknown_img)
unknown2_photo_label = Label(window, image=unknown_img)

title = Label(window, text="Mister Erathia", fg="deep pink", font=("arial", 28, "bold"))
undertitle = Label(window, text="Bitwa o Hełm Alabastrowego Jednorożca", fg="black", font=("arial", 11))
copyright = Label(window, text="©2021 Lulu_Quest", fg="grey", font=("arial", 8))
versus_text = Label(window, text="VS", fg="red", font=("arial", 12))
message_box = Text(window, width=28, height=1, wrap=WORD, fg="black", font=("Courier New", 10))
button = Button(window, text="Wyznacz Pretendentów", bg="orange", fg="red", font=("Courier New", 14, "bold"), command=lambda:randomize())
message_box.config(state=DISABLED)

def write(string):
    message_box.config(state=NORMAL)
    message_box.insert("end", string)
    message_box.see("end")
    message_box.config(state=DISABLED)
	
heroes_indexes = list(range(0, len(heroes)))

def randomize():
    for hero in heroes:
        hero.photo_label.grid_forget()

    unknown1_photo_label.grid_forget()
    unknown2_photo_label.grid_forget()

    hero1_index = choice(heroes_indexes)
    heroes_indexes.remove(hero1_index)
    hero2_index = choice(heroes_indexes)
    heroes_indexes.remove(hero2_index)

    heroes[hero1_index].photo_label.grid(row=3, column=1)
    heroes[hero2_index].photo_label.grid(row=3, column=3)
    write("\n" + heroes[hero1_index].name + " vs " + heroes[hero2_index].name)

title.grid(row=0, columnspan=3)
undertitle.grid(row=1, columnspan=3)
copyright.grid(row=2, columnspan=3)
unknown1_photo_label.grid(row=3, column=1)
versus_text.grid(row=3, column=2)
unknown2_photo_label.grid(row=3, column=3)
message_box.grid(row=4, columnspan=3, pady=20)
button.grid(row=5, column=1)
write("Welcome to Mister Erathia.")

window.mainloop()