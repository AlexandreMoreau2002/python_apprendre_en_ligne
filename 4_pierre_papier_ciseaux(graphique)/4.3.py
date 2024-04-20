from tkinter import *

fenetre = Tk()
fenetre.title("Pierre, Papier, Ciseaux")

pierre = PhotoImage(
    file="/Users/alex/Desktop/python_apprendre_en_ligne/4_pierre_papier_ciseaux(graphique)/assets/pierre.gif"
)

for i in range(10):
    lab = Label(fenetre, image=pierre)
    lab.grid(row=0, column=i)

# or with while
# i = 0
# while i < 10:
#     lab = Label(fenetre, image=pierre)
#     lab.grid(row=0, column=i)
#     i += 1

fenetre.mainloop()
