from random import random

ok = False
for x in range(5):
    nbr = random()
    if nbr < 0.01:
        print("Legend", end=" ")
        ok = True
    elif nbr < 0.05:
        print("Epic", end=" ")
        ok = True
    elif nbr < 0.28:
        print("Rare", end=" ")
        ok = True
    else:
        print("Commun", end=" ")

if not ok:
    print("paquet non valide, que des communes")
