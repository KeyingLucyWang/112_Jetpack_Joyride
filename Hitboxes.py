import pygame
import math
from gameObject import GameObject

class Hitboxes(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cors = (self.x - self.w / 2, self.y - self.h / 2,
                     self.x + self.w / 2, self.y + self.h / 2)

    def update(self, screenWidth, screenHeight):
        pass
    
    def draw(self, screen):
        pass
    
