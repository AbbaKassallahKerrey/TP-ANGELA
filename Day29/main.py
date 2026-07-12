from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = site_entry.get()
    nom_user = nom_user_entry.get()
    mdp = mdp_entry.get()
    is_ok =messagebox.askokcancel(title=site, message=f"These are the details entered: \nEmail: {nom_user} ")
    if is_ok:
        with open("data.txt", "a") as data_file:
                data_file.write(f"{site} | {nom_user} | {mdp}\n")
                site_entry.delete(0, END)
                nom_user_entry.delete(0, END)
                mdp_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
fenetre = Tk()
fenetre.title("La fenetre de mot de passe")
fenetre.config(padx=50, pady=50)
fenetre.geometry("800x600")
canvas=Canvas(fenetre, width=200, height=200)
image=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.pack()

site_label = Label(text="Website:",font=("Arial", 12, "bold"))
site_label.place(x=50, y=250)
site_entry = Entry(width=35, font=("Arial", 12, "bold"))
site_entry.place(x=200, y=250)
nom_user_label = Label(text="Email/Username:",font=("Arial", 12, "bold"))
nom_user_label.place(x=50, y=300)
nom_user_entry = Entry(width=35, font=("Arial", 12, "bold"))
nom_user_entry.place(x=200, y=300)
mdp_label = Label(text="Password:",font=("Arial", 12, "bold"))
mdp_label.place(x=50, y=350)
mdp_entry = Entry(width=21, font=("Arial", 12, "bold"))
mdp_entry.place(x=200, y=350)
button_gen = Button(text="Generate Password", font=("Arial", 12, "bold"),bg="green", fg="black")
button_gen.place(x=400, y=350)
button_add = Button(text="Add", font=("Arial", 12, "bold"),bg="blue", fg="black",command=save)
button_add.place(x=200, y=400)
fenetre.mainloop()