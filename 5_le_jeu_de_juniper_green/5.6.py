# Juniper Green solitaire

from random import randint


def multiples(n):
    # renvoie la liste des multiples de n <= Nmax
    mult = []
    i = 2
    while i * n <= Nmax:
        if i * n in possibles:
            mult.append(i * n)
        i += 1
    return mult


def diviseurs(n):
    # renvoie la liste des diviseurs de n
    div = []
    i = n
    while i >= 1:
        if n % i == 0 and n // i in possibles:
            div.append(n // i)
        i -= 1
    return div


Nmax = 50
nbr_parties = 100000
print("Je joue", nbr_parties, "parties avec des nombres entre 1 et", Nmax)
best = []
nbr_coup = 0
for i in range(nbr_parties):
    possibles = list(range(1, Nmax + 1))
    mon_nombre = possibles[randint(0, len(possibles) - 1)]
    possibles.remove(mon_nombre)
    partie = []
    partie.append(mon_nombre)
    valides = diviseurs(mon_nombre) + multiples(mon_nombre)
    while valides != []:
        mon_nombre = valides[randint(0, len(valides) - 1)]
        partie.append(mon_nombre)
        possibles.remove(mon_nombre)
        valides = diviseurs(mon_nombre) + multiples(mon_nombre)
    if len(partie) > len(best):
        best = partie[:]
    nbr_coup += len(partie)
print("Plus longue partie : ", len(best), "coups")
print(best)
print("Nombre moyen de coups par partie : ", int(nbr_coup / nbr_parties))
