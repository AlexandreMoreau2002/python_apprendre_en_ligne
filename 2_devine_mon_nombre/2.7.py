from random import randint


def forboucle():
    face, pile = 0, 0

    for _ in range(1000):
        if randint(0, 1) == 1:
            face += 1
        else:
            pile += 1

    print("pile = ", pile, "/ " "face = ", face)


def whileboucle():
    x = 0
    face, pile = 0, 0

    while x < 1000:
        if randint(0, 1) == 1:
            face += 1
        else:
            pile += 1
        x += 1
    print("pile = ", pile, "/ " "face = ", face)


forboucle(), whileboucle()
