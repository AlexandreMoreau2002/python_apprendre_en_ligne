from random import randint

def lancer_de(case):
    return case + randint(1,6)

def serpents_et_echelles(n):
    echelles = {1:38, 4:14, 9:31, 21:42, 28:84, 51:67, 71:91, 80:100}
    serpents = {98:79, 95:75, 93:73, 87:24, 64:60, 62:19, 54:34, 17:7}
    if n in echelles:
        n = echelles[n]
    elif n in serpents:
        n = serpents[n]
    return n

case = 0
nb_jets = 0
total = []
nb_parties = 1

while nb_parties <= 100000: # nombre de simulations
    while case < 100:
        case = serpents_et_echelles(lancer_de(case))
        nb_jets += 1

        if case > 100:  # on doit reculer
            case = serpents_et_echelles(100-(case-100))

        if case == 100:  # fin de la partie
            total.append(nb_jets)
            nb_parties += 1
            nb_jets = 0
            case = 0
            break

print("Nombre moyen de lancers :",sum(total)/len(total))