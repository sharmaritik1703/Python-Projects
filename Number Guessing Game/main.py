__author__ = "Ritik Sharma"
__email__ = "sharmaritik351@gmail.com"

from random import randint

random_number: int = randint(1, 10)
print("Welcome to Number Guessing Game")
print("You need to guess the generated number. The generated number is in range 1-10")

game_on = True
count = 0

while game_on:
    number = int(input("Enter the number: "))
    count += 1

    if count >= 3:
        print("You exceeded the number of attempts!")
        print(f"The original number was {random_number}")
        game_on = False

    else:
        if number == random_number:
            print(f"Great, you guessed it correct in {count} attempts!")
            game_on = False

        else:
            print("Try Again!")
