import pygame
import math
from gameObject import GameObject

class Obstacles(GameObject):
    @staticmethod
    def init():
        # image taken from: https://www.freepngimg.com/thumb/light/69349-ball-purple-light-energy-google-effects-images.png
        Obstacles.sprite = [pygame.transform.scale(pygame.image.load("lightning ball.png"),
                                            (150, 150)),
                            pygame.transform.scale(pygame.image.load("lightning ball2.png"),
                                            (150, 150)),
                            pygame.transform.scale(pygame.image.load("lightning ball3.png"),
                                            (150, 150)),
                            pygame.transform.scale(pygame.image.load("lightning ball4.png"),
                                            (150, 150)),
                            pygame.transform.scale(pygame.image.load("lightning ball.png"),
                                            (150, 150)),
                            pygame.transform.scale(pygame.image.load("lightning ball2.png"),
                                            (150, 150)),
                            pygame.transform.scale(pygame.image.load("lightning ball3.png"),
                                            (150, 150)),
                            pygame.transform.scale(pygame.image.load("lightning ball4.png"),
                                            (150, 150))]

    def __init__(self, x, y):
        self.image = Obstacles.sprite[0]
        self.width, self.height = self.image.get_size()
        #self.hitbox = Hitboxes(x, y, self.width, self.height, "obstacles")
        self.count = 0
        self.scroll = 0
        self.scrollY = 0
        #self.past = False
        super(Obstacles, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight, playerX, playerY):
        self.image = Obstacles.sprite[(self.count // 2) % 8]
        self.count += 1
        if playerX - self.x - self.width / 2 > screenWidth / 2:
            self.kill()
        super(Obstacles, self).update(screenWidth, screenHeight, self.image)
