# game_engine.py
from rich.console import Console
from rich.table import Table
from rich.text import Text
from labyrinthe import Labyrinthe

console = Console()

class GameEngine:
    def __init__(self, labyrinth_size, player):
        self.labyrinth = Labyrinthe(labyrinth_size, labyrinth_size, player)
        self.player = player

    def display_welcome_message(self):
        welcome_text = Text()
        welcome_text.append("Congratulations! You won!", style="bold white on green")
        console.print(welcome_text)

    def play_game(self):
        console.print(f"Welcome, {self.player.get_name()}!")
        console.print(f"You have chosen the [bold cyan]{self.player.__class__.__name__}[/bold cyan] class.")

        while True:
            self.labyrinth.display()
            direction = input("Enter direction (z/q/s/d to move, or 'exit' to quit): ")

            if direction == 'exit':
                console.print("Exiting the game. Goodbye!")
                break

            if self.labyrinth.is_valid_move(direction):
                if self.labyrinth.move_player(direction):
                    self.display_welcome_message()
                    break
            else:
                console.print("Invalid move. Try again.")
