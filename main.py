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

heroes = [christian, edric, orrin, lord_haart]

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