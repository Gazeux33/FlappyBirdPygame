import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game_manager):
        super().__init__()
        self.game_manager = game_manager
        self.image = pygame.image.load("src/assets/player.png")
        self.image = pygame.transform.scale(self.image, (120, 70))
        #self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = self.game_manager.HEIGHT / 2
        self.velocity = 4
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

    def check_collide(self, groupe):
        if pygame.sprite.spritecollideany(self, groupe) or self.rect.y > self.game_manager.HEIGHT - self.game_manager.HEIGHT_BASE:
            self.game_manager.speed = 0
            self.verticalSpeed = 0
            self.gravity = 0

