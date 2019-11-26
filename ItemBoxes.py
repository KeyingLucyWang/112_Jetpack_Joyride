import pygame
import math
from gameObject import GameObject

class ItemBoxes(GameObject):
    @staticmethod
    def init():
        pass

    def __init__(self, x, y, itemType):
        self.image = pygame.transform.scale(pygame.image.load("item box.png"),
                                            (60, 60))
        width, height = self.image.get_size()
        #self.hitbox = Hitboxes(x, y, width, height, "item boxes")
        self.scroll = 0
        self.scrollY = 0
        self.hit = False
        self.itemType = itemType # either invincible or magnet suit
        super(ItemBoxes, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight, playerX, playerY):
        if playerX - self.x - self.width / 2 > screenWidth / 2:
            self.kill()
        super(ItemBoxes, self).update(screenWidth, screenHeight, self.image)
