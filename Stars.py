import pygame
import math
from gameObject import GameObject

# class not used in the game
class Stars(GameObject):
    @staticmethod
    def init():
        # image taken from: https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/google/110/sparkles_2728.png
        Stars.sprite = [pygame.transform.scale(pygame.image.load("stars.png"),
                                               (20, 20)),
                        pygame.transform.scale(pygame.image.load("stars.png"),
                                               (18, 18)),
                        pygame.transform.scale(pygame.image.load("stars.png"),
                                               (15, 15))]

    def __init__(self, x, y):
        self.image = Stars.sprite[0]
        width, height = self.image.get_size()
        self.count = 0
        self.scroll = 0
        self.show = False
        super(Stars, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight):
        self.image = Stars.sprite[self.count % 3]
        if self.show:
            self.count += 1
        super(Stars, self).update(screenWidth, screenHeight, self.image)
        if self.count >= 2:
            self.show = False
            self.kill()
            self.count = 0
