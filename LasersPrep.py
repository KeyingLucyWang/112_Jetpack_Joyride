import pygame
import math
from gameObject import GameObject

class LasersPrep(GameObject):
    @staticmethod
    def init():
        LasersPrep.sprite = [pygame.transform.scale(pygame.image.load("laser eye.png"),
                                             (80, 80)),
                             pygame.transform.scale(pygame.image.load("laser eye2.png"),
                                             (80, 80)),
                             pygame.transform.scale(pygame.image.load("laser eye3.png"),
                                             (80, 80)),
                             pygame.transform.scale(pygame.image.load("laser eye4.png"),
                                             (80, 80))]


    def __init__(self, x, y):
        self.image = LasersPrep.sprite[0]
        self.width, self.height = self.image.get_size()
        self.scroll = 0
        self.past = False
        self.count = 0
        super(LasersPrep, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight, playerX, playerY):
        self.image = LasersPrep.sprite[self.count % 4]
        if self.count >= 120:
            self.kill()
        self.count += 1
        super(LasersPrep, self).update(screenWidth, screenHeight, self.image)
