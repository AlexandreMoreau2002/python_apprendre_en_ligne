h = 0
while h < 24:
    m = 0

    while m < 60:
        s = 0

        while s < 60:
            print(h, "heure(s) ", m, "minute(s) ", s, "seconde(s)")
            s += 1
        m += 1
    h += 1
