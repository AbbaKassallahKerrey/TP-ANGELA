from tkinter import *
from tkinter import messagebox
import random
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a random password and insert it into the password entry."""
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!#$%&()*+"

    password_list = (
        random.choices(letters, k=8) +
        random.choices(numbers, k=2) +
        random.choices(symbols, k=2)
    )

    random.shuffle(password_list)
    password = "".join(password_list)

    mdp_entry.delete(0, END)
    mdp_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = site_entry.get()
    nom_user = nom_user_entry.get()
    mdp = mdp_entry.get()

    # Check for empty fields
    if len(site) == 0 or len(mdp) == 0:
        messagebox.showwarning(
            title="Oops",
            message="Please don't leave the Website or Password fields empty!"
        )
        return

    # Confirmation dialog
    is_ok = messagebox.askokcancel(
        title="Confirm",
        message=f"These are the details entered:\n\n"
                f"Website: {site}\n"
                f"Email/Username: {nom_user}\n"
                f"Password: {mdp}\n\n"
                f"Do you want to save them?"
    )

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{site} | {nom_user} | {mdp}\n")

        # Clear entries
        site_entry.delete(0, END)
        mdp_entry.delete(0, END)
        site_entry.focus()



fenetre = Tk()
fenetre.title("Password Manager")
fenetre.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
site_label = Label(text="Website:")
site_label.grid(column=0, row=1)

nom_user_label = Label(text="Email/Username:")
nom_user_label.grid(column=0, row=2)

mdp_label = Label(text="Password:")
mdp_label.grid(column=0, row=3)


site_entry = Entry(width=35)
site_entry.grid(column=1, row=1, columnspan=2)
site_entry.focus()

nom_user_entry = Entry(width=35)
nom_user_entry.grid(column=1, row=2, columnspan=2)
nom_user_entry.insert(0, "example@email.com")

mdp_entry = Entry(width=21)
mdp_entry.grid(column=1, row=3)


button_gen = Button(
    text="Generate Password",
    command=generate_password
)
button_gen.grid(column=2, row=3)

button_add = Button(
    text="Add",
    width=36,
    command=save
)
button_add.grid(column=1, row=4, columnspan=2)

fenetre.mainloop()