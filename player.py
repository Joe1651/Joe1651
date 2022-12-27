import pygame


class Player:

    def __init__(self):
        self.xpos = 400
        self.ypos = 280
        self.playerroad = 2
        self.player = pygame.image.load("assets/img/playercar2.png")  # Loads player's car
        self.player = pygame.transform.scale(self.player, (260, 90))
        self.position = [self.xpos, 295 + self.ypos * self.playerroad]
        self.player_rect = pygame.Rect(self.xpos, self.ypos, self.player.get_width(), self.player.get_height())

    def rectposupdate(self):
        self.player_rect.x = self.xpos
        self.player_rect.y = self.ypos

