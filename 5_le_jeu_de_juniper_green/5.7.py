# combien de cartes pour remplir un album Panini ?

from random import randint

nb_cartes = 700
nb_essais = 100  # nombre d'expériences pour les statistiques
pourcentage = 0.5  # taux de remplissage
k_moyen = 0
for i in range(nb_essais):
    k = 0
    album = []
    while len(album) < pourcentage * nb_cartes:
        no = randint(1, nb_cartes)
        if no not in album:
            album.append(no)
        k += 1
    k_moyen += k

print(
    "Il a fallu",
    k_moyen / nb_essais,
    "cartes pour remplir à ",
    pourcentage * 100,
    "% un album de",
    nb_cartes,
    "cartes",
)
