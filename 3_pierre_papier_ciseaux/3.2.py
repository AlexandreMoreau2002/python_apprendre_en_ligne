def table(n):
    i = 1
    while i < 12:
        print(n, "x", i, "=", n * i)
        i += 1


b = 1
while b < 12:
    print("table de", b)
    print()
    table(b)
    print()
    b += 1
