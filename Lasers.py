import pygame
import math
from gameObject import GameObject

class Lasers(GameObject):
    @staticmethod
    def init():
        # image taken from: https://backgrounddownload.com/wp-content/uploads/2018/09/lightsaber-blade-transparent-background-300x200.png
        Lasers.sprite = pygame.transform.scale(pygame.image.load("laser.png"),
                                               (680, 10))
        Lasers.transparent = pygame.transform.scale(pygame.image.load("transparent.png"),
                                                    (20, 20))

    def __init__(self, x, y):
        self.image = Lasers.transparent
        self.width, self.height = Lasers.sprite.get_size()
        self.scroll = 0
        self.past = False
        self.count = 0
        self.laserOn = False
        super(Lasers, self).__init__(x, y, self.image)
        self.width, self.height = Lasers.sprite.get_size()

    def update(self, screenWidth, screenHeight, playerX, playerY):
        if self.count <= 40:
            self.image = Lasers.transparent
        else:
            self.image = Lasers.sprite
            self.laserOn = True
        if self.count >= 100:
            self.kill()
        self.count += 1
        super(Lasers, self).update(screenWidth, screenHeight, self.image)
       

    
