# -*- coding: utf-8 -*-
"""day_17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RonqBJ7o0U4YnD2-jT6A3Nt82F-w4HIw
"""

question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
class Question:
    def __init__(self ,text,answer):
        self.text=text
        self.answer=answer
question_bank=[]
for i in question_data:
    text=i['text']
    answer=i['answer']
    question_bank.append(Question(text,answer))

question_bank[1].answer

class QuizBrain:

  def __init__(self,question_list):
    self.question_list=question_list
    self.question_no=0
    self.score=0
  def still_has_question(self):
    return self.question_no<len(self.question_list)


  def next_question(self):
    current=self.question_list[self.question_no].text
    user=input(f"Q.{self.question_no+1}:{current}(True/False)?:").lower()
    answer=self.question_list[self.question_no].answer
    self.question_no+=1
    self.check_answer(user,answer)
  def check_answer(self,user,answer):

    if user==answer.lower():
      print("you got it rigth")
      self.score+=1
    else:
      print("you are wrong")
    print(f"The correct aswer was: {answer}")
    print(f"your current score is {self.score}/{self.question_no}")

a=QuizBrain(question_bank)
while a.still_has_question():
  a.next_question()

