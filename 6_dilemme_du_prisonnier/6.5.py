# Créé par dmu, le 19.01.2023 en Python 3.7

def shadok2dix(nombre_shadok):
    # convertit un nombre shadok en decimal
    shadok2quatre = {"GA":0, "BU":1, "ZO":2, "MEU":3}
    long = len(nombre_shadok)
    somme = 0
    for i in range(long):
        somme += shadok2quatre[nombre_shadok[i]]*4**(long-i-1)
    return somme

def dix2shadok(nombre):
    # convertit un nombre decimal en nombre shadok
    quatre2shadok = {0:"GA", 1:"BU", 2:"ZO", 3:"MEU"}
    shadok = ""
    if nombre == 0:
        return "GA"
    while nombre != 0:
        chif = nombre%4
        shadok = quatre2shadok[chif] + " " + shadok
        nombre = nombre//4
    return shadok

shadok = ["MEU", "BU", "ZO", "ZO", "GA"]
print(shadok, ":", shadok2dix(shadok))
print()

for nombre in range(21):
    print(nombre, ":", dix2shadok(nombre))