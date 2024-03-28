def option():
    print("'o' affichez les options")
    print("'c' convertir en °C")
    print("'f' convertir en °F")
    print("'q' pour quitter")


def to_fahrenheit(celsius):
    f = celsius * 9 / 5 + 32  # pour convertir °C en °F
    return f


def to_celsius(fahrenheit):
    c = (fahrenheit - 32) * 5 / 9  # pour convertir °F en °C
    return c


choix = "o"
while choix != "q":
    if choix == "c":
        temp = float(input("Temperature a convertir en °C : "))
        print(f"{temp:.0f} °F = {to_celsius(temp):.0f} °C")
        choix = "q"
    elif choix == "f":
        temp = float(input("Temperature a convertir en °F : "))
        print(f"{temp:.0f} °C = {to_fahrenheit(temp):.0f} °F")
        choix = "q"
    elif choix == "o":
        option()
    if choix != "q":
        choix = input("option : ")
