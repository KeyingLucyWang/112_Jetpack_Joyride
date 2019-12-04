import pygame
import math
from gameObject import GameObject

class Bullets(GameObject):
    @staticmethod
    def init():
        # image taken from: https://bevouliin.com/game-character-green-fur-monster-sprite-sheets/
        Bullets.image = pygame.transform.scale(pygame.image.load("bullet-A.png"),
                                              (50, 30))
        # image taken from: https://bevouliin.com/game-character-green-fur-monster-sprite-sheets/
        Bullets.explosion = pygame.transform.scale(pygame.image.load("got-hit.png"), (50, 50))
        Bullets.explosion2 = pygame.transform.scale(pygame.image.load("got-hit.png"), (70, 70))
        
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("bullet-A.png"),
                                              (50, 30))
        super(Bullets, self).__init__(x, y, self.image)
        self.distanceTraveled = 0
        self.hit = False
        self.hitCount = 0

    def update(self, screenWidth, screenHeight, player):
        if self.hit:
            self.hitCount += 1
            if self.hitCount >= 3:
                self.image = Bullets.explosion2
            else:
                self.image = Bullets.explosion
        if self.distanceTraveled >= 300 or self.hitCount > 5:
            player.bullets.remove(self)
            self.kill()
        if not self.hit:
            self.x += 20
            self.distanceTraveled += 20
        super(Bullets, self).update(screenWidth, screenHeight, self.image)

    def hitItem(self, item):
        (x0, y0, x1, y1) = (item.x - item.width / 2 , item.y - item.height / 2,
                            item.x + item.width / 2 , item.y + item.height / 2)
        (i0, j0, i1, j1) = (self.x - self.width / 2,
                            self.y - self.height / 2,
                            self.x + self.width / 2,
                            self.y + self.height / 2)
        if ((i0 <= x1) and (x0 <= i1)) and ((y0 <= j1) and (j0 <= y1)):
            self.hit = True
            item.kill()
'''
    def update(self, dt, keysDown, screenWidth, screenHeight):
        print("update")
        self.x += 50
        self.distanceTraveled += 50
        super(Bullets, self).update(screenWidth, screenHeight, Bullets.image)
'''         
        
