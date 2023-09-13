import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to handle the game logic
def play_game(user_choice):
    global user_score, computer_score

    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)

    user_label.config(text=f"Your Choice: {user_choice.capitalize()}")
    computer_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!", fg="gray")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        result_label.config(text="You Win!", fg="green")
        user_score += 1
    else:
        result_label.config(text="You Lose!", fg="red")
        computer_score += 1

    update_score()
    play_again_button.config(state=tk.NORMAL)

# Function to update the score
def update_score():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

# Function to reset the game
def play_again():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_score()
    user_label.config(text="")
    computer_label.config(text="")
    result_label.config(text="")
    play_again_button.config(state=tk.DISABLED)

# Create the main application window
app = tk.Tk()
app.title("Rock, Paper, Scissors Game")

# Create labels for user and computer choices
user_label = tk.Label(app, text="", font=("Helvetica", 14))
user_label.pack()

computer_label = tk.Label(app, text="", font=("Helvetica", 14))
computer_label.pack()

# Create buttons for user choices
rock_button = tk.Button(app, text="Rock", command=lambda: play_game("rock"), font=("Helvetica", 12))
rock_button.pack()

paper_button = tk.Button(app, text="Paper", command=lambda: play_game("paper"), font=("Helvetica", 12))
paper_button.pack()

scissors_button = tk.Button(app, text="Scissors", command=lambda: play_game("scissors"), font=("Helvetica", 12))
scissors_button.pack()

# Create a label to display the game result
result_label = tk.Label(app, text="", font=("Helvetica", 16))
result_label.pack()

# Create score labels
user_score_label = tk.Label(app, text="Your Score: 0", font=("Helvetica", 12))
user_score_label.pack()

computer_score_label = tk.Label(app, text="Computer's Score: 0", font=("Helvetica", 12))
computer_score_label.pack()

# Create a button to play again
play_again_button = tk.Button(app, text="Play Again", command=play_again, state=tk.DISABLED, font=("Helvetica", 12))
play_again_button.pack()

# Run the application
app.mainloop()
