from pprint import pprint

dico = {
    "Computer": "Ordinateur",
    "Mouse": "Souris",
    "Keyboard": "Clavier",
    "Hard disk": "Disque dur",
    "Screen": "Ecran",
    "Printer": "Imprimante",
}

pprint(dico)


def inverser(dico):
    dico_inv = {}
    for cle, valeur in dico.items():
        dico_inv[valeur] = cle
    return dico_inv


print()
pprint(inverser(dico))

# Version un peu plus intéressante : 

dico2 = {
    "computer": "ordi",
    "mouse": "souris",
    "keyboard": "clavier",
}


def inverser():
    global dico2
    print(f"dico avant {dico2}")
    dico_inv2 = {}
    for cle, valeur in dico2.items():
        dico_inv2[valeur] = cle
    dico2 = dico_inv2
    print(f"dico apres {dico2}")


inverser()
inverser()
