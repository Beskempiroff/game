import pygame, random

pygame.init()

# variables and constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
HEADER_HEIGHT = 80

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)

BUFFER_DISTANCE = 100
PLAYER_STARTING_SCORE = 0
PLAYER_STARTING_LIVE = 5
GHOSTPCK_STARTING_VELOCITY = 5
YELLOWGHOSTCUT_STARTING_VELOCITY = 9

player_score = PLAYER_STARTING_SCORE
player_live = PLAYER_STARTING_LIVE
cut_velocity = 5
ghostpck_velocity = GHOSTPCK_STARTING_VELOCITY

yellowghostcut_velocity = YELLOWGHOSTCUT_STARTING_VELOCITY
acceleration = 0.5

# main surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("CuT")

# images
background = pygame.image.load('fon.jpeg')






    pygame.display.update()
    clock.tick(FPS)

pygame.quit()