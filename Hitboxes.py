import pygame
import math
from gameObject import GameObject

class Hitboxes(object):
    def __init__(self, x, y, w, h, itemClass):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.itemClass = itemClass
        if itemClass == "coins":
            self.cors = ((self.x - self.w / 2, self.y - self.h / 2,
                          self.x + self.w / 2, self.y + self.h / 2))
        elif itemClass == "obstacles":
            self.cors = (self.x - self.w / 2 + 35, self.y - self.h / 2 + 55,
                         self.x + self.w / 2 - 35, self.y + self.h / 2 - 55)

    def update(self, screenWidth, screenHeight):
        pass
    
    def draw(self, screen):
        pass
    
