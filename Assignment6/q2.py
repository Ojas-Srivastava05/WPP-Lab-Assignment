import random

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ["rock", "paper", "scissors"]
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"
    
    def play(self):
        while self.current_round < self.rounds:
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            if user_choice not in self.choices:
                print("Invalid choice, try again.")
                continue
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            winner = self.find_winner(user_choice, computer_choice)
            if winner == "user":
                print("You win this round!")
            elif winner == "computer":
                print("Computer wins this round!")
            else:
                print("It's a draw!")
            self.current_round += 1
        self.check_winner()
    
    def check_winner(self):
        if self.user_wins > self.computer_wins:
            print("You win the game!")
        elif self.computer_wins > self.user_wins:
            print("Computer wins the game!")
        else:
            print("The game is a tie!")

rounds = int(input("Enter number of rounds: "))
game = Rock_paper_scissors(rounds)
game.play()
