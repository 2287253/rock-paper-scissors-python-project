import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        # Initialize scores
        self.user_score = 0
        self.computer_score = 0
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Title
        self.title_label = tk.Label(
            self.main_frame,
            text="Rock Paper Scissors",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0"
        )
        self.title_label.pack(pady=20)
        
        # Score display
        self.score_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.score_frame.pack(pady=10)
        
        self.user_score_label = tk.Label(
            self.score_frame,
            text=f"Your Score: {self.user_score}",
            font=("Arial", 14),
            bg="#f0f0f0"
        )
        self.user_score_label.pack(side="left", padx=20)
        
        self.computer_score_label = tk.Label(
            self.score_frame,
            text=f"Computer Score: {self.computer_score}",
            font=("Arial", 14),
            bg="#f0f0f0"
        )
        self.computer_score_label.pack(side="right", padx=20)
        
        # Result display
        self.result_label = tk.Label(
            self.main_frame,
            text="Choose your move!",
            font=("Arial", 16),
            bg="#f0f0f0"
        )
        self.result_label.pack(pady=20)
        
        # Choice buttons
        self.button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.button_frame.pack(pady=20)
        
        # Create buttons with emojis
        self.rock_button = tk.Button(
            self.button_frame,
            text="🪨 Rock",
            font=("Arial", 14),
            width=10,
            command=lambda: self.play("rock")
        )
        self.rock_button.pack(side="left", padx=10)
        
        self.paper_button = tk.Button(
            self.button_frame,
            text="📄 Paper",
            font=("Arial", 14),
            width=10,
            command=lambda: self.play("paper")
        )
        self.paper_button.pack(side="left", padx=10)
        
        self.scissors_button = tk.Button(
            self.button_frame,
            text="✂️ Scissors",
            font=("Arial", 14),
            width=10,
            command=lambda: self.play("scissors")
        )
        self.scissors_button.pack(side="left", padx=10)
        
        # Reset button
        self.reset_button = tk.Button(
            self.main_frame,
            text="Reset Game",
            font=("Arial", 12),
            command=self.reset_game
        )
        self.reset_button.pack(pady=20)
    
    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        # Determine winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
        
        # Update result label
        self.result_label.config(
            text=f"Your choice: {user_choice.capitalize()}\n"
                 f"Computer's choice: {computer_choice.capitalize()}\n"
                 f"{result}"
        )
        
        # Update scores
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
        
        # Check for game end
        if self.user_score == 5 or self.computer_score == 5:
            winner = "You" if self.user_score == 5 else "Computer"
            messagebox.showinfo("Game Over", f"{winner} won the game!")
            self.reset_game()
    
    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
        self.result_label.config(text="Choose your move!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop() 