from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#81DDC6"

try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}
flip_timer = None


def next_card():
    global current_card, flip_timer

    if flip_timer is not None:
        fenetre.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_words, text=current_card["French"], fill="black")

    flip_timer = fenetre.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_words, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("words_to_learn.csv", index=False)
    next_card()


fenetre = Tk()
fenetre.title("Flash Cards")
fenetre.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")

card_background = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(
    400,
    150,
    text="Title",
    font=("Arial", 40, "italic")
)

card_words = canvas.create_text(
    400,
    263,
    text="Word",
    font=("Arial", 60, "bold")
)

canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(
    image=wrong_image,
    highlightthickness=0,
    borderwidth=0,
    command=next_card
)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="right.png")
right_button = Button(
    image=right_image,
    highlightthickness=0,
    borderwidth=0,
    command=is_known
)
right_button.grid(row=1, column=1)

next_card()

fenetre.mainloop()