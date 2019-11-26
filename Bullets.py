import pygame
import math
from gameObject import GameObject

class Bullets(GameObject):
    @staticmethod
    def init():
        Bullets.image = pygame.transform.scale(pygame.image.load("bullet-A.png"),
                                              (50, 50))

    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("bullet-A.png"),
                                              (50, 30))
        super(Bullets, self).__init__(x, y, self.image)
        self.distanceTraveled = 0

    def update(self, screenWidth, screenHeight):
        if self.distanceTraveled >= 300:
            self.kill()
        self.x += 20
        self.distanceTraveled += 20
        super(Bullets, self).update(screenWidth, screenHeight, self.image)

'''
    def update(self, dt, keysDown, screenWidth, screenHeight):
        print("update")
        self.x += 50
        self.distanceTraveled += 50
        super(Bullets, self).update(screenWidth, screenHeight, Bullets.image)
'''         
        
