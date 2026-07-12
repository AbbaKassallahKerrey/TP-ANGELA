from tkinter import *


timer = None

def start_timer():
    countdown(5 * 60)

def stop_timer():
    global timer
    if timer is not None:
        fenetre.after_cancel(timer)
        timer = None

def countdown(count):
    global timer

    minutes = count // 60
    secondes = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{secondes:02d}")

    if count > 0:
        timer = fenetre.after(1000, countdown, count - 1)
    else:
        canvas.itemconfig(timer_text, text="00:00")

fenetre = Tk()

fenetre.title("Ma première fenêtre")
fenetre.geometry("800x600")
fenetre.config(bg="lightblue")

label1 = Label(fenetre, text="Timer", font=("Arial", 30), fg="blue")
label1.place(x=330, y=20)

canvas = Canvas(fenetre, width=250, height=264)
photo = PhotoImage(file="tomato.png")

canvas.create_image(0, 0, image=photo, anchor=NW)

timer_text = canvas.create_text(
    125, 150,
    text="05:00",
    font=("Arial", 20),
    fill="blue"
)

canvas.place(x=275, y=100)

button1 = Button(
    fenetre,
    text="Start",
    font=("Arial", 20),
    bg="green",
    fg="white",
    command=start_timer
)
button1.place(x=100, y=400)

button2 = Button(
    fenetre,
    text="Stop",
    font=("Arial", 20),
    bg="red",
    fg="white",
    command=stop_timer
)
button2.place(x=600, y=400)

fenetre.mainloop()