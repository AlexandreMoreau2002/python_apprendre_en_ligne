# simulation de resultat de lancer de dé au risk

print("Assaillant 1 dé, défenseur 1 dé")
a, d = 0, 0
i = 1  # counter
while i <= 6:
    y = 1  # counter
    while y <= 6:
        if i > y:
            d += 1
        else:
            a += 1
        y += 1
    i += 1
print("L'assaillant perd une armée {:.2f} %".format(100 * a / 6**2))
print("Le défenseur perd une armée {:.2f} %".format(100 * d / 6**2))

print()

print("Assaillant 2 dés, défenseur 1 dé")
a, d = 0, 0
i = 1
while i <= 6:
    j = 1
    while j <= 6:
        if i > j:
            k = i
        else:
            k = j
        y = 1
        while y <= 6:
            if k > y:
                d += 1
            else:
                a += 1
            y += 1
        j += 1
    i += 1
print("L'assaillant perd une armée {:.2f} %".format(100 * a / 6**3))
print("Le défenseur perd une armée {:.2f} %".format(100 * d / 6**3))
print()

print("Assaillant 3 dés, défenseur 1 dé")
a, d = 0, 0
i = 1
while i <= 6:
    j = 1
    while j <= 6:
        if i > j:
            l = i
        else:
            l = j
        k = 1
        while k <= 6:
            if k > l:
                l = k
            y = 1
            while y <= 6:
                if l > y:
                    d += 1
                else:
                    a += 1
                y += 1
            k += 1
        j += 1
    i += 1
print("L'assaillant perd une armée {:.2f} %".format(100 * a / 6**4))
print("Le défenseur perd une armée {:.2f} %".format(100 * d / 6**4))
print()

print("Assaillant 1 dé, dÃ©fenseur 2 dés")
a, d = 0, 0
i = 1
while i <= 6:
    x = 1
    while x <= 6:
        y = 1
        while y <= 6:
            if x > y:
                z = x
            else:
                z = y
            if i > z:
                d += 1
            else:
                a += 1
            y += 1
        x += 1
    i += 1
print("L'assaillant perd une armée {:.2f} %".format(100 * a / 6**3))
print("Le défenseur perd une armée {:.2f} %".format(100 * d / 6**3))
print()

print("Assaillant 2 dés, défenseur 2 dés")
a, d, e = 0, 0, 0
i = 1
while i <= 6:
    j = 1
    while j <= 6:
        if i > j:
            k = i  # meilleur dé de l'assalliant
            l = j
        else:
            k = j
            l = i
        x = 1
        while x <= 6:
            y = 1
            while y <= 6:
                if x > y:
                    t = x  # meilleur dé du défenseur
                    u = y
                else:
                    t = y
                    u = x
                if k > t and l > u:
                    d += 1
                elif t >= k and u >= l:
                    a += 1
                else:
                    e += 1
                y += 1
            x += 1
        j += 1
    i += 1
print("L'assaillant perd deux armées {:.2f} %".format(100 * a / 6**4))
print("Le défenseur perd deux armées {:.2f} %".format(100 * d / 6**4))
print("Chacun perd une armée {:.2f} %".format(100 * e / 6**4))
print()

print("Assaillant 3 dés, défenseur 2 dés")
a, d, e = 0, 0, 0
h = 1  # 1er dé
while h <= 6:
    i = 1  # 2ème dé
    while i <= 6:
        k, l = 0, 0
        if h > i:
            k = h  # meilleur dé
            l = i  # 2ème meilleur dé
        else:
            k = i
            l = h
        j = 1  # 3ème dé
        while j <= 6:
            m = k
            n = l
            if j >= m:  # j est le meilleur des 3 dés de l'assaillant
                n = m
                m = j
            elif j >= n:  # j est le 2ème meilleur dé
                n = j
            x = 1
            while x <= 6:
                y = 1
                while y <= 6:
                    if x > y:
                        t = x
                        u = y
                    else:
                        t = y
                        u = x
                    if m > t and n > u:
                        d += 1
                    elif t >= m and u >= n:
                        a += 1
                    else:
                        e += 1
                    y += 1
                x += 1
            j += 1
        i += 1
    h += 1
print("L'assaillant perd deux armées {:.2f} %".format(100 * a / 6**5))
print("Le défenseur perd deux armées {:.2f} %".format(100 * d / 6**5))
print("Chacun perd une armée {:.2f} %".format(100 * e / 6**5))
