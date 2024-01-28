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

level = 0
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

world_data = []
for row in range(ROWS):
    r = [-1] * MAX_COL
    world_data.append(r)

for tile in range(MAX_COL):
    world_data[-1][tile] = 0

screen = pygame.display.set_mode((SCREEN_WIDTH+SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption("Level_editor")

pine1_img = pygame.image.load("img/background/pine1.png")
pine2_img = pygame.image.load("img/background/pine2.png")
mountain_img = pygame.image.load("img/background/mountain.png")
sky_img = pygame.image.load("img/background/sky_cloud.png")

save_img = pygame.image.load("img/save.png")
load_img = pygame.image.load("img/load.png")


font = pygame.font.SysFont("arial", 22)


def draw_text(text, font, color, x,y):
    t = font.render(text, True, color)
    screen.blit(t, (x,y))

save_button = Button(SCREEN_WIDTH /2, SCREEN_HEIGHT + LOWER_MARGIN - 60, save_img , 1)
load_button = Button(SCREEN_WIDTH/2 + 250, SCREEN_HEIGHT + LOWER_MARGIN - 60, load_img, 1)



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


def draw_world():
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] >= 0:
                screen.blit(img_list[world_data[i][j]], (j * TILE_SIZE -scroll, i * TILE_SIZE))


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
            if event.key == pygame.K_UP:
                level += 1
            if event.key == pygame.K_DOWN and level > 0:
                level -= 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1 

    if scroll_left and scroll >0:
        scroll -= 5 * scroll_speed
    if scroll_right and scroll < MAX_COL * TILE_SIZE - SCREEN_WIDTH:
        scroll += 5 * scroll_speed
    
    pos = pygame.mouse.get_pos()
    x = (pos[0] + scroll) // TILE_SIZE
    y = pos[1] // TILE_SIZE

    if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
        if pygame.mouse.get_pressed()[0]:
            if world_data[y][x] != current_tile:
                world_data[y][x] = current_tile
        if pygame.mouse.get_pressed()[2]:
            world_data[y][x] = -1

    # save and load button click event handlers
    # save level world data into csv and pickle file and load the data

    draw_bg()
    darw_grid()
    draw_world()
    draw_text(f"level: {level}", font, (255,255,255), 10, SCREEN_HEIGHT + LOWER_MARGIN - 100)
    draw_text(f"Press Up or Down to change level", font, (255,255,255), 10, SCREEN_HEIGHT + LOWER_MARGIN - 60)
    pygame.draw.rect(screen, (20, 255, 10), (SCREEN_WIDTH,0, SIDE_MARGIN, SCREEN_HEIGHT))
    for i in range(len(button_list)):
        if button_list[i].draw(screen):
            current_tile = i
    pygame.draw.rect(screen, (255,0,0), button_list[current_tile].rect, 3)
    if save_button.draw(screen):
        # with open(f"levels\level{level}.csv", 'w', newline='') as csv_file:
        #     w = csv.writer(csv_file, delimiter=',')
        #     for row in world_data:
        #         w.writerow(row)
        f = open(f"levels\level{level}", 'wb')
        pickle.dump(world_data, f)
        f.close()
    if load_button.draw(screen):
        scroll = 0
        # with open(f"levels\level{level}.csv","r", newline='') as csv_file:
        #     reader = list(csv.reader(csv_file, delimiter=','))
        #     for i in range(len(reader)):
        #         for j in range(len(reader[i])):
        #             world_data[i][j] = int(reader[i][j])

        world_data = []
        f = open(f"levels\level{level}", 'rb')
        world_data = pickle.load(f)


    pygame.display.update()
    clock.tick(FPS)