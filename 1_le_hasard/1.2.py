from random import choice

liste = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
for x in range(100):
    print(choice(liste), end=" ")
