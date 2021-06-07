from tkinter import *
from random import choice
from time import sleep

window = Tk()
window.title("Mister Erathia")
window.geometry('320x320')
window.columnconfigure(1, weight=1)

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
ivor = Hero("Ivor", "img\Hero_Ivor.png")
ryland = Hero("Ryland", "img\Hero_Ryland.png")
thorgrim = Hero("Thorgrim", "img\Hero_Thorgrim.png")
ufretin = Hero("Ufretin", "img\Hero_Ufretin.png")
gelu = Hero("Gelu", "img\Hero_Gelu.png")
aeris = Hero("Aeris", "img\Hero_Aeris.png")
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
calh  = Hero("Calh", "img\Hero_Calh.png")
ignatius = Hero("Ignatius", "img\Hero_Ignatius.png")
rashka = Hero("Rashka", "img\Hero_Rashka.png")
xeron = Hero("Xeron", "img\Hero_Xeron.png")
axsis = Hero("Axsis", "img\Hero_Axsis.png")
ayden = Hero("Ayden", "img\Hero_Ayden.png")
xarfax = Hero("Xarfax", "img\Hero_Xarfax.png")
xyron = Hero("Xyron", "img\Hero_Xyron.png")
zydar = Hero("Zydar", "img\Hero_Zydar.png")
clavius = Hero("Clavius", "img\Hero_Clavius.png")
galthran = Hero("Galthran", "img\Hero_Galthran.png")
moandor = Hero("Moandor", "img\Hero_Moandor.png")
straker = Hero("Straker", "img\Hero_Straker.png")
vokial = Hero("Vokial", "img\Hero_Vokial.png")
nagash = Hero("Nagash", "img\Hero_Nagash.png")
nimbus = Hero("Nimbus", "img\Hero_Nimbus.png")
sandro = Hero("Sandro", "img\Hero_Sandro.png")
thant = Hero("Thant", "img\Hero_Thant.png")
ajit = Hero("Ajit", "img\Hero_Ajit.png")
arlach = Hero("Arlach", "img\Hero_Arlach.png")
dace = Hero("Dace", "img\Hero_Dace.png")
damacon = Hero("Damacon", "img\Hero_Damacon.png")
gunnar = Hero("Gunnar", "img\Hero_Gunnar.png")
shakti = Hero("Shakti", "img\Hero_Shakti.png")
alamar = Hero("Alamar", "img\Hero_Alamar.png")
darkstorn = Hero("Darkstorn", "img\Hero_Darkstorn.png")
deemer = Hero("Deemer", "img\Hero_Deemer.png")
geon = Hero("Geon", "img\Hero_Geon.png")
jaegar = Hero("Jaegar", "img\Hero_Jaegar.png")
jeddite = Hero("Jeddite", "img\Hero_Jeddite.png")
malekith = Hero("Malekith", "img\Hero_Malekith.png")
crag_hack = Hero("Crag Hack", "img\Hero_Crag_Hack.png")
gurnisson = Hero("Gurnisson", "img\Hero_Gurnisson.png")
jabarkas = Hero("Jabarkas", "img\Hero_Jabarkas.png")
krellion = Hero("Krellion", "img\Hero_Krellion.png")
tyraxor = Hero("Tyraxor", "img\Hero_Tyraxor.png")
yog = Hero("Yog", "img\Hero_Yog.png")
boragus = Hero("Boragus", "img\Hero_Boragus.png")
kilgor = Hero("Kilgor", "img\Hero_Kilgor.png")
dessa = Hero("Dessa", "img\Hero_Dessa.png")
saurug = Hero("Saurug", "img\Hero_Saurug.png")
terek = Hero("Terek", "img\Hero_Terek.png")
vey = Hero("Vey", "img\Hero_Vey.png")
zubin = Hero("Zubin", "img\Hero_Zubin.png")
alkin = Hero("Alkin", "img\Hero_Alkin.png")
broghild = Hero("Broghild", "img\Hero_Broghild.png")
bron = Hero("Bron", "img\Hero_Bron.png")
drakon = Hero("Drakon", "img\Hero_Drakon.png")
gerwulf = Hero("Gerwulf", "img\Hero_Gerwulf.png")
korbac = Hero("Korbac", "img\Hero_Korbac.png")
tazar = Hero("Tazar", "img\Hero_Tazar.png")
wystan = Hero("Wystan", "img\Hero_Wystan.png")
erdamon = Hero("Erdamon", "img\Hero_Erdamon.png")
fiur = Hero("Fiur", "img\Hero_Fiur.png")
kalt = Hero("Kalt", "img\Hero_Kalt.png")
monere = Hero("Monere", "img\Hero_Monere.png")
aenain = Hero("Aenain", "img\Hero_Aenain.png")
gelare = Hero("Gelare", "img\Hero_Gelare.png")
grindan = Hero("Grindan", "img\Hero_Grindan.png")
inteus = Hero("Inteus", "img\Hero_Inteus.png")
lord_haart_death_knight = Hero("Lord Haart Death Knight", "img\Hero_Lord_Haart_Death_Knight.png")

heroes = [
    christian, edric, orrin, lord_haart, roland, sir_mullich, cuthbert, ingham, loynis, rion, clancy, ryland,
    thorgrim, ufretin, gelu, aeris, ivor, alagar, coronius, elleshar, malcom, uland, fafner, piquedram, thane,
    torosar, astral, halon, solmyr, theodorus, dracon, calh, ignatius, rashka, xeron, axsis, ayden, xarfax,
    xyron, zydar, clavius, galthran, moandor, straker, vokial, nagash, nimbus, sandro, thant, ajit, arlach,
    dace, damacon, gunnar, shakti, alamar, darkstorn, deemer, geon, jaegar, jeddite, malekith, crag_hack,
    gurnisson, jabarkas, krellion, tyraxor, yog, boragus, kilgor, dessa, saurug, terek, vey, zubin, alkin,
    broghild, bron, drakon, gerwulf, korbac, tazar, wystan, erdamon, fiur, kalt, monere, aenain, gelare,
    grindan, inteus, lord_haart_death_knight
]

heroes_indexes = list(range(0, len(heroes)))

unknown_img = PhotoImage(file="img\Hero_Christian.png")
unknown1_photo_label = Label(window, image=unknown_img)
unknown2_photo_label = Label(window, image=unknown_img)

title = Label(window, text="Mister Erathia", fg="deep pink", font=("arial", 28, "bold"))
undertitle = Label(window, text="Bitwa o Hełm Alabastrowego Jednorożca", fg="black", font=("arial", 11))
copyright = Label(window, text="©2021 Lulu_Quest", fg="grey", font=("arial", 8))
remaining_text = Label(window, text="Pozostało: " + str(len(heroes_indexes)) + "/" + str(len(heroes)), fg="black", font=("arial", 11))
versus_text = Label(window, text="VS", fg="red", font=("arial", 12))
message_box = Text(window, width=28, height=2, wrap=WORD, fg="black", font=("Courier New", 10))
button = Button(window, text="Wyznacz Pretendentów", bg="orange", fg="red", font=("Courier New", 14, "bold"), command=lambda:randomize())
message_box.config(state=DISABLED)

def write(string):
    message_box.config(state=NORMAL)
    message_box.insert("end", string)
    message_box.see("end")
    message_box.config(state=DISABLED)

def randomize():
    for hero in heroes:
        hero.photo_label.grid_forget()

    unknown1_photo_label.grid_forget()
    unknown2_photo_label.grid_forget()

    hero1_index = choice(heroes_indexes)
    heroes_indexes.remove(hero1_index)
    hero2_index = choice(heroes_indexes)
    heroes_indexes.remove(hero2_index)

    heroes[hero1_index].photo_label.grid(row=3, column=0, ipadx=42)
    heroes[hero2_index].photo_label.grid(row=3, column=2, ipadx=42)
    write("\n" + "\n" + heroes[hero1_index].name + " vs " + heroes[hero2_index].name)

    remaining_text = Label(window, text="Pozostało: " + str(len(heroes_indexes)) + "/" + str(len(heroes)), fg="black", font=("arial", 11))
    remaining_text.grid_forget()
    remaining_text.grid(row=6, columnspan=3)

title.grid(row=0, column=0, columnspan=3)
undertitle.grid(row=1, column=0, columnspan=3)
copyright.grid(row=2, column=0, columnspan=3)
unknown1_photo_label.grid(row=3, column=0, ipadx=42)
versus_text.grid(row=3, column=1)
unknown2_photo_label.grid(row=3, column=2, ipadx=42)
message_box.grid(row=4, column=0, columnspan=3, pady=20)
button.grid(row=5, column=0, columnspan=3)
remaining_text.grid(row=6, column=0, columnspan=3)
write("Welcome to Mister Erathia.")

window.mainloop()