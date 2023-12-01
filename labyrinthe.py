import random
import os
from random import shuffle, randrange

class Labyrinthe:
    def __init__(self, p, q, player):
        self.p = p
        self.q = q
        self.player_position = (0, 0)
        self.exit_position = (p - 1, q - 1)  # Position de la sortie
        self.player = player
        self.generate()

    def generate(self):
        self.matrix = [[' ' for _ in range(self.q)] for _ in range(self.p)]
        self.matrix[0][0] = 'P'  # Position initiale du joueur
        self.matrix[self.exit_position[0]][self.exit_position[1]] = '✨'  # Position de la sortie

        # Génération du labyrinthe (version simplifiée)
        for i in range(self.p):
            for j in range(self.q):
                if (i, j) != (0, 0) and (i, j) != self.exit_position and random.random() < 0.3:
                    self.matrix[i][j] = '#'  # 30% de chance d'ajouter un mur



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
        self.matrix[x][y] = 'P'  # Met à jour la nouvelle position du joueur

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