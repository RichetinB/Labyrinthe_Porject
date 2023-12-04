import pygame
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

pygame.init()



sound_game_over = pygame.mixer.Sound("sounds/GameOver.mp3")
sound_in_game = pygame.mixer.Sound("sounds/InGame.mp3")
sound_last_boss = pygame.mixer.Sound("sounds/LastBoss.mp3")
sound_lobby = pygame.mixer.Sound("sounds/Lobby.mp3")
sound_victory = pygame.mixer.Sound("sounds/Victory.mp3")
