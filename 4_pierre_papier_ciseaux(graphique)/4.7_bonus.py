from random import *
from tkinter import *

# création de la fenetre
fenetre = Tk()
fenetre.title("Le probleme de monty hall")

# les images
n1 = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/monty_hall/door_1.gif"
)
n2 = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/monty_hall/door_2.gif"
)
n3 = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/monty_hall/door_3.gif"
)
ship = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/monty_hall/door-ship.gif"
)
wax = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/monty_hall/door-wax.gif"
)
sheep = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/monty_hall/door-sheep.gif"
)
candy = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/monty_hall/door-candy.gif"
)
rice = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/monty_hall/door-rice.gif"
)

# variables de base
prize = [candy, rice, sheep, wax]
text = 'Cliquez sur "Nouvelle partie" pour commencer'
player_score = 0
game_number = 0
boat = choice([1, 2, 3])
porte = 0
clic = 0
var = 0
controller_value = 0
x = False


# Fonction principal
def jouer(porte_num):
    global porte, clic, player_score, game_number, controller_value, x
    clic += 1
    porte = porte_num
    if clic <= 2:
        message(porte)
    if clic == 1:
        open_other_door(porte)
    if clic == 2:
        controller(controller_value, porte)
        if x == False:
            open(porte)
            resultat(porte)
            score_label.config(text=ratio_win_game(player_score, game_number))
        else:
            clic -= 1
            x = False


def controller(controller_value, porte):
    global x
    if controller_value == 1 and porte == 1:
        stop()
        x = True
    if controller_value == 2 and porte == 2:
        stop()
        x = True
    if controller_value == 3 and porte == 3:
        stop()
        x = True


def stop():
    error_page = Toplevel()
    error_page.title("Erreur")

    error_label = Label(error_page, text="Cette porte est déjà ouverte!")
    error_label.pack()

    error_button = Button(
        error_page, text="Fermer la fenêtre", command=error_page.destroy
    )
    error_button.pack()


def generator_prize(boat):
    global alias1, alias2, alias3
    if boat == 1:
        alias1 = ship
        alias2 = choice(prize)
        alias3 = choice(prize)
    elif boat == 2:
        alias2 = ship
        alias1 = choice(prize)
        alias3 = choice(prize)
    elif boat == 3:
        alias3 = ship
        alias1 = choice(prize)
        alias2 = choice(prize)


def open(porte):
    global porte1, porte2, porte3, controller_value

    if porte == 1:
        porte1.configure(image=alias1)
        controller_value = 1
    elif porte == 2:
        porte2.configure(image=alias2)
        controller_value = 2
    elif porte == 3:
        porte3.configure(image=alias3)
        controller_value = 3


def open_other_door(porte):
    global boat, text, instruction, var
    if porte == 1 and boat == 2:
        open(3)
        var = 3
    elif porte == 1 and boat == 3:
        open(2)
        var = 2
    elif porte == 1 and boat == 1:
        var = choice([2, 3])
        open(var)

    elif porte == 2 and boat == 1:
        open(3)
        var = 3
    elif porte == 2 and boat == 3:
        open(1)
        var = 1
    elif porte == 2 and boat == 2:
        var = choice([1, 3])
        open(var)

    elif porte == 3 and boat == 1:
        open(2)
        var = 2
    elif porte == 3 and boat == 2:
        open(1)
        var = 1
    elif porte == 3 and boat == 3:
        var = choice([1, 2])
        open(var)

    text += f"\nVoyons ce qu'il y avait derrière la porte {var}.\nChoisissez maintenant votre porte définitive!"
    instruction.configure(text=text)


def resultat(porte):
    global player_score, game_number, text, instruction
    if porte == boat:
        text += "\nBravo, vous avez gagné le voyage!"
        instruction.configure(text=text)
        player_score += 1
        game_number += 1
    else:
        text += "\nDommage, vous avez fait le mauvais choix!"
        instruction.configure(text=text)
        game_number += 1
    for x in range(3):
        open(x)


def message(porte):
    global text, instruction
    text += f"\nVous avez choisi la porte {porte}"
    instruction.configure(text=text)


def ratio_win_game(player_score, game_number):
    return f"parties gagné: {player_score} / {game_number}"


def init():
    global text, porte, clic, boat, controller_value, var, x
    text = "Choisissez une porte!"
    instruction.configure(text=text)
    porte = 0
    clic = 0
    var = 0
    boat = choice([1, 2, 3])
    x = False
    controller_value = 0


def new_game():
    global porte1, porte2, porte3
    init()
    generator_prize(boat)
    porte1 = Label(fenetre, image=n1)
    porte1.grid(row=0, column=0)

    porte2 = Label(fenetre, image=n2)
    porte2.grid(row=0, column=1)

    porte3 = Label(fenetre, image=n3)
    porte3.grid(row=0, column=2)

    bouton1.configure(state=NORMAL)
    bouton2.configure(state=NORMAL)
    bouton3.configure(state=NORMAL)


def reset():
    global player_score, game_number
    player_score = 0
    game_number = 0
    score_label.config(text=ratio_win_game(player_score, game_number))


# les portes par defaut
porte1 = Label(fenetre, image=n1)
porte1.grid(row=0, column=0)

porte2 = Label(fenetre, image=n2)
porte2.grid(row=0, column=1)

porte3 = Label(fenetre, image=n3)
porte3.grid(row=0, column=2)

# les boutons d'action du jeu
bouton1 = Button(fenetre, text="Porte 1", command=lambda: jouer(1), state=DISABLED)
bouton1.grid(row=1, column=0)
bouton2 = Button(fenetre, text="Porte 2", command=lambda: jouer(2), state=DISABLED)
bouton2.grid(row=1, column=1)
bouton3 = Button(fenetre, text="Porte 3", command=lambda: jouer(3), state=DISABLED)
bouton3.grid(row=1, column=2)

# Information de partie
instruction = Label(fenetre, text=text)
instruction.grid(row=2, column=0, columnspan=2)

# score des parties
score_label = Label(fenetre, text=ratio_win_game(player_score, game_number))
score_label.grid(row=2, column=2)

# container pour les boutons de controle du jeu
button_frame = Frame(fenetre)
button_frame.grid(row=4, column=0, columnspan=3)

# boutons de controle du jeu
bouton_new_game = Button(button_frame, text="Nouvelle partie", command=new_game)
bouton_new_game.pack(side=LEFT, padx=(10, 15))
bouton_reset = Button(button_frame, text="Remise à zéro", command=reset)
bouton_reset.pack(side=LEFT, padx=(15, 10))

generator_prize(boat)
print(f"le bateau est la porte suivante : {boat}")
fenetre.mainloop()
