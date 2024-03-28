from random import randint

nbr_essais_max = 5
nbr_essais = 1
play = "y"

while play == "y":

    ok = False
    while True:
        try:
            nbr = int(input("Choisi un nombre entre 1 et 5 : "))
            break
        except ValueError:
            print("vous devez entrer un nombre entre 1 et 5")
    input("Entrez 'Enter' pour commencer")
    ia_nbr = randint(1, 5)
    print(
        "1 si c'est plus grand, \n2 si c'est plus petit, \n0 si c'est la bonne reponse"
    )
    while not ok:
        while True:
            print("est ce que c'est : ", ia_nbr, "?")
            try:
                response = int(input("= "))
                break
            except ValueError:
                print("vous devez entrer un des choix suivant: 0 , 1, 2")
        if response == 1:  # si c'est plus grand
            ia_nbr += 1
        elif response == 2:  # si c'est plus petit
            ia_nbr -= 1
        elif response == 0:
            print("j'ai trouvé le bon nombre !")
            ok = True

    print()
    while True:
        try:
            play = input("Voulez-vous rejouer ? (y/n): ").lower()
            break
        except ValueError:
            print("vous devez entrer soit y (yes) soit n (no)")
