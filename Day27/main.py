from tkinter import *

def calculer_conversion():
    nombre = float(input_field.get())
    resultat = nombre * 1.60934
    resultat_label.config(text=f"{nombre} miles = {resultat:.2f} kilomètres")

fenetre = Tk()

fenetre.title("Ma première fenêtre")
fenetre.geometry("800x600")
fenetre.config(bg="lightblue")

my_label = Label(fenetre, text="Bonjour, bienvenue dans ma première fenêtre !",
                 font=("Arial", 14), bg="lightblue")
my_label.pack()



Nom = Label(fenetre, text="Entrez Le nombre a convertir :",
            font=("Arial", 12), bg="lightblue")
Nom.pack()

input_field = Entry(fenetre, font=("Arial", 12), bg="white")
input_field.pack()
bouton = Button(fenetre, text="Convertir",
                font=("Arial", 12), bg="blue", fg="white",
                command=calculer_conversion)
bouton.pack()


resultat_label = Label(fenetre, text="", font=("Arial", 12), bg="lightblue")
resultat_label.pack()

fenetre.mainloop()