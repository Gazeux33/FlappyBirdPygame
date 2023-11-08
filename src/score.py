import pygame


class Score:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.numbers = {"0": pygame.image.load("src/assets/0.png"),
                        "1": pygame.image.load("src/assets/1.png"),
                        "2": pygame.image.load("src/assets/2.png"),
                        "3": pygame.image.load("src/assets/3.png"),
                        "4": pygame.image.load("src/assets/4.png"),
                        "5": pygame.image.load("src/assets/5.png"),
                        "6": pygame.image.load("src/assets/6.png"),
                        "7": pygame.image.load("src/assets/7.png"),
                        "8": pygame.image.load("src/assets/8.png"),
                        "9": pygame.image.load("src/assets/9.png")}
        self.y = game_manager.HEIGHT/5
        self.x_unite = game_manager.WIDTH/2
        self.x_dizaine = self.x_unite - self.numbers["0"].get_width()+3
        self.x_centaine = self.x_dizaine - self.numbers["0"].get_width()+5

    def display_score(self, score, screen):
        if score > 999:
            score = 999

        unite = score % 10
        dizaine = (score % 100) // 10
        centaine = score // 100

        screen.blit(self.numbers[str(unite)], (self.x_unite, self.y))
        if score > 9:
            screen.blit(self.numbers[str(dizaine)], (self.x_dizaine, self.y))
        if score > 99:
            screen.blit(self.numbers[str(centaine)], (self.x_centaine, self.y))


