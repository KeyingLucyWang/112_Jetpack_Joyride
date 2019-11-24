import pygame
import random
from pygamegame import PygameGame
from Player import Player
from Obstacles import Obstacles
from Hitboxes import Hitboxes
from Coins import Coins
from Bullets import Bullets
#from Stars import Stars
from ItemBoxes import ItemBoxes
from Magnet import Magnet

class Game(PygameGame):
    def init(self):
        super().init()
        self.bg = pygame.image.load("mountain.png")
        self.bgWidth = self.bg.get_width()
        self.bgX = 0
        self.bgX2 = self.bgWidth
        #self.clock = pygame.time.Clock()
        self.scrollSpeed = 3
        self.isPaused = False
        self.score = 0
        pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(4000, 5500)) # random obstacles event
        pygame.time.set_timer(pygame.USEREVENT+2, random.randrange(1000, 2000)) # random coins event
        pygame.time.set_timer(pygame.USEREVENT+3, random.randrange(5000, 10000)) # random item boxes event


    def redrawAll(self, screen):
        # game over screen
        if not self.playerGroup.sprite.isAlive:
            screen.fill((0, 0, 0))
            font = pygame.font.Font("Amatic-Bold.ttf", 50)
            text = font.render('GAME OVER', True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (self.width / 2, self.height / 2)
            screen.blit(text, textRect)
            scoreFont = pygame.font.Font("Amatic-Bold.ttf", 30)
            score = scoreFont.render(f'Your score: {self.score}', True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (self.width / 2, self.height / 2 + 50)
            screen.blit(score, scoreRect)
            pygame.display.update()
            return

        # start screen
        if self.mode == "start":
            screen.blit(self.bg, (self.bgX, 0))
            titleFont = pygame.font.Font("Amatic-Bold.ttf", 50)
            title = titleFont.render('112 Jetpack Joyride', True, (0, 0, 0))
            titleRect = title.get_rect()
            titleRect.center = (self.width / 2, self.height / 2 - 70)
            screen.blit(title, titleRect)
            insFont = pygame.font.Font("Amatic-Bold.ttf", 25)
            ins = insFont.render('Press any key to start!', True, (0, 0, 0))
            insRect = ins.get_rect()
            insRect.center = (self.width / 2, self.height / 2)
            screen.blit(ins, insRect)
            pygame.display.update()

        # paused mode
        if self.isPaused:
            #screen.fill((255, 255, 255))
            pauseFont = pygame.font.Font("Amatic-Bold.ttf", 50)
            pause = pauseFont.render('GAME PAUSED', True, (0, 0, 0))
            pauseIns = pauseFont.render('Hit "p" to unpause', True, (0, 0, 0))
            pauseRect = pause.get_rect()
            pauseRect.center = (self.width / 2, self.height / 2 - 70)
            pauseInsRect = pauseIns.get_rect()
            pauseInsRect.center = (self.width / 2, self.height / 2)
            screen.blit(pause, pauseRect)
            screen.blit(pauseIns, pauseInsRect)
            pygame.display.update()

        # game mode
        elif self.mode == "game": 
            screen.blit(self.bg, (self.bgX, 0))
            screen.blit(self.bg, (self.bgX2, 0))
            self.playerGroup.draw(screen)
            self.obstacles.draw(screen)
            #print(self.stars)
            self.coins.draw(screen)
            self.itemBoxes.draw(screen)
            if self.player.bullet != None and self.player.bullet.distanceTraveled <= 300:
                #print("obstacle", self.obstaclesLst[0].x)
                #print("player", self.player.x, self.player.y)
                #print(self.player.bullet.x, self.player.bullet.y)
                self.bulletGroup.draw(screen)
            if self.player.magnet != None:
                self.magnetGroup.draw(screen)
            '''
            if len(self.starsLst) != 0:
                for star in self.starsLst:
                    # print(star, star.show)
                    if star.show:
                        #print("draw star")
                        self.stars.draw(screen)
                    #print(star.x, star.y)
                #print(self.player.x, self.player.y)     
            #pygame.display.update()
            '''
        pygame.display.update()
        
    def timerFired(self, dt):
        if self.player.mode == "invincible":
            self.scrollSpeed = 30
        else:
            self.scrollSpeed = 3
        if not self.playerGroup.sprite.isAlive or (self.mode != "game") or self.isPaused:
            return
        if len(self.obstacles) != 0:
            for obstacle in self.obstacles:
                obstacle.scroll += self.scrollSpeed
        if len(self.coins) != 0:
            for coin in self.coins:
                coin.scroll += self.scrollSpeed
        #if len(self.stars) != 0:
           # for star in self.stars:
            #    star.scroll += self.scrollSpeed
        if len(self.itemBoxes) != 0:
            for itemBox in self.itemBoxes:
                itemBox.scroll += self.scrollSpeed
                
        # modified code inspired by: https://www.youtube.com/watch?v=PjgLeP0G5Yw
        self.bgX -= self.scrollSpeed
        self.bgX2 -= self.scrollSpeed
        if self.bgX < (self.bgWidth * -1):
            self.bgX = self.bgWidth
        elif self.bgX2 < (self.bgWidth * -1):
            self.bgX2 = self.bgWidth
    
        for obstacle in self.obstacles:
            obstacle.x -= self.scrollSpeed
        for coin in self.coins:
            coin.x -= self.scrollSpeed
        #for star in self.stars:
            #star.x -= self.scrollSpeed
        for itemBox in self.itemBoxes:
            itemBox.x -= self.scrollSpeed
            
        self.playerGroup.update(dt, self.isKeyPressed, self.width, self.height)
        self.obstacles.update(self.width, self.height)
        self.coins.update(self.width, self.height, self.player.x, self.player.y, self.player.mode)
        #self.stars.update(self.width, self.height)
        self.itemBoxes.update(self.width, self.height)
        #self.hitboxes.update(self.width, self.height)
        
        if self.player.bullet != None:
            self.bulletGroup = pygame.sprite.GroupSingle(self.player.bullet)
            self.player.bullet.update(self.width, self.height)

        if self.player.magnet != None:
            self.magnetGroup = pygame.sprite.GroupSingle(self.player.magnet)
            self.player.magnet.update(self.width, self.height, self.player.x, self.player.y)
        
        (boolObstacle, obstacle) = self.player.collide(self.obstacles)
        if self.player.mode != "invincible" and obstacle != None:
            self.player.isAlive = False
            #print(f"collide with obstacle {obstacle}")
            
        (boolCoin, coin) = self.player.collide(self.coins)
        if coin != None and not coin.hit:
            self.score += 1
            coin.hit = True
            coin.count = 0
            #print(f"collide with coin {coin}")

        (boolItemBox, itemBox) = self.player.collide(self.itemBoxes)
        if itemBox != None:
           #print("invincible mode entered")
            self.player.mode = itemBox.itemType
            #print(self.player.mode)
            self.player.count = 0
            itemBox.hit = True
            itemBox.kill()
            if self.player.mode == "magnet suit":
                self.player.magnet = Magnet(self.player.x, self.player.y)
        
    def keyPressed(self, keyCode, modifier):
        #print(keyCode)
        if keyCode == 114: #keyCode for "r" --> restart
            self.init()
            self.__init__(800, 390)
        elif keyCode == 112: #keyCode for "p" --> pause
            self.isPaused = not self.isPaused
        elif keyCode == 32 and (self.player.mode == "fly"): #keyCode for the space bar
            self.player.mode = "attack"
            self.player.count = 0
            self.player.bullet = Bullets(self.player.x, self.player.y)
            #print("space pressed", self.player.count)
            
Game(800, 390).run()
