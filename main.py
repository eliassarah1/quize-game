from data import  question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for i in question_data:
    text = i['text']
    anwser = i['answer']
    new_q = Question(text,anwser)
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)

while quiz.still_has_q():
    quiz.next_question()