from random import *
from tkinter import *

fenetre = Tk()
fenetre.title("Pierre, Papier, Ciseaux")

# import des images
pierre = PhotoImage(file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/pierre.gif")
papier = PhotoImage(file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/papier.gif")
ciseaux = PhotoImage(file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/ciseaux.gif")

# generation random 
def random_generation(): 
    x = random()
    if x < 0.33:
        return pierre
    elif x < 0.66:
        return papier
    else:
        return ciseaux


# generation d'une ligne avec 10 images
for y in range (2):
    for z in range(10):
        photo = random_generation()
        lab = Label(fenetre, image=photo)
        lab.grid(row=y, column=z)
    
# demarrage :
fenetre.mainloop()
