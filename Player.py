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
            Player.fly[i] = pygame.transform.scale(Player.fly[i],(60, 60))
        Player.count = 0
        Player.image = Player.fly[0]
        Player.powerUp = False
        
    def __init__(self, x, y):
        super(Player, self).__init__(x, y, Player.image)
        self.angle = 0
        self.timeAlive = 0
        self.isAlive = True
        self.acceleration = (0, 9.8*2) #accounts for gravity
        self.velocity = (0, 0)
        #self.t = 1/30
        self.powerUp = False
        self.goingUp = False

    def update(self, dt, keysDown, screenWidth, screenHeight):
        self.timeAlive += dt
        Player.count += 1
        if self.goingUp:
            #Player.count = Player.count % 2
            Player.image = Player.fly[Player.count % 8]
        elif Player.count % 2 == 0:
            Player.image = Player.fly[(Player.count // 2) % 8]
        ax, ay = self.acceleration
        vx, vy = self.velocity
        dt1 = dt / 300
        dt2 = dt / 220
        if keysDown(pygame.K_UP) and (not self.powerUp):
            self.goingUp = True
            Player.count = 7
            self.powerUp = True
            #ay -= 25
            #self.y = vy * self.timeAlive + 0/5 * ay * (self.timeAlive**2)
            #vy = -8 + ay * dt
            vy = -50
            #self.y = self.y + vy * dt
            #self.velocity = (vx, vy)
            #self.acceleration = (ax, ay)
            #print("velocity", self.velocity,
            #      "acceleration", self.acceleration)
        #elif self.powerUp:
            #self.y = self.y + vy * dt
            #vy = vy + ay * dt
            #if vy < 9.8:
                #ay += 2
        #if vy > 9.8 * 3:
            #vy = 9.8 * 3
        #if ay > 9.8:
            #ay = 9.8
            #self.velocity = (vx, vy)
            #self.acceleration = (ax, ay)
            #if self.y + self.height / 2 > screenHeight:
                #self.isAlive = False
            #if self.y - self.height / 2 < 0:
                #self.y = self.height / 2
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
            #self.y -= 30
            if self.y - self.height / 2 < 0:
                self.y = self.height / 2
                
        if self.powerUp and vy >= 9.8 * 1.5:
            self.powerUp = False
        if self.goingUp and vy >= 0:
            self.goingUp = False
            Player.count *= 2
        if self.y + self.height / 2 > screenHeight:
                self.isAlive = False
        if self.y - self.height / 2 < 0:
                self.y = self.height / 2
        if self.goingUp:
            vy = vy + ay * dt2
            self.y = self.y + vy * dt2
        else:
            vy = vy + ay * dt1
            self.y = self.y + vy * dt1
        self.velocity = (vx, vy)
        self.acceleration = (ax, ay)
        super(Player, self).update(screenWidth, screenHeight, Player.image)

    def collide(self, obstacles):
        for obstacle in obstacles:
            (x0, y0, x1, y1) = obstacle.hitbox.cors
            (i0, j0, i1, j1) = (self.x - self.width / 2, self.y - self.height / 2,
                                self.x + self.width / 2, self.y + self.height / 2)
            #print((x0, y0, x1, y1),
            #      (j0, j0, i1, j1))
            if ((i0 <= x1) and (x0 <= i1)) and ((y0 <= j1) and (j0 <= y1)):
                return True, hitbox
        return False, None

'''
    def powerUp(self):
        # perform power-up once
        force = 10
        time = clock.tick(self.fps)
        self.timerFired(time)
        self.powerUp = False
'''



    
