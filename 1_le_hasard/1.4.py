from random import shuffle

liste = [
    "Wade Barrett",
    "Daniel Bryan",
    "Sin Cara",
    "John Cena",
    "Antonio Cesaro",
    "Brodus Clay",
    "Bo Dallas",
    "The Godfather",
    "Goldust",
    "Kane",
    "The Great Khali",
    "Chris Jericho",
    "Kofi Kingston",
    "Jinder Mahal",
    "Santino Marella",
    "Drew McIntyre",
    "The Miz",
    "Rey Mysterio",
    "Titus O'Neil",
    "Randy Orton",
    "David Otunga",
    "Cody Rhodes",
    "Ryback",
    "Zack Ryder",
    "Damien Sandow",
    "Heath Slater",
    "Sheamus",
    "Tensai",
    "Darren Young",
    "Dolph Ziggler",
]

shuffle(liste)
for i in range(30):
    print(i + 1, liste[i])
