# Substitution simple


def remplacer(chaine, table):
    for i in chaine:
        print(table[i], end="")
    print()


def inverser_table(table):
    table_inv = {}
    for cle, valeur in table.items():
        table_inv[valeur] = cle
    return table_inv


table_chiffrante = {
    "A": "W",
    "B": "B",
    "C": "H",
    "D": "A",
    "E": "Y",
    "F": "P",
    "G": "O",
    "H": "D",
    "I": "Q",
    "J": "Z",
    "K": "X",
    "L": "N",
    "M": "T",
    "N": "S",
    "O": "F",
    "P": "L",
    "Q": "R",
    "R": "U",
    "S": "V",
    "T": "M",
    "U": "C",
    "V": "E",
    "W": "K",
    "X": "J",
    "Y": "G",
    "Z": "I",
    " ": " ",
}

remplacer("RENARD", table_chiffrante)

table_dechiffrante = inverser_table(table_chiffrante)

remplacer("UYSWUA", table_dechiffrante)

remplacer("WUJ MWULYQW HWLQMFNQ LUFJQTW", table_dechiffrante)