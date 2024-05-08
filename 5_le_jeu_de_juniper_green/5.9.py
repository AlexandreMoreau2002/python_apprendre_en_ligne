from random import sample, randint
from tkinter import *

# numéros classés par colonnes
nos = [
    list(range(1, 10)),
    list(range(10, 20)),
    list(range(20, 30)),
    list(range(30, 40)),
    list(range(40, 50)),
    list(range(50, 60)),
    list(range(60, 70)),
    list(range(70, 80)),
    list(range(80, 91)),
]


def colonnes(nos):  # renvoie les 9 colonnes de la carte
    carte = []
    # On prend déja un numéro dans chaque colonne
    repartition = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    # puis on complète en prenant au max 2 nos par dizaines
    j = 0
    while j < 6:  # encore 6 nos à tirer
        k = randint(0, 8)  # tirage au sort d'une colonne
        while (repartition[k] == 3) or (repartition[k] == 2 and k < 8):
            k = randint(0, 8)
        repartition[k] += 1
        j += 1
    for i in range(9):
        carte.append(sample(nos[i], repartition[i]))
    return carte


def lignes(carte):  # tranforme les neuf colonnes de la cartes en trois lignes
    lignes = [
        [],
        [],
        [],
    ]  # la carte sera renvoyée sous la forme de 3 listes de 5 numéros
    for i in range(9):
        for j in range(len(carte[i])):
            k = min(len(lignes[0]), len(lignes[1]), len(lignes[2]))
            no_ligne = randint(0, 2)
            long = len(lignes[no_ligne])
            while long > k or (
                long > 0 and carte[i][j] // 10 == lignes[no_ligne][long - 1] // 10
            ):
                no_ligne = randint(0, 2)  # une ligne est tir au sort
                long = len(lignes[no_ligne])
            lignes[no_ligne].append(carte[i][j])
    return lignes


carte = colonnes(nos)
# print(carte)
carte = lignes(carte)
# print(carte)

# fenetre graphique
fenetre = Tk()
fenetre.title("Carte de loto")
fenetre.configure(background="white")
rien = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/5_le_jeu_de_juniper_green/assets/Rectangle.gif"
)
blanc = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/5_le_jeu_de_juniper_green/assets/Blanc.gif"
)

# dessine la carte
for l in range(3):  # initialise la carte en mettant des rectangles bleus partout
    for c in range(9):
        lab1 = Label(fenetre, image=rien)
        lab1.grid(row=l, column=c)
for l in range(3):
    for c in range(5):
        if carte[l][c] == 90:  # trouve la colonne où écrire le numéro
            colonne = 8
        else:
            colonne = carte[l][c] // 10
        lab1 = Label(fenetre, image=blanc)  # place un fond blanc
        lab1.grid(row=l, column=colonne)
        texte = Label(fenetre, text=str(carte[l][c]), font=("Helvetica", 20))
        texte.configure(background="white")
        texte.grid(row=l, column=colonne)  # écrit le numéro

fenetre.mainloop()
