# table de multiplication de 53

# partie 1

i = 1
while i <= 20:
    print("{:2d}".format(i), "x 53 =", "{:4d}".format(53 * i))
    i += 1


# partie 2
x = 2
while x <= 12:
    print("table n°", x)
    print()
    i = 1
    while i <= 12:
        print("{:2d}".format(i), "x", x, " =", "{:4d}".format(x * i))
        i += 1
    x += 1
    print()
