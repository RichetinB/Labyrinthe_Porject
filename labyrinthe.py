import random
import os
from character import Enemy
from dice import Dice

class Labyrinthe:
    COLOR_PLAYER = "\033[92m" 
    COLOR_EXIT = "\033[93m"  
    COLOR_ENEMY = "\033[91m"  
    COLOR_POTION = "\033[94m"  
    COLOR_WALL = "\033[90m"    
    COLOR_RESET = "\033[0m"     

    def __init__(self, p, q, player, enemy):
        self.p = p
        self.q = q
        self.enemy = enemy
        self._exits_reached = 0

        self.generate()

    def generate(self):
        self.matrix = [[' ' for _ in range(self.q)] for _ in range(self.p)]
        self.player_position = (0, 0)
        self.exit_position = (self.p - 1, self.q - 1)
        self.enemy_position = (random.randint(0, self.p - 1), random.randint(0, self.q - 1))
        self.potion = (random.randint(0, self.p - 1), random.randint(0, self.q - 1))
        self.place_element('P', self.player_position)
        self.place_element('✨', self.exit_position)
        self.place_element('E', self.enemy_position)
        self.place_element('🧪', self.potion)
    

        for i in range(self.p):
            for j in range(self.q):
                if (i, j) not in [self.player_position, self.exit_position, self.enemy_position] and random.random() < 0.3:
                    self.matrix[i][j] = '#'

    def place_element(self, element, position):
        x, y = position
        self.matrix[x][y] = element

    def is_traversable(self, x, y):
        return self.matrix[x][y] not in ['#', '|', '| ', '-', '+']

    def display(self):
        for row in self.matrix:
            row_str = ' '.join([
                f"{self.COLOR_PLAYER}{cell}{self.COLOR_RESET}" if cell == 'P' else
                f"{self.COLOR_EXIT}{cell}{self.COLOR_RESET}" if cell == '✨' else
                f"{self.COLOR_ENEMY}{cell}{self.COLOR_RESET}" if cell == 'E' else
                f"{self.COLOR_POTION}{cell}{self.COLOR_RESET}" if cell == '🧪' else
                f"{self.COLOR_WALL}{cell}{self.COLOR_RESET}" for cell in row
            ])
            print(row_str)
        print()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def move_player(self, direction):
        self.clear_console()
        x, y = self.player_position
        self.matrix[x][y] = ' '

        if direction == 'z' and x > 0:
            x -= 1
        elif direction == 'q' and y > 0:
            y -= 1
        elif direction == 's' and x < self.p - 1:
            x += 1
        elif direction == 'd' and y < self.q - 1:
            y += 1

        self.player_position = (x, y)
        self.place_element('P', self.player_position)

        if self.player_position == self.exit_position:
            return True
        elif self.player_position == self.potion:
            self.clear_console()
            print("You found a potion! Using it would be too easy...")
            input("Press Enter to continue...")
            self.clear_console()
            self.display()
            return False
       

        if self.player_position == self.exit_position:
            return True

        return False

    def is_valid_move(self, direction):
        self.clear_console()
        x, y = self.player_position

        if direction == 'z' and x > 0 and self.matrix[x - 1][y] != '#':
            return True
        elif direction == 'q' and y > 0 and self.matrix[x][y - 1] != '#':
            return True
        elif direction == 's' and x < self.p - 1 and self.matrix[x + 1][y] != '#':
            return True
        elif direction == 'd' and y < self.q - 1 and self.matrix[x][y + 1] != '#':
            return True

        return False

    def Battle(self):
        if self.player_position == self.enemy_position:
            return True

        return False

    def is_exit(self):
        if self.player_position == self.exit_position:
            return True
        
        return False
