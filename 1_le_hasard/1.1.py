from random import *


def jet(x, y, z):
    """
    Fonction qui simule un jet de dé avec la fonction randint du module random.
    Avec comme paramètre :
    - x pour le nombre de tir
    - y pour le nombre de dés
    - z pour le nombre de faces du dé
    """
    for _ in range(x):
        sum_dice = 0
        for _ in range(y):
            sum_dice += randint(1, z)
        print(sum_dice, end=" ")
    print()


jet(3, 3, 6)
print(" ")
jet(50, 3, 6)
print(" ")
jet(200, 2, 8)

print(jet.__doc__)

# exo modifié en ajoutant une docstring et en utilisant une fonction
