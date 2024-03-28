def f(x):
    return 2 * x**3 - 3 * x - 1


def tabuler(f, borneInf, borneSup, pas):
    x = borneInf
    while x <= borneSup:
        print(x, "   ", f(x))
        x += pas


tabuler(f, -2.0, 2.0, 0.5)
