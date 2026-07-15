from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for item in question_data:
    question = Question(
        item["question"],
        item["correct_answer"]
    )
    question_bank.append(question)

quiz = QuizBrain(question_bank)

QuizInterface(quiz)