__author__ = "Ritik Sharma"
__email__ = "sharmaritik351@gmail.com"

from random import choice
from time import sleep

# Stone
stone = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

mapping: dict = {"stone": stone, "paper": paper, "scissor": scissors}

print("Welcome to Stone Paper Scissors Game")
sleep(0.1)

random_state = choice(["stone", "paper", "scissor"])
sleep(0.1)
user_state: str = input("Select one state (stone, paper, scissor): ")

sleep(0.1)
print(f"You Selected: {mapping[user_state]}")
sleep(0.1)
print(f"Computer Selected: {mapping[random_state]}")

if mapping[user_state] == mapping[random_state]:
    print("You have a tie!")

else:
    if user_state == "stone" and random_state == "scissor":
        print("You wins the game!")

    elif user_state == "paper" and random_state == "stone":
        print("You wins the game!")

    elif user_state == "scissor" and random_state == "paper":
        print("You wins the game!")

    else:
        print("Computer wins the game.")
