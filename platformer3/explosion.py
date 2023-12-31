from pygame.sprite import Sprite
from constants import *
class Explosion(Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images = list()
        for i in range(1,6):
            image = pygame.image.load(f"img/explosion/exp{i}.png")
            self.images.append(image)


        self.frame_index = 0
        self.counter = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect(center = (x,y))

    def update(self):
        EXPLOSION_COOLDOWN = 5
        self.counter += 1
        if self.counter >= EXPLOSION_COOLDOWN:
            self.counter = 0
            self.frame_index += 1
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]
        

