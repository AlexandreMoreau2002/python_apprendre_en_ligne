from random import randint

victoires_enfants = 0
victoires_corbeau = 0
nb_coups = 0
nb_parties = 10000

def maxi(liste):
    m=0
    j=0
    for i in range(len(liste)):
        if liste[i]>m:
            m=liste[i]
            j=i
    return j

for n in range(nb_parties):
    fruits = [10]*4
    nb_fruits = 40
    corbeau = 9
    while True:
        nb_coups += 1
        de = randint(0,5) # 0-3 : fruits, 4 : panier, 5 corbeau
        if de<5:
            if de == 4: # panier : on prend 2 fruits
                fruits[maxi(fruits)] -= 1   
                nb_fruits -= 1
                if nb_fruits>0:
                    fruits[maxi(fruits)] -= 1
                    nb_fruits -= 1
            elif fruits[de]>0: # il faut encore des fruits dans l'arbre...
                fruits[de] -= 1
                nb_fruits -= 1
        else:
            corbeau -= 1
        if nb_fruits == 0:
            victoires_enfants += 1
            break
        elif corbeau == 0:
            victoires_corbeau += 1
            break

print('Les enfants ont gagné',victoires_enfants*100/nb_parties,'% des parties')
print('Le corbeau a gagné',victoires_corbeau*100/nb_parties,'% des parties')
print('Nombre de coups moyen:',nb_coups/nb_parties)
        