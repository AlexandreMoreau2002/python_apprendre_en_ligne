from random import *

liste = []

for i in range(15):
    liste.append(randint(1, 10))

liste2 = []
for el in liste:
    if not el in liste2:
        liste2.append(el)

liste2.sort()

print(f"Liste initiale : {liste}")
print(f"Liste traité : {liste2}")
