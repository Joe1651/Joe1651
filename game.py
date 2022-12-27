import pygame
import time

import obstacles
from player import Player
from obstacles import Obstacles

pygame.init()


class Game:
    def __init__(self):
        # Obstacle class
        self.running = True
        self.obst = Obstacles()
        # Clock
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks() // 60

        # Sets the screen
        self.screenX = 1280
        self.screenY = 720
        self.screen = pygame.display.set_mode([self.screenX, self.screenY])

        # Title and Icon
        pygame.display.set_caption("Alpha v0.1")  # Sets caption
        self.icon = pygame.image.load("assets/img/car.png")  # Loads Icon
        pygame.display.set_icon(self.icon)  # Set Icon

        # Resize background to screen
        self.background = pygame.image.load("assets/img/background720.jpg")
        self.background = pygame.transform.scale(self.background, (self.screenX, self.screenY))

        # Sets the player
        self.ispressed = False
        self.player = Player()
        self.playeroad = self.player.playerroad

    def compteur(self):
        self.current_time = pygame.time.get_ticks()//60
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.current_time}", True, (0,0,0))

        self.screen.blit(text, (1075, 30))

    def handling_inputs(self):
        pressed = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time
        if elapsed_time >= 250:
            self.ispressed = False

        if not self.ispressed:
            self.start_time = current_time

        if pressed[pygame.K_DOWN] and self.playeroad < 3 and self.ispressed == False:
            self.playeroad += 1
            self.ispressed = True
            print("Down KEY", self.playeroad)
        if pressed[pygame.K_UP] and self.playeroad > 1 and self.ispressed == False:
            self.playeroad -= 1
            self.ispressed = True
            print("Up Key", self.playeroad)

    def roadchange(self):
        self.player.player_rect.y = 295+((self.playeroad-1)*120)
        self.player.ypos = 295 + ((self.playeroad - 1) * 120)

    def drawbackground(self):
        # Draws the background
        self.screen.blit(self.background, (0, 0))

    def drawsprites(self):
        for obst in self.obst.obstacles:
            self.screen.blit(self.obst.barrier_img, (obst["x"], obst["y"]))
         # Draws player
        self.screen.blit(self.player.player, self.player.player_rect)

    def obstmove(self):
        for obst in self.obst.obstacles:
            obst["x"] -= self.obst.obstacle_speed
            obst["rect"].x -= self.obst.obstacle_speed

            if obst["x"] < 0:
                self.obst.obstacles.remove(obst)

            if self.player.player_rect.colliderect(obst["rect"]):
                print(f"Game Over! \nFinal Score: {self.current_time}")
                self.running = False
                self.screen.fill((255,255,255))

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            break
                    # If the player pressed Y, start a new game
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_y]:
                                # Reset the player's position
                        self.player.xpos = 400
                        self.player.ypos = 400
                            # Clear the list of obstacles
                        self.obst.obstacles.clear()
                        self.obst.obstspawn()
                        self.running = True
                        break
                    elif keys[pygame.K_n]:
                        break
                    else:
                        pass

                    font = pygame.font.Font(None, 36)
                    pointage = font.render(f"Score: {self.current_time}", True, (0, 0, 0))
                    text = font.render("Voulez-vous rejouer? (Y/N)", True, (0, 0, 0))
                    self.screen.blit(text, (500, 300))
                    self.screen.blit(pointage, (600, 350))
                    pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            # Loops and check if quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.drawbackground()
            self.compteur()
            self.drawsprites()
            self.handling_inputs()
            self.roadchange()
            self.player.rectposupdate()
            self.obst.obstspawn()
            self.obstmove()
            # Updates the screen [IMPORTANT]
            pygame.display.update()
    pygame.quit()
