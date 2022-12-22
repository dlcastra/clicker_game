import pygame
import random

pygame.init()
pygame.font.init()
pygame.display.set_caption('CLICK ON PABLO')

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
IMAGE = pygame.transform.scale(IMAGE ,(250,250))
target_rect = IMAGE.get_rect()

score = 0
font = pygame.font.Font(None, 36)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if target_rect.collidepoint(event.pos):
                    score += 1

                else:
                    score -= 1

    clock.tick(FPS)
    screen.fill((123, 104, 238))
    score_surface = ARIAL_64.render(str(score), True, (0, 0, 0))
    score_rect = score_surface.get_rect()

    score_rect.midtop = SCREEN_TOP
    target_rect.midtop = SCREEN_CENTER
    screen.blit(IMAGE, target_rect)
    screen.blit(score_surface, score_rect)

    pygame.display.flip()
pygame.quit()


