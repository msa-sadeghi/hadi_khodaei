from constants import *
class HealthBar:
    def __init__(self, x,y, health, max_health) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health


    def draw(self, screen, health):
        self.health = health
        ratio = self.health/self.max_health

        pygame.draw.rect(screen, (255, 0,0), (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, (0, 255,0), (self.x, self.y, ratio * 150, 20))
        pygame.draw.rect(screen, (230, 0,230), (self.x, self.y,  150, 20), 2)


