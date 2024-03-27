from random import randint
from time import time


nmax = int(input("Nombre maximum ? : "))
e = 0

for i in range(10):
    t0 = time()
    a = randint(2, nmax)
    b = randint(2, nmax)
    f = a * b
    print(a, " x ", b, " = ", end="")
    r = int(input())
    while r != f:
        print("Faux ! Ré-essayez !")
        print(a, "x", b, "= ", end="")
        r = int(input())
        e += 1

print("chrono : {:.2f}".format(time() - t0), "seconde")
print("vous avez reussi avec ", e, " erreur")
