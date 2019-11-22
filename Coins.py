import pygame
import math
from gameObject import GameObject
from Hitboxes import Hitboxes
from Stars import Stars

class Coins(GameObject):
    @staticmethod
    def init():
        Coins.sprite = [pygame.image.load("coins/coin1.png"),
                        pygame.image.load("coins/coin2.png"),
                        pygame.image.load("coins/coin3.png"),
                        pygame.image.load("coins/coin4.png"),
                        pygame.image.load("coins/coin5.png"),
                        pygame.image.load("coins/coin6.png")]
        for i in range(len(Coins.sprite)):
            Coins.sprite[i] = pygame.transform.scale(Coins.sprite[i], (30, 30))
        Coins.count = 0
        Coins.heart = []
        Coins.lines = []
        Coins.curves = []

    def __init__(self, x, y):
        self.image = Coins.sprite[0]
        width, height = self.image.get_size()
        self.hitbox = Hitboxes(x, y, width, height, "coins")
        self.scroll = 0
        self.hit = False
        self.star = Stars(x + self.scroll, y)
        super(Coins, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight):
        self.image = Coins.sprite[Coins.count % 6]
        Coins.count += 1
        super(Coins, self).update(screenWidth, screenHeight, self.image)
