from tkinter import *

counter = 0


def Incrementer():
    global counter
    counter += 1
    row1.configure(text=str(counter))


def Restart():
    global counter
    counter = 0
    row1.configure(text=str(counter))


fenetre = Tk()
fenetre.title("Bouton incrementeur")
fenetre.geometry("400x400")

row1 = Label(fenetre, text=counter, font=("Helvetica", 48))
row1.grid(row=0, column=0, rowspan=3)

bouton1 = Button(fenetre, text="Incrementer", command=Incrementer)
bouton1.grid(row=1, column=1, padx=10)
bouton2 = Button(fenetre, text="Recommencer", command=Restart)
bouton2.grid(row=2, column=1, padx=10)
bouton3 = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton3.grid(row=3, column=1, padx=10)

fenetre.mainloop()
