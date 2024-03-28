from random import randint
from time import time


nmax = int(input("Nombre maximum ? : "))
e = 0
t0 = time()

for i in range(1):
    a = randint(2, nmax)
    b = randint(2, nmax)
    op = randint(1, 4)
    if op == 1:
        texte = str(a) + " + " + str(b) + " = "
        f = a + b

    elif op == 2:
        if a < b:
            a, b = b, a
        texte = str(a) + " - " + str(b) + " = "
        f = a - b

    elif op == 3:
        texte = str(a) + " x " + str(b) + " = "
        f = a * b

    else:
        texte = str(a) + " / " + str(b) + " = "
        f = a / b

    print(texte, end="")

    r = int(input())

    # modifier la gestion de l'erreur aussi
    while r != f:
        e += 1
        print("Faux ! Ré-essayez !")
        print(texte, end="")
        r = int(input())

print("chrono : {:.2f}".format(time() - t0), "seconde")

if e == 1:
    print("vous avez reussi avec 1 erreur")
else:
    print("vous avez reussi avec ", e, " erreur")
