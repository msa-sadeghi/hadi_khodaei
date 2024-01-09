import pygame

class Button:
    def __init__(self, x,y, image, scale) -> None:
        self.image = pygame.transform.scale(image, (scale * image.get_width(), scale * image.get_height()))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.clicked = False

    def draw(self, screen):
        actions = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                actions = True
                self.clicked = True
        if not pygame.mouse.get_pressed()[0] :
                self.clicked = False


        screen.blit(self.image, self.rect)

        return actions


        