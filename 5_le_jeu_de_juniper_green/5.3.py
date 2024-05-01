from math import sqrt

n = 1000
n += 1
liste = [True]*n

for i in range(2,int(sqrt(n))+1):
    if liste[i] :
        for j in range(i*2, n, i):
            liste[j] = False

premiers = []
for i in range(2,n):
    if liste[i] :
        premiers.append(i)

print(premiers)

