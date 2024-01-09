import pygame
import csv
import pickle
from button import Button

pygame.init()
clock = pygame.time.Clock()
FPS = 60


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

ROWS = 16
MAX_COL = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
current_tile = 0
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


img_list = []
for i in range(TILE_TYPES):
    img = pygame.image.load(f"img/tile/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)


button_list = list()
button_col = 0
button_row = 0
for i in range(len(img_list)):
    tile_button = Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1)
    button_list.append(tile_button)
    button_col += 1
    if button_col == 3:
        button_row += 1
        button_col = 0


def draw_bg():
    screen.fill((10,240,30))
    width = sky_img.get_width()
    for i in range(4):
        screen.blit(sky_img, (i * width - scroll * 0.5,0))
        screen.blit(mountain_img, (i * width - scroll * 0.6,SCREEN_HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img, (i * width - scroll * 0.7,SCREEN_HEIGHT - pine1_img.get_height() - 150))
        screen.blit(pine2_img, (i * width - scroll * 0.8,SCREEN_HEIGHT - pine2_img.get_height()))

def darw_grid():
    for i in range(MAX_COL  + 1):
        pygame.draw.line(screen, (255,255,255), (i * TILE_SIZE-scroll, 0), (i * TILE_SIZE-scroll, SCREEN_HEIGHT ))
    for i in range(ROWS  + 1):
        pygame.draw.line(screen, (255,255,255), (0, i * TILE_SIZE), (SCREEN_WIDTH, i * TILE_SIZE ))





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
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1 

    if scroll_left and scroll >0:
        scroll -= 5 * scroll_speed
    if scroll_right:
        scroll += 5 * scroll_speed
    
    draw_bg()
    darw_grid()
    pygame.draw.rect(screen, (20, 255, 10), (SCREEN_WIDTH,0, SIDE_MARGIN, SCREEN_HEIGHT))
    for i in range(len(button_list)):
        if button_list[i].draw(screen):
            current_tile = i
    print("tile # ", current_tile)
    pygame.draw.rect(screen, (255,0,0), button_list[current_tile].rect, 3)

    pygame.display.update()
    clock.tick(FPS)