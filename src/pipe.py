from abc import ABC
import pygame
from random import randint


class PipeManager:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.spaceX = 200
        self.spaceY = 200
        self.nbPipe = 40
        self.index = game_manager.player.rect.x + self.spaceX
        self.group = pygame.sprite.Group()


    def add_pair(self):
        pos = randint(200, self.game_manager.HEIGHT - 200)

        self.group.add(PipeDown(self.index, pos, self.game_manager))
        self.group.add(PipeUp(self.index, pos, self,self.game_manager))
        self.index += self.spaceX

    def update_group(self):
        if len(self.group) < self.nbPipe:
            self.add_pair()
        for pipe in self.group:
            pipe.rect.x -= self.game_manager.speed
            if pipe.rect.x + pipe.rect.width < 0:
                self.group.remove(pipe)

    def display_group(self):
        self.update_group()
        self.group.draw(self.game_manager.displaysurface)


class PipeUp(pygame.sprite.Sprite):
    def __init__(self, x, y, pipe_manager, game_manager):
        print("tuyau haut")
        super().__init__()
        print(f"y={y},x={x}")
        self.posy = game_manager.HEIGHT - pipe_manager.spaceY - y
        print(f"longueur={self.posy}")
        self.image = pygame.image.load("src/assets/pipe.png")
        if self.posy >= 0:
            self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.posy))
        self.image = pygame.transform.flip(self.image, 1, 1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0
        print(f"y={y},x={x}")


class PipeDown(pygame.sprite.Sprite):
    def __init__(self, x, y, game_manager):
        super().__init__()
        print("tuyau bas")
        print(f"y={y},x={x}")
        self.longueur_tuyau = y - game_manager.HEIGHT_BASE + 5
        print(f"hauteur base={game_manager.HEIGHT_BASE} , longueur={self.longueur_tuyau}")
        self.image = pygame.image.load("src/assets/pipe.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.longueur_tuyau))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = game_manager.HEIGHT - y
        print(f"y={y},x={x}")
