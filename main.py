import logging
import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Choose: rock, paper, or scissors: ")
computer_choice = random.choice(choices)
win = ""
draw = ""
lose = ""
print(f"I choice: {user_choice}")
print(f"Computer choice: {computer_choice}")

if user_choice == computer_choice:
    draw = "it's a draw :)"
    print(draw)
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    win = "I win ^^"
    print(win)
else:
    lose = "computer win :("
    print(lose)

with open("data/test.txt", "w" , encoding="utf-8") as file:
     file.write(f"winner: {win}, loser {lose}")        