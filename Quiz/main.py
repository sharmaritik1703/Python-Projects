from random import choice, randint
import numpy as np

print("Welcome to Quiz!")
print("""
You will be asked some questions related to programming 
and your performance will be evaluated.

Each correct answer will add 4 marks and incorrect answer
will deduct 1 marks. If you want to skip enter skip and for
that there will be 0 marks.

""")

questions = ["Which programming language is fastest?",
             "Which programming language supports borrow checking?",
             "Tensorflow module is created by ?",
             "Which programming language is created by Microsoft?",
             "Which programming language is used by Unreal Engine?",
             "NumPy is created using which language?",
             "Which Python Framework is used in Back end development?",
             "Spring Boot is a popular framework of which language?",
             "Which programming language supports dynamic typing?"
             ]
answers = ["C", "Rust", "Google", "C#", "C++", "C", "Django", "Java", "Python"]

bank = {x: y for x, y in zip(questions, answers)}

score = 0
number_of_questions = randint(3, 6)
total = number_of_questions * 4

for n in range(number_of_questions):
    question = choice(questions)
    print(question)

    user_prompt = input("Enter the answer: ")

    if user_prompt == "skip":
        pass

    elif user_prompt == bank[question]:
        score += 4

    else:
        score -= 1

    questions.remove(question)

print(f"Your percentage is: {np.round(score/total, 2)*100}%")
