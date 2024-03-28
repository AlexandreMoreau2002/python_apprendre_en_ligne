from random import randint

a = randint(1, 10) + randint(1, 10) / 10
b = randint(1, 10) + randint(1, 10) / 10
c = randint(1, 10) + randint(1, 10) / 10

print(a, b, c)


def max_of(a, b, c):
    print("Renvoie le plus grand des 3 nombres")
    if a >= b and a >= c:
        print("a est le plus grand", end=" = ")
        return a
    elif b >= a and b >= c:
        print("b est le plus grand", end=" = ")
        return b
    else:
        print("c est le plus grand", end=" = ")
        return c


print(max_of(a, b, c))
