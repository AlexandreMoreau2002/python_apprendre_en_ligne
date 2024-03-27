"""
Variable local, global.
Trouver où est le problème
"""


# Programme 1
def truc():
    n = 10
    p = p + 1


n, p = 5, 20
truc()
print(n, p)

# truc() n'a pas accès a p et ne peut donc pas l'incrementé


# Programme 2
def truc():
    global p
    n = 10
    p = p + 1


n, p = 5, 20
truc()
print(n, p)

# truc() n'a toujours pas accès a n, il y a donc 2 n, un global et un local


# Programme 3
def truc():
    global n, p
    n = 10
    p = p + 1


n, p = 5, 20
truc()
print(n, p)

# n et p sont global, donc n = 10 et p = 21


# Programme 4
def truc(p):
    n = 10
    p = p + 1  # p = 21


n, p = 5, 20
truc(p)
print(n, p)

# truc() a accès a p mais étant immuable (int) il créer un autre p. n n'est pas accessible


# Programme 5
def truc(p):
    # global p # produit une erreur
    n = 10
    p = p + 1


n, p = 5, 20
truc(p)
print(n, p)

# erreur car un param ne peut pas etre une var globale


# Programme 6
def truc(p):
    global n
    n = 10
    p = p + 1


n, p = 5, 20
truc(p)
print(n, p)

# >>> 20 10, pas d'erreur mais toujours 2 variable p dont une local a 21


# Programme 7
def truc(n):
    global p
    n = 10
    p = p + 1


n, p = 5, 20
truc(p)
print(n, p)

# p étant global il a bien été incrémenté, par contre n étant immuable a été modifier localement
# >>> 5 21


# Programe 8
def truc(n):
    global p
    n = 10
    p = p + 1
    return n


n, p = 5, 20
n = truc(p)
print(n, p)

# Ici on a une fonction. n est modifié localement et la fonction retourne cette valeur qui sera stockée dans le n global.
# >>> 10 21
