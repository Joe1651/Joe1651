import pygame
import random
from player import Player

class Obstacles:

    def __init__(self):
        self.player = Player()
        self.obstacle_speed = 7
        self.obstacles = []
        self.barrier_img = pygame.image.load("assets/img/barrier.png")
        self.barrier_img = pygame.transform.scale(self.barrier_img, (120, 120))
        self.start_time = pygame.time.get_ticks()

    def obstspawn(self):
        if len(self.obstacles) < 2:
            y = 280 + 120 * random.randint(0, 2)
            self.obstacles.append({
                "x": 1280,
                "y": y,
                "rect": pygame.Rect(1280, y, self.barrier_img.get_width(), self.barrier_img.get_height())
            })
