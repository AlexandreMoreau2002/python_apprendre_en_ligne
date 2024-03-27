from random import randint

nbr_essais_max = 5

prenom = input("Quel est votre prénom ? ")
rejouer = "y"
nbr_reussites, nbr_parties, nbr_coups = 0, 0, 0

while rejouer != "n":
    nbr_essais = 1
    mon_nombre = randint(1, 30)
    ton_nombre = 0
    print("J'ai choisi un nombre entre 1 et", 30)
    print("A vous de le deviner en", nbr_essais_max, "tentatives au maximum !")

    while ton_nombre != mon_nombre and nbr_essais <= nbr_essais_max:
        print("Essai no ", nbr_essais)
        ton_nombre = int(input("Votre proposition : "))
        if ton_nombre < mon_nombre:
            print("Trop petit")
        elif ton_nombre > mon_nombre:
            print("Trop grand")
        else:
            print(
                "Bravo,",
                prenom,
                "! Vous avez trouvé",
                mon_nombre,
                "en",
                nbr_essais,
                "essai(s)",
            )
            nbr_reussites += 1
            nbr_coups += nbr_essais
        nbr_essais += 1

    if nbr_essais > nbr_essais_max and ton_nombre != mon_nombre:
        print("Désoler, vous avez utilisé vos", nbr_essais_max, "essais en vain.")
        print("J'avais choisi le nombre", mon_nombre, ".")

    nbr_parties += 1
    rejouer = input("Voulez-vous rejouer (y/n) ? ")
    print()

print("Pourcentage de réussite:", 100 * nbr_reussites / nbr_parties, "%")
print("Nombre moyen de tentatives:", nbr_coups / nbr_reussites)
