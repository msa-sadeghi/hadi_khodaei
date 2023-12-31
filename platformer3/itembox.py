from constants import *
from pygame.sprite import Sprite

class ItemBox(Sprite):
    def __init__(self, item_type, x,y):
        super().__init__()
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE/2,y + TILE_SIZE - self.image.get_height())
        

    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            if self.item_type == "Health":
                player.health += 25
                if player.health > player.max_health:
                    player.health = player.max_health
            elif self.item_type == "Ammo":
                player.ammo += 15
            elif self.item_type == "Grenade":
                player.grenade_counts += 3
            self.kill()
        