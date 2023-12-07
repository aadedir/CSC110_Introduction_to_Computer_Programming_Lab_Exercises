import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors Game")

        self.player_name = ""
        self.user_choice = ""
        self.wins = 0
        self.losses = 0

        self.create_start_gui()

    def create_start_gui(self):
        start_frame = tk.Frame(self.root)
        start_frame.pack(pady=20)

        label = tk.Label(start_frame, text="Enter Your Name:")
        label.grid(row=0, column=0, padx=10)

        self.name_entry = tk.Entry(start_frame)
        self.name_entry.grid(row=0, column=1, padx=10)

        start_button = tk.Button(start_frame, text="Start Playing", command=self.start_playing)
        start_button.grid(row=1, columnspan=2, pady=10)

    def start_playing(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showerror("Error", "Please enter your name.")
            return

        self.create_game_gui()

    def create_game_gui(self):
        game_frame = tk.Frame(self.root)
        game_frame.pack(pady=20)

        choices = ["Rock", "Paper", "Scissors"]

        def on_choice_selected(choice):
            self.user_choice = choice
            computer_choice = random.choice(choices)

            outcome = self.determine_winner(self.user_choice, computer_choice)

            messagebox.showinfo("Result", f"{self.player_name}, you chose {self.user_choice}. "
                                           f"Computer chose {computer_choice}.\n\n{outcome}")

            if "win" in outcome.lower():
                self.wins += 1
            elif "lose" in outcome.lower():
                self.losses += 1

            # Update the final tally
            self.update_final_tally()

        for choice in choices:
            button = tk.Button(game_frame, text=choice, command=lambda c=choice: on_choice_selected(c))
            button.pack(side="left", padx=10)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif ((player_choice == "Rock" and computer_choice == "Scissors") or
              (player_choice == "Paper" and computer_choice == "Rock") or
              (player_choice == "Scissors" and computer_choice == "Paper")):
            return "YOU WIN!!!"
        else:
            return "You lose."

    def update_final_tally(self):
        # If you want to display the running count, you can add a label or messagebox here
        continue_frame = tk.Frame(self.root)
        continue_frame.pack(pady=20)

        continue_label = tk.Label(continue_frame, text="Continue playing?")
        continue_label.pack()

        yes_button = tk.Button(continue_frame, text="Yes", command=self.create_game_gui)
        yes_button.pack(side="left", padx=10)

        no_button = tk.Button(continue_frame, text="No", command=self.display_final_stats)
        no_button.pack(side="right", padx=10)

    def create_stats_gui(self):
        stats_frame = tk.Frame(self.root)
        stats_frame.pack(pady=20)

        stats_label = tk.Label(stats_frame, text=f"Wins: {self.wins}, Losses: {self.losses}")
        stats_label.pack()

    def display_final_stats(self):
        messagebox.showinfo("Game Over", f"Thanks for playing, {self.player_name}!\n\n"
                                         f"Final Stats:\nWins: {self.wins}\nLosses: {self.losses}")
        self.root.destroy()


if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.root.mainloop()
