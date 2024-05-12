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
