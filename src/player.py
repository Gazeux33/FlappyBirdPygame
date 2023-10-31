import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game_manager):
        super().__init__()
        self.image = pygame.image.load("src/assets/player.png")
        self.image = pygame.transform.scale(self.image, (120, 70))
        self.rect = self.image.get_rect()
        self.rect.x = game_manager.WIDTH / 2
        self.rect.y = game_manager.HEIGHT / 2
        self.velocity = 5
        self.gravity = 0.1
        self.verticalSpeed = 0

    def update(self):
        self.verticalSpeed += self.gravity
        self.rect.y += self.verticalSpeed

    def display(self, surface):
        self.update()
        surface.blit(self.image, self.rect)

    def bounce(self):
        self.verticalSpeed = -self.velocity
