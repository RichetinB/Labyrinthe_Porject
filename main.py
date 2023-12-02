from rich.console import Console
from rich.table import Table
from character import Warrior, Mage, Thief, Enemy
from engine import GameEngine
from dice import Dice
import os

console = Console()

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

# Cadre de bienvenue stylé
welcome_frame = Table(show_header=False, show_lines=False)
welcome_frame.add_row("[bold yellow]Welcome to the[/bold yellow]")
welcome_frame.add_row("[bold yellow]  Labyrinth Game![/bold yellow]")

console.print(welcome_frame)
input("\nPress Enter to continue...")

clear_console()
limit_name = 10
while True:
    name = console.input(f"[bold blue]Enter your name (max {limit_name} characters): [/bold blue]")
    
    # Vérifier si la longueur du nom est inférieure ou égale à la limite
    if len(name) <= limit_name:
        break
    else:
        console.print(f"[bold red]Name exceeds the character limit of {limit_name}. Please enter a shorter name.[/bold red]")
console.print("[bold magenta]Choose your class: [/bold magenta]")

# Afficher les caractéristiques des classes
class_table = Table(title="[cyan]Available Classes[/cyan]")
class_table.add_column("Class Number", style="cyan", justify="right")
class_table.add_column("Class", style="green", justify="left")
class_table.add_column("Attack", style="yellow", justify="right")
class_table.add_column("Defense", style="yellow", justify="right")
class_table.add_column("Health", style="yellow", justify="right")

# Ajouter les caractéristiques des classes
class_table.add_row("1", "Warrior", "8", "3", "20")
class_table.add_row("2", "Mage", "8", "3", "20")
class_table.add_row("3", "Thief", "8", "3", "20")

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

clear_console()
def choose_difficulty(self):
        print("Choose your difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        while True:
            choice = input("Enter the number of your choice: ")
            if choice in ['1', '2', '3']:
                return int(choice)
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")


def get_difficulty_settings(self, difficulty):
    if difficulty == 1:
        return 10, 2  
    elif difficulty == 2:
        return 15, 4 
    elif difficulty == 3:
        return 20, 6 
    
my_enemy = Enemy("MOB", 22, 5, 2, Dice(10))

engine = GameEngine()
engine.choose_difficulty(player_class, my_enemy)
engine.play_game()