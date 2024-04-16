from tkinter import Tk, Label, Button

counter = 0


def incrementer():
    global counter
    counter += 1
    ligne1.configure(text=str(counter))


def restart():
    global counter
    counter = 0
    ligne1.configure(text=str(counter))


fenetre = Tk()
fenetre.title("Bouton incrementeur")
fenetre.geometry("400x400")

ligne1 = Label(fenetre, text=counter)
ligne1.grid(row=0, column=1,)

bouton1 = Button(fenetre, text="Incrementer", command=incrementer, width=6, height=2)
bouton1.grid(row=1, column=0)
bouton2 = Button(fenetre, text="Recommencer", command=restart, width=6, height=2)
bouton2.grid(row=1, column=1)
bouton3 = Button(fenetre, text="Quitter", command=fenetre.destroy, width=6, height=2)
bouton3.grid(row=1, column=2)

fenetre.mainloop()
