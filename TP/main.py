from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Votre score final est : {quiz.score}/{len(question_bank)}")