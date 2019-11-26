import pygame
import math
from gameObject import GameObject

class Rockets(GameObject):
    @staticmethod
    def init():
        # image take from: https://www.stickpng.com/assets/images/58e911aceb97430e819064d8.png
        Rockets.image = pygame.transform.scale(pygame.image.load("rocket.png"), (80, 60))
        
    def __init__(self, x, y):
        self.image = Rockets.image
        width, height = self.image.get_size()
        self.scroll = 0
        self.scrollY = 0
        self.hit = False
        self.count = 0
        self.past = False
        self.isVisible = False
        super(Rockets, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight, playerX, playerY):
        if playerX - self.x - self.width / 2 > screenWidth / 2:
            self.kill()
        self.x -= 40
        self.scroll += 40
        super(Rockets, self).update(screenWidth, screenHeight, self.image)

    
