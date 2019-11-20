import pygame
import math
from gameObject import GameObject

class Player(GameObject):
    @staticmethod
    def init():
        #Player.image = pygame.transform.scale(pygame.image.load("bird.png").convert_alpha(),
        #                                      (40, 30))
        Player.fly = [pygame.image.load("flying/a1.png"),
                      pygame.image.load("flying/a2.png"),
                      pygame.image.load("flying/a3.png"),
                      pygame.image.load("flying/a4.png"),
                      pygame.image.load("flying/a5.png"),
                      pygame.image.load("flying/a6.png"),
                      pygame.image.load("flying/a7.png"),
                      pygame.image.load("flying/a8.png")]
        for i in range(len(Player.fly)):
            Player.fly[i] = pygame.transform.scale(Player.fly[i],(80, 80))
        Player.count = 0
        Player.image = Player.fly[0]
        Player.powerUp = False
        
    def __init__(self, x, y):
        super(Player, self).__init__(x, y, Player.image)
        self.angle = 0
        self.timeAlive = 0
        self.isAlive = True

    def update(self, dt, keysDown, screenWidth, screenHeight):
        self.timeAlive += dt
        Player.count += 1
        Player.image = Player.fly[Player.count % 8]
        if keysDown(pygame.K_UP):
            '''
            self.powerUp = True
            self.counter = 20
            self.factor = 1
            while self.powerUp:
                self.y -= self.counter / self.factor
                self.factor += 1
                super(Player, self).update(screenWidth, screenHeight, Player.image)
                if self.counter > 0:
                    self.counter /= self.factor
                elif self.counter < 0:
                    self.counter *= self.factor
                if self.counter < 0 and (abs(-self.counter - 5) < 1 / 1000):
                    self.powerUp = False
                elif self.counter > 0 and self.counter < 1 / 1000:
                    self.counter = -self.counter
            '''
            self.y -= 20
            if self.y - self.height / 2 < 0:
                self.y = self.height / 2
            #self.y -= 5
            #super(Player, self).update(screenWidth, screenHeight, Player.image)
            #self.y -= 3
            #super(Player, self).update(screenWidth, screenHeight, Player.image)
            #self.y -= 2
            #super(Player, self).update(screenWidth, screenHeight, Player.image)
            #self.y -= 1
            #super(Player, self).update(screenWidth, screenHeight, Player.image)
            #self.y -= 1
            #super(Player, self).update(screenWidth, screenHeight, Player.image)
            #self.y += 1
            #super(Player, self).update(screenWidth, screenHeight, Player.image)
            #self.y += 3
            #super(Player, self).update(screenWidth, screenHeight, Player.image)
            #self.y += 5
            #super(Player, self).update(screenWidth, screenHeight, Player.image)
            #self.y += 9
            #super(Player, self).update(screenWidth, screenHeight, Player.image)
        #elif keysDown(pygame.K_DOWN):
        if not self.powerUp:
            self.y += 5
            if self.y + self.height / 2 > screenHeight:
                self.isAlive = False
        super(Player, self).update(screenWidth, screenHeight, Player.image)

    def powerUp(self):
        # perform power-up once
        force = 10
        time = clock.tick(self.fps)
        self.timerFired(time)
        self.powerUp = False






    
