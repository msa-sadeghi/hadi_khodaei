import pygame
import csv
import pickle


pygame.init()
clock = pygame.time.Clock()
FPS = 60


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

LOWER_MARGIN = 100
SIDE_MARGIN = 300


scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1


screen = pygame.display.set_mode((SCREEN_WIDTH+SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption("Level_editor")

pine1_img = pygame.image.load("img/background/pine1.png")
pine2_img = pygame.image.load("img/background/pine2.png")
mountain_img = pygame.image.load("img/background/mountain.png")
sky_img = pygame.image.load("img/background/sky_cloud.png")


def draw_bg():
    screen.fill((10,240,30))
    screen.blit(sky_img, (0 - scroll,0))
    screen.blit(mountain_img, (0 - scroll,SCREEN_HEIGHT - mountain_img.get_height() - 300))
    screen.blit(pine1_img, (0 - scroll,SCREEN_HEIGHT - pine1_img.get_height() - 150))
    screen.blit(pine2_img, (0 - scroll,SCREEN_HEIGHT - pine2_img.get_height()))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False

    if scroll_left and scroll >0:
        scroll -= 5
    if scroll_right:
        scroll += 5
    
    draw_bg()

    pygame.display.update()
    clock.tick(FPS)