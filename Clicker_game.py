import pygame
import random

pygame.init()
pygame.font.init()

W = 100
H = 600
SCREEN_SIZE = (W, H)
SCREEN_CENTER = (W // 2, H // 2)
SCREEN_TOP = (W // 2, 0)

screen = pygame.display.set_mode(SCREEN_SIZE)

FPS = 60
clock = pygame.time.Clock()

ARIAL_FONT_PATH = pygame.font.match_font('arial')
ARIAL_64 = pygame.font.Font(ARIAL_FONT_PATH, 64)
ARIAL_32 = pygame.font.Font(ARIAL_FONT_PATH, 32)

