import pygame
import math
from gameObject import GameObject

class Laser(GameObject):
    @staticmethod
    def init():
        #image = pygame.image.load("purpleClouds.jpg").convert_alpha()
        pass

    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("Laser.png").convert_alpha(),
                                            (100, 95))
        width, height = self.image.get_size()
        super(Laser, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight):
        super(Laser, self).update(screenWidth, screenHeight, self.image)
