import pygame
from constants import *
from grenade import Grenade
from soldier import Soldier, Enemy
from world import World
from itembox import ItemBox
from healthbar import HealthBar

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()


item_box = ItemBox('Health', 100,260)
item_box_group.add(item_box)

item_box = ItemBox('Ammo', 400,260)
item_box_group.add(item_box)

item_box = ItemBox('Grenade', 500,260)
item_box_group.add(item_box)





player = Soldier('player',500,200, 3, 5,1000,player_bullet_group)
enemy1 = Enemy('enemy',50,280, 3, 2,5,enemy_bullet_group)
enemy2 = Enemy('enemy',70,220, 3, 5,5,enemy_bullet_group)
enemy_group.add(enemy1)
enemy_group.add(enemy2)
world = World()

healthbar = HealthBar(10,10, player.health, player.health)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_SPACE:
                player.jump = True
            if event.key == pygame.K_LALT:
                player.shooting = True
            if event.key == pygame.K_q:
                player.grenade = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LALT:
                player.shooting = False
            if event.key == pygame.K_q:
                player.grenade = False
                player.grenade_thrown = False
    if player.alive:
        if player.shooting:
            
            
            player.shoot(enemy_group)
        elif player.grenade and not player.grenade_thrown and player.grenade_counts > 0:
            grenade = Grenade(player.rect.centerx + (0.5 * player.rect.size[0]* player.direction), \
                              player.rect.top, player.direction, explosion_group)
            grenade_group.add(grenade)
            player.grenade_counts -= 1
            player.grenade_thrown = True
        if player.in_air:
            player.update_action(2)
        elif player.moving_left or player.moving_right:
            player.update_action(1)
        else:
            player.update_action(0)
    
    ########################
    # enemy1.shoot(player)
    # enemy2.shoot(player)
    ########################
    world.draw_bg(screen)

    healthbar.draw(screen, player.health)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(screen)
    grenade_group.update(player,enemy_group)
    grenade_group.draw(screen)
    explosion_group.update()
    explosion_group.draw(screen)
    item_box_group.draw(screen)
    item_box_group.update(player)
    player.move(player.moving_left, player.moving_right)
    player.update()
    # enemy_group.update(screen, player)
    # enemy_group.draw(screen)
    #############################################

    for enemy in enemy_group:
        enemy.ai_movement(screen, player)
        enemy.update(screen, player)
        enemy.draw(screen)


    player.draw(screen)
    pygame.display.update()
    clock.tick(FPS)

