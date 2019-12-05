import pygame
import math
from gameObject import GameObject

# This is the WarningSigns class
# import warning sign images
# contain init and update methods for WarningSigns objects
class WarningSigns(GameObject):
    @staticmethod
    def init():
        # image taken from: http://www.pngall.com/wp-content/uploads/2017/05/Alert-Download-PNG.png
        # image taken from: https://www.transparenttextures.com/patterns/asfalt-light.png
        WarningSigns.sprite = [pygame.transform.scale(pygame.image.load("warning.png"),
                                                      (50, 50)),
                               pygame.transform.scale(pygame.image.load("warning.png"),
                                                      (50, 50)),
                               pygame.transform.scale(pygame.image.load("transparent.png"),
                                                      (50, 50)),
                               pygame.transform.scale(pygame.image.load("transparent.png"),
                                                      (50, 50))]

    def __init__(self, x, y):
        self.image = WarningSigns.sprite[0]
        width, height = self.image.get_size()
        self.scroll = 0
        self.count = 0
        super(WarningSigns, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight):
        self.image = WarningSigns.sprite[self.count % 4]
        if self.count >= 20:
            self.kill()
        self.count += 1
        super(WarningSigns, self).update(screenWidth, screenHeight, self.image)

