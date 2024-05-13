# Fréquences de chaque lettre dans un texte

texte = "c etait a megara faubourg de carthage dans les jardins d hamilcar les soldats qu il avait commandes en sicile se donnaient un grand festin pour celebrer le jour anniversaire de la bataille d eryx et comme le maitre etait absent et qu ils se trouvaient nombreux ils mangeaient et ils buvaient en pleine liberte"
print(texte)
print()

dico = {}
for c in texte:
    dico[c] = dico.get(c, 0) + 1

liste = list(dico.items())
liste.sort()
for car, freq in liste:
    print(car, " :", end=" ")
    for i in range(freq):
        print("|", end="")
    print()
