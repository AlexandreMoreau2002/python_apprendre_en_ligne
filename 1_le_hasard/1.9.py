from random import randint

for _ in range(100):
    rnd = randint(1, 4)
    if rnd == 1:
        print("d6 ", randint(1, 6))
    elif rnd == 2:
        print("d8 ", randint(1, 8))
    elif rnd == 3:
        print("d12", randint(1, 12))
    else:
        print("d20", randint(1, 20))
