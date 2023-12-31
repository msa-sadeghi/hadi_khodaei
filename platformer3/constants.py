import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
FPS = 60
GRAVITY = 1
GRENADE_IMAGE = pygame.image.load("img/icons/grenade.png")
HEALTH_BOX_IMG = pygame.image.load("img/icons/health_box.png")
AMMO_BOX_IMG = pygame.image.load("img/icons/ammo_box.png")
GRENADE_BOX_IMG = pygame.image.load("img/icons/grenade_box.png")

item_boxes = {
    'Health':HEALTH_BOX_IMG,
    'Ammo':AMMO_BOX_IMG,
    'Grenade':GRENADE_BOX_IMG
}


TILE_SIZE = 32