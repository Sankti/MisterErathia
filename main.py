from tkinter import *
from random import randint

window = Tk()
window.title("KUBOMIZER")
window.geometry('270x420')



logo_img = PhotoImage(file="img\Hero_Christian.png")
logo_photo_label = Label(window, image=logo_img)
# professional_img = PhotoImage(file="img\profes.gif")
# professional_photo_label = Label(window, image=professional_img)
# inspired_img = PhotoImage(file="img\inspired.gif")
# inspired_photo_label = Label(window, image=inspired_img)
# enraged_img = PhotoImage(file="img\enraged.gif")
# enraged_photo_label = Label(window, image=enraged_img)
# jonah_img = PhotoImage(file="img\jonah.gif")
# jonah_photo_label = Label(window, image=jonah_img)

title = Label(window, text="Mister Erathia", fg="deep pink", font=("arial", 28, "bold"))
undertitle = Label(window, text="Bitwa o Hełm Alabastrowego Jednorożca", fg="black", font=("arial", 11))
copyright = Label(window, text="©2021 Lulu_Quest", fg="grey", font=("arial", 8))
versus_text = Label(window, text="VS", fg="red", font=("arial", 12))
message_box = Text(window, width=25, height=1, wrap=WORD, fg="black", font=("Courier New", 10))
button = Button(window, text="Wyznacz Pretendentów", bg="orange", fg="red", font=("Courier New", 14, "bold"), command=lambda:randomize())
message_box.config(state=DISABLED)

def write(string):
    message_box.config(state=NORMAL)
    message_box.insert("end", string)
    message_box.see("end")
    message_box.config(state=DISABLED)
	
# def randomize():
# 	logo_photo_label.grid_forget()
# 	professional_photo_label.grid_forget()
# 	inspired_photo_label.grid_forget()
# 	enraged_photo_label.grid_forget()
# 	jonah_photo_label.grid_forget()
# 	kuba_type = randint(1,4)
# 	if kuba_type == 1:
# 		write("\n" + "Kuba is professional.")
# 		professional_photo_label.grid(row=3, columnspan=3)
# 	elif kuba_type == 2:
# 		write("\n" + "Kuba is inspired.")
# 		inspired_photo_label.grid(row=3, columnspan=3)
# 	elif kuba_type == 3:
# 		write("\n" + "Kuba is enraged!")
# 		enraged_photo_label.grid(row=3, columnspan=3)
# 	elif kuba_type == 4:
# 		write("\n" + "Kuba is Jonah.")
# 		jonah_photo_label.grid(row=3, columnspan=3)
# 	else:
# 		write("Kuba is error.")

title.grid(row=0, columnspan=3)
undertitle.grid(row=1, columnspan=3)
copyright.grid(row=2, columnspan=3)
logo_photo_label.grid(row=3, column=1)
versus_text.grid(row=3, column=2)
message_box.grid(row=4, columnspan=3, pady=20)
button.grid(row=5, column=1)
write("Welcome to Kubomizer.")

window.mainloop()