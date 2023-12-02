import time
import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import pygame.mixer
from labyrinthe import Labyrinthe
from character import Enemy
from character import Warrior, Mage, Thief,Boss
from dice import Dice
from sound import sound_game_over, sound_in_game, sound_last_boss, sound_lobby, sound_victory




class GameEngine:
    def __init__(self):
        self.player = None
        self.enemy = None
        self.labyrinth = None
        self.difficulty = None
        self._exits_reached = 0
        self.current_sound = None

        
    def play_lobby_music(self):
        if self.current_sound != sound_lobby:
            if self.current_sound:
                self.current_sound.stop()
            self.current_sound = sound_lobby
            self.current_sound.play()


    def play_in_game_music(self):
        if self.current_sound != sound_in_game:
            if self.current_sound:
                self.current_sound.stop()
            self.current_sound = sound_in_game
            self.current_sound.play()


    def choose_difficulty(self, player, enemy):
        self.player = player
        self.enemy = enemy

        self.play_lobby_music()

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
                
                self.play_in_game_music()

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
        self.play_in_game_music()
        self.clear_console()
        self.display_welcome_story()
        self.clear_console()



        while self.labyrinth._exits_reached < 3:  # Modifiez ici pour vérifier si le nombre de sorties atteintes est inférieur à 3
            self.clear_console()
            self.labyrinth.display()
            self.display_player_status()

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
                    self.labyrinth.generate() 
                    self.labyrinth._exits_reached += 1  
                    self.display_exits_count()  
            else:
                print("Invalid move. Try again.")
        
        if self.labyrinth._exits_reached >= 3:
            print("You've reached the exit 3 times. It's time to face the final boss!")
            self.display_final_boss_battle()

    def display_exits_count(self):
        print(f"You've reached the exit {self._exits_reached} times.")

    def display_final_boss_battle(self):
        self.clear_console()
        print("You've reached the final boss! Prepare for the ultimate battle.")
        time.sleep(2)

        final_boss = Boss("Final Boss", 50, 15, 10, Dice(8))

        while self.player.is_alive() and final_boss.is_alive():
            self.clear_console()
            self.player.show_healthbar()
            final_boss.show_healthbar()

            print("\nIt's your turn to attack!")
            time.sleep(1)
            self.player.attack(final_boss)

            if not final_boss.is_alive():
                break

            print("\nIt's the boss's turn to attack!")
            time.sleep(1)
            final_boss.special_attack(self.player)

            # Demander au joueur s'il veut continuer le combat
            input("\nPress Enter to continue the battle.")

        if self.player.is_alive():
            print("Congratulations! You defeated the final boss.")
        else:
            print("You were defeated by the final boss. Game over.")

        input("Press Enter to return to the labyrinth.")

    def change_floor(self):
        print("Regenerating the labyrinth...")
        self.play_in_game_music()  # Assure-toi que la musique in-game continue après le changement de niveau
        labyrinth_size, num_enemies = self.get_difficulty_settings(self.difficulty)
        self.labyrinth = Labyrinthe(labyrinth_size, labyrinth_size, self.player, num_enemies)
        print("You've changed floors. A new labyrinth awaits!")


    def display_player_status(self):
        print("\nPlayer Status:")
        self.player.show_healthbar()


    def enter_battle(self):
        sound_in_game.stop()
        sound_last_boss.play()
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
            input("\nPress Enter to continue the battle.")

        if self.player.is_alive():
            sound_victory.play()
            print("Congratulations! You won the battle.")
        else:
            sound_game_over.play()
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

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')