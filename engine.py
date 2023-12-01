import time
import os
from labyrinthe import Labyrinthe
from character import Enemy
from character import Warrior, Mage, Thief
from dice import Dice


class GameEngine:
    def __init__(self):
        self.player = None
        self.enemy = None
        self.labyrinth = None
        self.difficulty = None

    def choose_difficulty(self, player, enemy):
        self.player = player
        self.enemy = enemy

        print("Choose your difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        while True:
            choice = input("Enter the number of your choice: ")
            if choice in ['1', '2', '3']:
                self.difficulty = int(choice)
                self.labyrinth_size, num_enemies = self.get_difficulty_settings(self.difficulty)
                self.labyrinth = Labyrinthe(self.labyrinth_size, self.labyrinth_size, self.player, num_enemies)
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def get_difficulty_settings(self, difficulty):
        if difficulty == 1:
            return 10, 2  
        elif difficulty == 2:
            return 15, 4 
        elif difficulty == 3:
            return 20, 6 

    def play_game(self):
        self.clear_console()
        self.display_welcome_story()
        self.clear_console()
        while True:
            self.clear_console()
            self.labyrinth.display()
            direction = input("Enter direction (z/q/s/d to move, 'exit' to quit, 'change' to regenerate labyrinth): ")

            if direction == 'change':
                self.change_floor()
                continue

            if self.labyrinth.Battle():
                self.enter_battle()
                if self.player.is_alive():
                    print("Congratulations! You won the battle.")
                else:
                    print("You were defeated in battle. Game over.")
                    break

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
        

    def change_floor(self):
        print("Regenerating the labyrinth...")
        labyrinth_size, num_enemies = self.get_difficulty_settings(self.difficulty)
        self.labyrinth = Labyrinthe(labyrinth_size, labyrinth_size, self.player, num_enemies)
        print("You've changed floors. A new labyrinth awaits!")


    def display_player_stats(self):
        print(f"Player Stats - {self.player.get_name()}")
        print(f"Class: {self.player.__class__.__name__}")
        print(f"HP: {self.player.get_current_hp()}/{self.player.get_max_hp()}")


    def enter_battle(self):
        self.clear_console()
        print("A wild enemy appears! Get ready for battle.")
        time.sleep(2)

        while self.player.is_alive() and self.enemy.is_alive():
            self.clear_console()
            self.player.show_healthbar()
            self.enemy.show_healthbar()

            print("\nIt's your turn to attack!")
            time.sleep(1)
            self.player.attack(self.enemy)

            if not self.enemy.is_alive():
                break

            print("\nIt's the enemy's turn to attack!")
            time.sleep(1)
            self.enemy.attack(self.player)

            # Demander au joueur s'il veut continuer le combat
            continue_battle = input("\nDo you want to continue the battle? (yes/no): ").lower()
            if continue_battle != 'yes':
                break

        if self.player.is_alive():
            print("Congratulations! You won the battle.")
        else:
            print("You were defeated in battle. Game over.")
        
        input("Press Enter to return to the labyrinth.")
        
        
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

    def display_battle_status(self):
        print("\nBattle Status:")
        print(f"{self.player.get_name()} HP: {self.player._current_hp}/{self.player._max_hp}")
        print(f"{self.enemy.get_name()} HP: {self.enemy._current_hp}/{self.enemy._max_hp}")

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
