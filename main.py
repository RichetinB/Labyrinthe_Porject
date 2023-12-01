from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from character import Warrior, Mage, Thief, Character, Enemy
from engine import GameEngine
from dice import Dice
from labyrinthe import Labyrinthe
from engine import GameEngine

console = Console()

# Cadre de bienvenue stylé
welcome_frame = Table(show_header=False, show_lines=False)
welcome_frame.add_row("[bold yellow]Welcome to the[/bold yellow]")
welcome_frame.add_row("[bold yellow]  Labyrinth Game![/bold yellow]")

console.print(welcome_frame)

name = console.input("[bold blue]Enter your name: [/bold blue]")
console.print("[bold magenta]Choose your class: [/bold magenta]")

class_table = Table(title="[cyan]Available Classes[/cyan]")
class_table.add_column("Class Number", style="cyan", justify="right")
class_table.add_column("Class", style="green", justify="left")
class_table.add_row("1", "Warrior")
class_table.add_row("2", "Mage")
class_table.add_row("3", "Thief")
console.print(class_table)

class_choice = console.input("[bold blue]Enter the number of your class: [/bold blue]")

if class_choice == "1":
    player_class = Warrior(name, 20, 8, 3, Dice(6))
elif class_choice == "2":
    player_class = Mage(name, 20, 8, 3, Dice(6))
elif class_choice == "3":
    player_class = Thief(name, 20, 8, 3, Dice(6))
else:
    console.print("[bold red]Invalid class choice. Exiting the game.[/bold red]")
    exit()

my_ennemy = Enemy("MOB", 5, 2, 1, Dice(6))

engine = GameEngine(labyrinth_size=10, player=player_class, enemy=my_ennemy)
engine.play_game()