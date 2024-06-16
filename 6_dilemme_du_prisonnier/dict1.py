# exercice créer par GPT4 pour exercer d'avantage les bases du dictionnaire en python

personne = {
    "nom": "John",
    "age": 30,
    "ville": "Paris",
}

personne["ville"] = "Lyon"
personne["travail"] = "ingenieur"

# exo 4
del personne["age"]

print(personne)

# exo 5
for key, value in personne.items():
    print(f"{key} : {value}")

# exo 6
## méthode 1
print(personne)
error = "message d'erreur"
print(f' voici comment afficher la ville recherché : {personne.get("ville", error)}')

## méthode 2
if "nom" in personne:
    print('la clé "nom" existe')
else:
    print("la clé 'nom' n'existe pas")


# exo 7
dict_1 = {"a": 1, "b": 2}
dict_2 = {"c": 3, "d": 4}

dict_1.update(dict_2)
print(dict_1)


# exo 8
def count_occurrences(string):
    occurrences = {}
    for char in string:
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1
    return occurrences


string = str(input("quel mot ?"))
print(count_occurrences(string))
