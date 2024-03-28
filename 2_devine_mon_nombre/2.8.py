from random import randint

nb_paquets = int(input("combien de paquets voulez-vous ? : "))
nc, nr, ne, nl = 0, 0, 0, 0  # nombres de Communes, Rares, Epiques, Legendaires
for _ in range(nb_paquets):
    ok = False
    while not ok:  # créer un paquet valide
        nc_paquet, nl_paquet = 0, 0  # nombres de Communes et Legendaires dans un paquet
        for _ in range(5):
            if randint(1, 100) == 1:
                print("L", end=" ")
                nl_paquet += 1
                nl += 1
            elif randint(1, 100) <= 5:
                print("E", end=" ")
                ne += 1
            elif randint(1, 100) <= 28:
                print("R", end=" ")
                nr += 1
            else:
                print("C", end=" ")
                nc_paquet += 1
                nc += 1
        ok = nc_paquet < 5
        if not ok:
            nc -= 5
            print("non valide")
        elif nl_paquet > 0:
            print("!")
        else:
            print()
print()
print(nl, "légendaire(s):", "{:.2f}".format(100 * nl / (nb_paquets * 5)), "%")
print(ne, "épique(s):", "{:.2f}".format(100 * ne / (nb_paquets * 5)), "%")
print(nr, "rare(s):", "{:.2f}".format(100 * nr / (nb_paquets * 5)), "%")
print(nc, "communes:", "{:.2f}".format(100 * nc / (nb_paquets * 5)), "%")
