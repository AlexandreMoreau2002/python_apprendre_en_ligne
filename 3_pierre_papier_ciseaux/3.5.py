from random import *


def ecrire(nombre):
    if nombre == 1:
        print("pierre", end=" ")
    elif nombre == 2:
        print("papier", end=" ")
    else:
        print("ciseaux", end=" ")


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


def coup_ordi():
    # selon un sondage, un humain joue pierre 41%, papier 30%, ciseaux 29%
    # donc l'ordinateur va jouer papier 41%, ciseaux 30%, pierre 29%
    x = random()
    if x < 0.41:
        return 2
    elif x < 0.71:
        return 1
    else:
        return 3


ton_score, mon_score = 0, 0
fin = 5
manche = 0  # ajout perso en voyant la correction
print("Pierre-papier-ciseaux. Le premier à", fin, "a gagné !")
while mon_score < fin and ton_score < fin:
    ton_coup = int(input("1 : pierre, 2 : papier, 3 : ciseaux ? "))
    while ton_coup < 1 or ton_coup > 3:
        ton_coup = int(input("1 : pierre, 2 : papier, 3 : ciseaux ? "))
    print("Vous montrez", end=" ")
    ecrire(ton_coup)
    mon_coup = coup_ordi()
    print("- Je montre", end=" ")
    ecrire(mon_coup)
    print()  # aller à la ligne
    augmenter_scores(mon_coup, ton_coup)
    print("vous", ton_score, " moi", mon_score)
    manche += 1

if ton_score > mon_score:
    print("Tu as gagné bravo en ", manche, "manches")
else:
    print("J'ai gagné en", manche, "manches")

# # Test de la sortie de la fonction coup_ordi :
# pierre, papier, ciseaux = 0, 0, 0
# for _ in range(100):
#     x = coup_ordi()
#     if x == 1:
#         pierre += 1
#     elif x == 2:
#         papier += 1
#     elif x == 3:
#         ciseaux += 1
# print(pierre, ": pierre")
# print(papier, ": papier")
# print(ciseaux, ": ciseaux")
