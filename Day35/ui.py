from tkinter import Tk, Canvas, Label, Button, PhotoImage

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            self.window,
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 12, "bold")
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(
            self.window,
            width=300,
            height=250,
            bg="white",
            highlightthickness=0
        )

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 18, "italic")
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(
            self.window,
            image=self.true_image,
            highlightthickness=0,
            command=self.true_pressed
        )

        self.false_button = Button(
            self.window,
            image=self.false_image,
            highlightthickness=0,
            command=self.false_pressed
        )

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(
                self.question_text,
                text=question
            )
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"Quiz terminé !\n\nScore : {self.quiz.score}/{len(self.quiz.question_list)}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)