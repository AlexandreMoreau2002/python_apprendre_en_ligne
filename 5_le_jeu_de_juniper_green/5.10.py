# Cadavres exquis

from random import choice


def jeu(sujet, verbe, adverbe, complement):
    s = choice(sujet)
    v = choice(verbe)
    a = choice(adverbe)
    c = choice(complement)
    return f"{s} {v} {a} {c}."


sujet = (
    "kevin",
    "la voisine",
    "abdel",
    "pierre",
    "paul",
    "jaques",
    "je",
    "le président",
)
verbe = ("mange", "essaye", "vole", "casse", "detruit", "nettoie", "range", "derobe")

adverbe = (
    "rapidement",
    "doucement",
    "clairement",
    "regulièrement",
    "heureusement",
    "sérieusement",
    "simplement",
    "parfaitement",
)
complement = (
    "dans le jardin",
    "la maison",
    "avec enthousiasme",
    "sous la pluie",
    "pendant la nuit",
    "au sommet de la colline",
    "derrière le bâtiment",
    "sans hésitation",
)


for _ in range(4):
    print(jeu(sujet, verbe, adverbe, complement))
