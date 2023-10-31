import pygame
import sys

from player import Player
from background import BackGround
from pipe import PipeManager


class GameManager:
    def __init__(self) -> None:
        self.WIDTH = 500
        self.HEIGHT = 700
        self.HEIGHT_BASE = 136
        self.speed = 1
        self.displaysurface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Flappy")
        self.FramePerSec = pygame.time.Clock()
        self.background = BackGround()
        self.player = Player(self)
        self.pipe_manager = PipeManager(self)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.bounce()

            self.background.display(self.speed, self.displaysurface)
            self.player.display(self.displaysurface)
            self.pipe_manager.display_group()
            self.player.check_collide(self.pipe_manager.group)

            pygame.display.update()
            self.FramePerSec.tick(120)
