import pygame
import random

pygame.init()
pygame.font.init()

WIDTH = 1000
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
SCREEN_CENTER = (WIDTH // 2, HEIGHT // 2)
SCREEN_TOP = (WIDTH // 2, 0)

screen = pygame.display.set_mode(SCREEN_SIZE)
FPS = 60
clock = pygame.time.Clock()

ARIAL_FONT_PATH = pygame.font.match_font('arial')
ARIAL_64 = pygame.font.Font(ARIAL_FONT_PATH, 64)
ARIAL_32 = pygame.font.Font(ARIAL_FONT_PATH, 32)

IMAGE = pygame.image.load('pablo.png')
IMAGE = pygame.transform.scale(IMAGE ,(100,100))
target_rect = IMAGE.get_rect()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

