import pygame
import math
from gameObject import GameObject

# class not used in the game
class Hitboxes(object):
    def __init__(self, x, y, w, h, itemClass):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = None
        
        self.itemClass = itemClass
        if itemClass == "coins":
            self.cors = ((self.x - self.w / 2, self.y - self.h / 2,
                          self.x + self.w / 2, self.y + self.h / 2))
        elif itemClass == "obstacles":
            self.cors = (self.x - self.w / 2 + 35, self.y - self.h / 2 + 55,
                         self.x + self.w / 2 - 35, self.y + self.h / 2 - 55)
        elif itemClass == "item boxes":
            self.cors = ((self.x - self.w / 2, self.y - self.h / 2,
                          self.x + self.w / 2, self.y + self.h / 2))
        #super(Hitboxes, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight):
        if self.itemClass == "coins":
            self.cors = ((self.x - self.w / 2, self.y - self.h / 2,
                          self.x + self.w / 2, self.y + self.h / 2))
        elif self.itemClass == "obstacles":
            self.cors = (self.x - self.w / 2 + 35, self.y - self.h / 2 + 55,
                         self.x + self.w / 2 - 35, self.y + self.h / 2 - 55)
        elif self.itemClass == "item boxes":
            self.cors = ((self.x - self.w / 2, self.y - self.h / 2,
                          self.x + self.w / 2, self.y + self.h / 2))
        #super(Hitboxes, self).update(screenWidth, screenHeight, self.image)
    
    
