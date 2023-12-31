from pygame.sprite import Sprite
from constants import GRENADE_IMAGE, GRAVITY, SCREEN_WIDTH
from explosion import Explosion
from constants import *
class Grenade(Sprite):
    def __init__(self, x,y,direction, explosion_group):
        super().__init__()
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = GRENADE_IMAGE
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = direction
        self.explosion_group = explosion_group
        

    def update(self, player, enemy_group):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y


        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.speed = 0

        if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
            self.direction *= -1
            dx = self.direction * self.speed 


        self.rect.x += dx
        self.rect.y += dy
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y)
            self.explosion_group.add(explosion)
            if abs(self.rect.centerx - player.rect.centerx) < 2 * TILE_SIZE and abs(self.rect.centery - player.rect.centery) < 2 * TILE_SIZE:
                player.health -= 50

            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < 2 * TILE_SIZE and abs(self.rect.centery - enemy.rect.centery) < 2 * TILE_SIZE:
                    enemy.health -= 50


