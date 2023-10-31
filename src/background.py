import pygame


class BackGround:
    def __init__(self) -> None:
        self.image = pygame.image.load("src/assets/bg.png")
        self.x1 = 0
        self.x2 = self.image.get_width()

    def display(self, speed, surface):
        self.x1 -= speed
        self.x2 -= speed
        surface.blit(self.image, (self.x1, 0))
        surface.blit(self.image, (self.x2, 0))
        if self.x1 <= -self.image.get_width():
            self.x1 = self.x2 + self.image.get_width()
        if self.x2 <= -self.image.get_width():
            self.x2 = self.x1 + self.image.get_width()
