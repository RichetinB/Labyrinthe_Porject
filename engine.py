import time
import os
from labyrinthe import Labyrinthe

class GameEngine:
    def __init__(self, labyrinth_size, player):
        self.labyrinth = Labyrinthe(labyrinth_size, labyrinth_size, player)
        self.player = player

    def play_game(self):
        self.clear_console()
        self.display_welcome_story()
        input("\nPress Enter to continue...")
        self.clear_console()
        print(f"Welcome, {self.player.get_name()}!")
        print(f"You have chosen the {self.player.__class__.__name__} class.")
        while True:
            self.labyrinth.display()
            direction = input("Enter direction (z/q/s/d to move, or 'exit' to quit): ")

            if direction == 'exit':
                print("Exiting the game. Goodbye!")
                break

            if self.labyrinth.is_valid_move(direction):
                if self.labyrinth.move_player(direction):
                    self.display_congratulations_story()
                    print("Congratulations! You won!")
                    break
            else:
                print("Invalid move. Try again.")

    def display_welcome_story(self):
        print("Once upon a time...")
        time.sleep(1)
        print("You find yourself in a mysterious labyrinth surrounded by ancient trees.")
        time.sleep(2)
        print("Legends speak of a hidden exit that leads to untold treasures.")
        time.sleep(2)
        print("Brave adventurer, your quest begins now!")

    def display_congratulations_story(self):
        print("As you step through the exit, you feel a rush of triumph.")
        time.sleep(2)
        print("You have conquered the labyrinth and claimed the legendary treasures!")
        time.sleep(2)
        print("The world will forever remember the brave adventurer who navigated the maze.")

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
