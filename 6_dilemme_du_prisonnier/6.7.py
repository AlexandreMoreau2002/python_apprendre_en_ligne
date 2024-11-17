# dilemme du renvoi d'ascenseur


# cours 6.5, a detourner pour resoudre l'exercice ?
from random import choice

choix = ["T", "C"]  # T : trahit, C : coopère


def gain(lui, moi):
    if lui == "C" and moi == "C":
        return 3
    elif lui == "C" and moi == "T":
        return 8
    elif lui == "T" and moi == "C":
        return 0
    elif lui == "T" and moi == "T":
        return 1


# Toujours seul
# ne coopère jamais
def toujours_seul(liste_lui, liste_moi):
    return "T"


# Bonne poire
# coopère toujours
def bonne_poire(liste_lui, liste_moi):
    return "C"


# Aléatoire
# joue avec une probabilité égale 'T' ou 'C'
def aleatoire(liste_lui, liste_moi):
    global choix
    return choice(choix)


# Donnant donnant
# coopère seulement si l'autre joueur a coopéré au coup précédent.
def donnant_donnant(liste_lui, liste_moi):
    if len(liste_lui) > 0:
        return liste_lui[-1]
    else:  # premier coup
        return "C"


# Majorité
# coopère seulement si l'autre joueur a coopéré en majorité.
def majorite(liste_lui, liste_moi):
    if len(liste_lui) > 0:
        if liste_lui.count("C") > len(liste_lui) // 2:
            return "C"
        else:
            return "T"
    else:  # premier coup
        return "C"


# Une partie entre deux joueurs différents
liste = {}
score = {}
liste["Aléatoire"] = []
liste["Donnant donnant"] = []
for joueur in liste.keys():
    score[joueur] = 0
nb_coups = 0
while nb_coups < 10:  # à modifier
    coup_joueur1 = aleatoire(liste["Donnant donnant"], liste["Aléatoire"])
    coup_joueur2 = donnant_donnant(liste["Aléatoire"], liste["Donnant donnant"])
    liste["Aléatoire"].append(coup_joueur1)
    liste["Donnant donnant"].append(coup_joueur2)
    score["Aléatoire"] += gain(coup_joueur2, coup_joueur1)
    score["Donnant donnant"] += gain(coup_joueur1, coup_joueur2)
    nb_coups += 1
for joueur in liste.keys():
    print("Coups et score du joueur", joueur)
    print(liste[joueur])
    print(score[joueur])
    print()
