import random
import os
from random import shuffle, randrange

class Labyrinthe:
    def __init__(self, p, q, player, enemy):
        self.p = p
        self.q = q
        self.enemy = enemy
        self.generate()

    def generate(self):
        self.matrix = [[' ' for _ in range(self.q)] for _ in range(self.p)]
        self.player_position = (0, 0)
        self.exit_position = (self.p - 1, self.q - 1)  # Position de la sortie
        self.enemy_position = (random.randint(0, self.p - 1), random.randint(0, self.q - 1))
        self.place_element('P', self.player_position)
        self.place_element('✨', self.exit_position)
        self.place_element('E', self.enemy_position)

        # Génération du labyrinthe (version simplifiée)
        for i in range(self.p):
            for j in range(self.q):
                if (i, j) not in [self.player_position, self.exit_position, self.enemy_position] and random.random() < 0.3:
                    self.matrix[i][j] = '#'  # 30% de chance d'ajouter un mur

    def place_element(self, element, position):
        x, y = position
        self.matrix[x][y] = element

    def is_traversable(self, x, y):
        # Vérifie si la position (x, y) est traversable
        return self.matrix[x][y] not in ['#', '|', '| ', '-', '+']

    def display(self):
        for row in self.matrix:
            print(' '.join(row))
        print()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def move_player(self, direction):
        self.clear_console()
        x, y = self.player_position
        self.matrix[x][y] = ' '  # Efface la position actuelle du joueur

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
            return True  # Le joueur a atteint la sortie, la partie est gagnée

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
            return True  # Le joueur rentre en combat

        return False
