# Initialisation des coups des joueurs
historique = {"joueur": [], "adversaire": []}

# Stratégies
strategies = {
    "Always Cooperate": lambda h: "C",
    "Always Defect": lambda h: "D",
    "Tit for Tat": lambda h: "C" if not h["adversaire"] else h["adversaire"][-1],
    "Grudge": lambda h: "C" if "D" not in h["adversaire"] else "D",
}


def jouer_tour(historique, strategie):
    coup = strategie(historique)
    historique["joueur"].append(coup)
    return coup


# Fonction pour simuler un adversaire
def coup_adversaire(historique):
    return (
        "C"
        if not historique["joueur"]
        else ("D" if historique["joueur"][-1] == "D" else "C")
    )


# Simulation d'une partie
def jouer_partie(strategie_nom, tours=10):
    historique = {"joueur": [], "adversaire": []}
    strategie = strategies[strategie_nom]

    for _ in range(tours):
        coup_joueur = jouer_tour(historique, strategie)
        coup_adv = coup_adversaire(historique)
        historique["adversaire"].append(coup_adv)
        print(f"Tour {_+1}: Joueur - {coup_joueur}, Adversaire - {coup_adv}")

    return historique


# Tester les stratégies
print("Testing 'Always Cooperate' Strategy")
historique1 = jouer_partie("Always Cooperate")
print("\nTesting 'Always Defect' Strategy")
historique2 = jouer_partie("Always Defect")
print("\nTesting 'Tit for Tat' Strategy")
historique3 = jouer_partie("Tit for Tat")
print("\nTesting 'Grudge' Strategy")
historique4 = jouer_partie("Grudge")
