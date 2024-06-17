# exercice créer par GPT4 pour exercer d'avantage les bases du dictionnaire en python

# exercice 9
personne = {
    "nom": "no-last-name",
    "prenom": "kevin",
    "age": 25,
    "sexe": "homme",
    "ville": "grenoble",
}

personne_copie = personne.copy()
personne_copie["prenom"] = "jane"

print(personne)
print(personne_copie)

# exercice 10
print(personne.get("sexe", "clé non trouvée"))

# exercice 11
notes = {"Alice": [14, 15, 17], "Bob": [9, 16, 14]}

notes["Alice"].append(8), notes["Bob"].append(12)
print(f'notes d\'Alice : {notes["Alice"]}', end="\n" f'notes de Bob : {notes["Bob"]}')
print()


def moyenne(personne):
    moyenne = sum(notes[personne]) / len(notes[personne])
    return moyenne


print(f'moyenne d\'Alice : {moyenne("Alice")}')
print(f'moyenne de Bob : {moyenne("Bob")}')

# exercice 12
fruits = {"pomme": 3, "orange": 2, "banane": 5, "kiwi": 1}

fruits_tries_par_cle = dict(sorted(fruits.items()))
print(fruits_tries_par_cle)

# exercice 13
fruits_tries_par_valeur = dict(sorted(fruits.items(), key=lambda item: item[1]))
print("fruit trier par valeur :", end="")
print(fruits_tries_par_valeur)

# exercice 14
dict1 = {
    "a": 1,
    "b": 2,
    "c": 3,
}
dict2 = {
    "c": 4,
    "d": 5,
    "e": 6,
}

dict_fusion = {}

for key in dict1:
    dict_fusion[key] = dict1[key]

for key in dict2:
    if key in dict_fusion:
        dict_fusion[key] += dict2[key]
    else:
        dict_fusion[key] = dict2[key]
print(dict_fusion)

combined_dict_unsorted = {
    key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)
}
combined_dict = dict(sorted(combined_dict_unsorted.items()))

# compréhension de dictionnaire
combined_dict = dict(
    sorted(
        {
            key: dict1.get(key, 0) + dict2.get(key, 0)
            for key in set(dict1) | set(dict2)
        }.items()
    )
)
print(combined_dict)

# exercice 15
from collections import defaultdict

d = defaultdict(list)
d["fruits"].append("orange")
d["fruits"].append("pomme")
d["legume"].append("carotte")

print(dict(d))

# exercice 16


def compter_occurences_mots(phrase):
    mots = phrase.split()
    compteur = {}
    for mot in mots:
        if mot in compteur:
            compteur[mot] += 1
        else:
            compteur[mot] = 1
    return dict(sorted(compteur.items(), key=lambda item: item[1]))


text = "le chat de la voisine est aussi le chien du postier"
print(compter_occurences_mots(text))
