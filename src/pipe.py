from abc import ABC
import pygame
from random import randint


class PipeManager:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.spaceX = 300
        self.spaceY = 200
        self.nbPipe = 40
        self.index = game_manager.player.rect.x + self.spaceX
        self.group = pygame.sprite.Group()
        self.validated_pipe = []
        self.score = 0
        self.buffer_score = 0

    def add_pair(self):
        pos = randint(200, self.game_manager.HEIGHT - 200)
        self.group.add(PipeDown(self.index, pos, self.game_manager))
        self.group.add(PipeUp(self.index, pos, self, self.game_manager))
        self.index += self.spaceX

    def update_group(self):
        if len(self.group) < self.nbPipe:
            self.add_pair()

        for pipe in self.group:
            pipe.rect.x -= self.game_manager.speed
            if self.game_manager.player.rect.x > pipe.rect.x and pipe not in self.validated_pipe:
                self.validated_pipe.append(pipe)
                self.buffer_score += 1
                if self.buffer_score == 2:
                    self.score += 1
                    self.buffer_score = 0
                    print(self.score)
            if pipe.rect.x + pipe.rect.width < 0:
                self.group.remove(pipe)


    def display_group(self):
        self.update_group()
        self.group.draw(self.game_manager.displaysurface)


class PipeUp(pygame.sprite.Sprite):
    def __init__(self, x, y, pipe_manager, game_manager):
        super().__init__()
        self.posy = game_manager.HEIGHT - pipe_manager.spaceY - y
        self.image = pygame.image.load("src/assets/pipe.png")
        if self.posy >= 0:
            self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.posy))
        self.image = pygame.transform.flip(self.image, 1, 1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0


class PipeDown(pygame.sprite.Sprite):
    def __init__(self, x, y, game_manager):
        super().__init__()
        self.longueur_tuyau = y - game_manager.HEIGHT_BASE + 5
        self.image = pygame.image.load("src/assets/pipe.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.longueur_tuyau))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = game_manager.HEIGHT - y
