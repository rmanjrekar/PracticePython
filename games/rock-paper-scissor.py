'''
Rock Paper Scissors (RPS) is a zero-sum game, typically played by two people using their hands and no tools. Players deliver hand signals representing rock, paper, or scissors, with the outcome determined by these three rules:

Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.

Here, we are allowing a player to pick its choice against computer which randomly chose from any of these choices ['rock', 'paper', 'scissors'].
'''

from random import choice
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.choice = None

    @abstractmethod
    def choose(self):
        pass

class HumanPlayer(Player):
    def choose(self):
        while True:
            choice = input(f"{self.name}, choose (rock/paper/scissors): ").lower()
            if choice in ['rock', 'paper', 'scissors']:
                self.choice = choice
                break
            else:
                print("Invalid choice. Please choose again.")

class ComputerPlayer(Player):
    def choose(self):
        self.choice = choice(['rock', 'paper', 'scissors'])

class Game:
    def __init__(self, name):
        self.player = HumanPlayer(name)
        self.computer = ComputerPlayer("Computer")

    def play_round(self):
        self.player.choose()
        self.computer.choose()

        print(f"{self.player.name} chose {self.player.choice}")
        print(f"{self.computer.name} chose {self.computer.choice}")

        if self.player.choice == self.computer.choice:
            print("It's a tie!")
        elif (self.player.choice == 'rock' and self.computer.choice == 'scissors') or \
             (self.player.choice == 'paper' and self.computer.choice == 'rock') or \
             (self.player.choice == 'scissors' and self.computer.choice == 'paper'):
            print(f"{self.player.name} wins!")
        else:
            print(f"{self.computer.name} wins!")

    def play_game(self):
        while True:
            self.play_round()
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Game!")
    name = input("Enter your name : ")
    game = Game(name)
    game.play_game()
