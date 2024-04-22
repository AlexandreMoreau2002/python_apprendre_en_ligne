# jeu pierre, papier, ciseaux, puis avec historique des coups
# l'ordinateur joue au hasard

# mon coup = ordinateur
# ton coup = joueur

from random import randint
from tkinter import *


def augmenter_scores(mon_coup, ton_coup):
    global mon_score, ton_score
    if mon_coup == 1 and ton_coup == 2:
        ton_score += 1
    elif mon_coup == 2 and ton_coup == 1:
        mon_score += 1
    elif mon_coup == 1 and ton_coup == 3:
        mon_score += 1
    elif mon_coup == 3 and ton_coup == 1:
        ton_score += 1
    elif mon_coup == 3 and ton_coup == 2:
        mon_score += 1
    elif mon_coup == 2 and ton_coup == 3:
        ton_score += 1
    elif mon_coup == 4 and ton_coup == 1:
        mon_score += 1
    elif mon_coup == 4 and ton_coup == 2:
        mon_score += 1
    elif mon_coup == 4 and ton_coup == 3:
        ton_score += 1


def quel_objet(coup):
    if coup == 1:
        objet = pierre
        objet_p = pierre_p
    elif coup == 2:
        objet = papier
        objet_p = papier_p
    elif coup == 3:
        objet = ciseaux
        objet_p = ciseaux_p
    elif coup == 4:
        objet = puit
        objet_p = puit
    return objet, objet_p


def jouer(ton_coup):
    global mon_score, ton_score, score1, score2, nbr_coups
    nbr_coups += 1
    if nbr_coups > 20:
        nbr_coups = 1
    mon_coup = randint(1, 4)
    augmenter_scores(mon_coup, ton_coup)
    score1.configure(text=str(ton_score))
    score2.configure(text=str(mon_score))
    objet, objet_p = quel_objet(mon_coup)
    lab3.configure(image=objet)
    lab = Label(historique, image=objet_p)
    lab.grid(row=1, column=nbr_coups)
    objet, objet_p = quel_objet(ton_coup)
    lab = Label(historique, image=objet_p)
    lab.grid(row=0, column=nbr_coups)


def jouer_pierre():
    jouer(1)
    lab1.configure(image=pierre)


def jouer_papier():
    jouer(2)
    lab1.configure(image=papier)


def jouer_ciseaux():
    jouer(3)
    lab1.configure(image=ciseaux)


def jouer_puis():
    jouer(4)
    lab1.configure(image=puit)


def init_historique():
    i = 1
    while i <= 20:
        lab = Label(historique, image=rien_p)
        lab.grid(row=0, column=i)
        lab = Label(historique, image=rien_p)
        lab.grid(row=1, column=i)
        i += 1


def reinit():
    global mon_score, ton_score, score1, score2, lab1, lab3, nbr_coups, texte1b, texte2b
    ton_score = 0
    mon_score = 0
    nbr_coups = 0
    score1.configure(text=str(ton_score))
    score2.configure(text=str(mon_score))
    lab1.configure(image=rien)
    lab3.configure(image=rien)
    init_historique()


# variables globales
ton_score = 0
mon_score = 0
nbr_coups = 0

# fenetres graphiques
fenetre = Tk()
fenetre.title("Pierre, papier, ciseaux")
historique = Toplevel()
historique.title("Partie en cours")

# images
rien = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/rien.gif"
)
versus = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/versus.gif"
)
pierre = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/pierre.gif"
)
papier = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/papier.gif"
)
ciseaux = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/ciseaux.gif"
)
puit = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/puit.gif"
)
rien_p = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/rien_p.gif"
)
pierre_p = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/pierre_p.gif"
)
papier_p = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/papier_p.gif"
)
ciseaux_p = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/ciseaux_p.gif"
)

# Label
texte1 = Label(fenetre, text="Humain :", font=("Helvetica", 16))
texte1.grid(row=0, column=0)
texte1b = Label(historique, text="Humain :", font=("Helvetica", 16))
texte1b.grid(row=0, column=0, sticky=W)

texte2 = Label(fenetre, text="Machine :", font=("Helvetica", 16))
texte2.grid(row=0, column=2)
texte2b = Label(historique, text="Machine :", font=("Helvetica", 16))
texte2b.grid(row=1, column=0, sticky=W)

texte3 = Label(fenetre, text="Pour jouer, cliquez sur une des icones ci-dessous.")
texte3.grid(row=3, columnspan=3, pady=5)

score1 = Label(fenetre, text="0", font=("Helvetica", 16))
score1.grid(row=1, column=0)

score2 = Label(fenetre, text="0", font=("Helvetica", 16))
score2.grid(row=1, column=2)

lab1 = Label(fenetre, image=rien)
lab1.grid(row=2, column=0)

lab2 = Label(fenetre, image=versus)
lab2.grid(row=2, column=1)

lab3 = Label(fenetre, image=rien)
lab3.grid(row=2, column=2)

# boutons
bouton1 = Button(fenetre, command=jouer_pierre)
bouton1.configure(image=pierre)
bouton1.grid(row=4, column=0)

bouton2 = Button(fenetre, command=jouer_papier)
bouton2.configure(image=papier)
bouton2.grid(row=4, column=1)

bouton3 = Button(fenetre, command=jouer_ciseaux)
bouton3.configure(image=ciseaux)
bouton3.grid(row=4, column=2)

# bouton puit
bouton4 = Button(fenetre, command=jouer_puis)
bouton4.configure(image=puit)
bouton4.grid(row=4, column=3)

bouton5 = Button(fenetre, text="Recommencer", command=reinit)
bouton5.grid(row=5, column=0, pady=10, sticky=E)

bouton5 = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton5.grid(row=5, column=2, pady=10, sticky=W)

# demarrage :
init_historique()
fenetre.mainloop()
