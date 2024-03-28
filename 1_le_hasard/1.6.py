from random import shuffle, sample

# Avec shuffle (donc on melange)
numbers = list(range(1, 91))
shuffle(numbers)
print(numbers)

# Avec sample (donc on tire au sort)
liste = list(range(1, 91))
print(sample(liste, 90))
