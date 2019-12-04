import pygame
import math
from gameObject import GameObject
from Bullets import Bullets
from Magnet import Magnet
from Coins import Coins
from Obstacles import Obstacles

class Player(GameObject):
    @staticmethod
    def init():
        # all images taken from: https://bevouliin.com/game-character-green-fur-monster-sprite-sheets/
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
            
        Player.attack = [pygame.image.load("Attack/a1.png"),
                         pygame.image.load("Attack/a2.png"),
                         pygame.image.load("Attack/a3.png")]
        for i in range(len(Player.attack)):
            Player.attack[i] = pygame.transform.scale(Player.attack[i],(60, 60))

        Player.invincible = [pygame.image.load("Invincible/a1.png"),
                             pygame.image.load("Invincible/a2.png"),
                             pygame.image.load("Invincible/a3.png")]
        for i in range(len(Player.invincible)):
            Player.invincible[i] = pygame.transform.scale(Player.invincible[i],(180, 100))
        
        Player.image = Player.fly[0]
        Player.powerUp = False
        
    def __init__(self, x, y):
        super(Player, self).__init__(x, y, Player.image)
        self.angle = 0
        self.timeAlive = 0
        self.isAlive = True
        self.acceleration = (0, 9.8*2.5) #accounts for gravity
        self.velocity = (0, 0)
        #self.t = 1/30
        self.powerUp = False
        self.goingUp = False
        self.mode = "fly"
        self.bullets = []
        self.magnet = None
        self.count = 0
        self.powerUpCount = 0
        self.scroll = 0

    def update(self, dt, keysDown, screenWidth, screenHeight):
        self.timeAlive += dt
        if self.mode == "invincible":
            if self.count >= 80:
                self.mode = "fly"
                self.count = 0
            if keysDown(pygame.K_UP):
                self.y -= 10
                if self.y - self.height / 2 < 0:
                    self.y = self.height / 2
            elif keysDown(pygame.K_DOWN):
                self.y += 10
                if self.y + self.height / 2 > screenHeight - 30:
                    self.y = screenHeight - 30 - self.height / 2
                    vy = 0
            Player.image = Player.invincible[self.count % 3]
            self.count += 1
        else:
            if self.mode == "fly":
                #print("fly mode entered", Player.count)
                self.count += 1
                if self.goingUp:
                    #Player.count = Player.count % 2
                    Player.image = Player.fly[self.count % 8]
                elif self.count % 2 == 0:
                    Player.image = Player.fly[(self.count // 2) % 8]
            elif self.mode == "attack":
                #print("attack mode", self.count)
                if self.count >= 2:
                    #print("switching back to fly", Player.count)
                    self.mode = "fly"
                    self.count = 0
                Player.image = Player.attack[(self.count % 3)]
                self.count += 1
            elif self.mode == "magnet suit":
                if self.count >= 130:
                    #print("back to fly mode")
                    self.mode = "fly"
                    self.count = 0
                    self.magnet = None
                Player.image = Player.fly[self.count % 8]
                self.count += 1
            ax, ay = self.acceleration
            vx, vy = self.velocity
            dt1 = dt / 250
            dt2 = dt / 250
            if vy < 0:
                self.goingUp = True
            else:
                self.goingUp = False
            if keysDown(pygame.K_UP):
                self.powerUpCount = 0
                #self.count = 7
                self.powerUp = True
            #if not keysDown(pygame.K_UP):
                #vy += 15
            if keysDown(pygame.K_UP):
                vy -= (16 - self.powerUpCount)
                if self.powerUpCount <= 16:
                    self.powerUpCount += 2
                if self.y - self.height / 2 < 0:
                    self.y = self.height / 2
                    #vy = -5
                    
            if self.powerUp and vy >= 9.8 * 1.5:
                self.powerUp = False
            #if self.goingUp and vy >= 0:
            #   self.goingUp = False
                if self.mode == "fly":
                    self.count *= 2
            if self.goingUp:
                vy = vy + ay * dt2
                self.y = self.y + vy * dt2
                if self.y - self.height / 2 < 0:
                    self.y = self.height / 2
            else:
                vy = vy + ay * dt1
                self.y = self.y + vy * dt1 
                if self.y + self.height / 2 > screenHeight - 30:
                    self.y = screenHeight - 30 - self.height / 2
            if (self.y >= screenHeight - 30 - self.height / 2) and not keysDown(pygame.K_UP):
                vy = 0
            if self.y <= self.height / 2 and not keysDown(pygame.K_UP):
                vy = 0
            if vy <= -40:
                vy = -40
            self.velocity = (vx, vy)
            self.acceleration = (ax, ay)
        super(Player, self).update(screenWidth, screenHeight, Player.image)

    def collide(self, items):
        for item in items:
            if isinstance(item, Obstacles):
                (x0, y0, x1, y1) = (item.x - item.width / 2 + 35,
                                    item.y - item.height / 2 + 55,
                                    item.x + item.width / 2 - 35,
                                    item.y + item.height / 2 - 55)
            else:
                (x0, y0, x1, y1) = (item.x - item.width / 2 , item.y - item.height / 2,
                                    item.x + item.width / 2 , item.y + item.height / 2)
            '''
            if isinstance(item, Coins):
                (x0, y0, x1, y1) = (item.x - item.width / 2 + item.scroll, item.y - item.height / 2 + item.scrollY,
                                    item.x + item.width / 2 + item.scroll, item.y + item.height / 2 + item.scrollY)
            else:
                (x0, y0, x1, y1) = item.hitbox.cors
            '''
            (i0, j0, i1, j1) = (self.x - self.width / 2,
                                self.y - self.height / 2,
                                self.x + self.width / 2,
                                self.y + self.height / 2)
            #print((x0, y0, x1, y1),
            #      (j0, j0, i1, j1))
            if ((i0 <= x1) and (x0 <= i1)) and ((y0 <= j1) and (j0 <= y1)):
                return True, item
        return False, None

    def collideCoins(self, items):
        coins = []
        for item in items:
            (x0, y0, x1, y1) = (item.x - item.width / 2 , item.y - item.height / 2,
                                item.x + item.width / 2 , item.y + item.height / 2)
            (i0, j0, i1, j1) = (self.x - self.width / 2,
                                self.y - self.height / 2,
                                self.x + self.width / 2,
                                self.y + self.height / 2)
            if ((i0 <= x1) and (x0 <= i1)) and ((y0 <= j1) and (j0 <= y1)):
                coins.append(item)
        if len(coins) > 0:
            return True, coins
        return False, None
'''
    def powerUp(self):
        # perform power-up once
        force = 10
        time = clock.tick(self.fps)
        self.timerFired(time)
        self.powerUp = False
'''



    
