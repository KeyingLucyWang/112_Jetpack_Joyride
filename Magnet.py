import pygame
import math
from gameObject import GameObject

class Magnet(GameObject):
    @staticmethod
    def init():
        Magnet.image = pygame.transform.scale(pygame.image.load("magnet.png"),
                                              (50, 50))

    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("magnet.png"),
                                              (40, 35))
        super(Magnet, self).__init__(x - 50, y + 50, self.image)

    def update(self, screenWidth, screenHeight, playerX, playerY):
        self.x = playerX - 40
        self.y = playerY + 40
        super(Magnet, self).update(screenWidth, screenHeight, self.image)


        
