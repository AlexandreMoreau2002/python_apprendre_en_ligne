from random import randint


nmax = int(input("Nombre maximum ? : "))

for i in range(10):
    a = randint(2, nmax)
    b = randint(2, nmax)
    f = a * b
    print(a, " x ", b, " = ", end="")
    r = int(input())
    while r != f:
        print("Faux ! Ré-essayez !")
        print(a, "x", b, "= ", end="")
        r = int(input())
