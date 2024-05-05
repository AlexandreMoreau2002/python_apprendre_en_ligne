# Le jeu possède 4 règles :

# 1. Le Joueur 1 choisit un nombre entre 1 et Nmax
# 2. A tour de rôle, chaque joueur doit choisir un nombre parmi les multiples
#    ou les diviseurs du nombre choisi précédemment par son adversaire
#    et inférieur à Nmax.
# 3. Un nombre ne peut être joué qu'une seule fois.
# 4. Le premier nombre choisi doit être pair.

# Le perdant est le joueur qui ne trouve plus de multiples ou de diviseurs
# communs au nombre précédemment choisi.

from random import randint
from math import sqrt


def liste_premiers(n):
    # renvoie la liste des nombres premiers entre 3 et n
    premiers = []
    n += 1
    liste = [1] * n
    for i in range(2, int(sqrt(n) + 1)):
        for j in range(i * 2, n, i):
            liste[j] = 0
    for i in range(3, n):
        if liste[1] == 1:
            premiers.append(i)
    return premiers


def multiples(n):
    # renvoie la liste des multiples de n <= Nmax
    mult = []
    i = 2
    while i * n <= Nmax:
        if i * n in possibles:  # on l'ajoute seulement s'il n'a pas été joué
            mult.append(i * n)
        i += 1
    return mult


def diviseurs(n):
    # renvoie la liste des diviseurs de n
    div = []
    i = n
    while i >= 1:
        if n % i == 0 and n // i in possibles:  # on l'ajoute s'il n'a pas été joué
            div.append(n // i)
        i -= 1
    return div


def je_joue_premier():
    global possibles
    mon_nombre = 2 * randint(1, int(Nmax / 2))  # l'ordinateur choisit un nombre pair
    possibles.remove(
        mon_nombre
    )  # on enlèvera de la liste "possibles" tous les nombres joué
    print("Je choisis comme nombre de départ", mon_nombre)
    return mon_nombre


def je_joue(valides):
    global possibles, nombres_premiers
    print("Nombres valides :", valides)
    i = len(valides) - 1
    while (valides[i] not in nombre_premiers) and i > 0:
        i -= 1
    if valides[i] in nombre_premiers:
        print("Je choisis comme nombre", valides[i])
        possibles.remove(valides[i])
        return valides[i]
    if len(valides)>1:
        mon_nombre = valides[randint(1,len(valides)-1)]
    else:
        mon_nombre = valides[0]
    possibles.remove(mon_nombre)
    print("Je choisis comme nombre", mon_nombre)
    return mon_nombre


def il_joue(valides):
    global possibles
    print("Nombres valides :", valides)
    ton_nombre = int(input("Que jouez-vous ? "))
    while ton_nombre not in valides:
        ton_nombre = int(input("Incorrect. Que jouez-vous ? "))
    possibles.remove(ton_nombre)
    return ton_nombre


# ------------------ Programme principal -----------------------

Nmax = int(input("Entrez le nombre maximum (entre 20 et 100): "))
print("Jouons avec des nombres entre 1 et", Nmax)
possibles = list(range(1, Nmax + 1))  # liste des nombres pas encore joué
commence = input("Voulez-vous commencer (o/n) ? ")
valides = []
nombre_premiers = liste_premiers(Nmax)

# Début du jeu
# Condition spéciale : le premier nombre joué doit être pair.

if commence == "n":
    mon_nombre = je_joue_premier()
    valides = diviseurs(mon_nombre) + multiples(mon_nombre)
else:
    valides = [2] + multiples(2)
    ton_nombre = il_joue(valides)
    valides = diviseurs(ton_nombre) + multiples(ton_nombre)

# suite du jeu

while valides != []:
    if commence != "n":
        mon_nombre = je_joue(valides)
        valides = diviseurs(mon_nombre) + multiples(mon_nombre)
        if valides == []:
            print("Vous avez perdu!")
            break
    else:
        commence = ""
    ton_nombre = il_joue(valides)
    valides = diviseurs(ton_nombre) + multiples(ton_nombre)
    if valides == []:
        print("Bravo!")
