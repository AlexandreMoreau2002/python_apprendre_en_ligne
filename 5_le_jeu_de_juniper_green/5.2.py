liste1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
liste2 = [
    "Janvier",
    "Février",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Aout",
    "Septembre",
    "Octobre",
    "Novembre",
    "Décembre",
]

i = 1
for mois in liste1:
    liste2[i:i] = [mois]  # l'element insere doit etre une liste
    i += 2

print(liste2)

liste2[4:4] = [29]

print(liste2)
