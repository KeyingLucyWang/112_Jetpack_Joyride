import pygame
import random
from pygamegame import PygameGame
from Player import Player
from Obstacles import Obstacles
from Hitboxes import Hitboxes
from Coins import Coins
from Bullets import Bullets
from Stars import Stars

class Game(PygameGame):
    def init(self):
        super().init()
        #Player.init()
        #player = Player(self.width / 2, self.height / 2)
        #self.playerGroup = pygame.sprite.GroupSingle(player)
        self.bg = pygame.image.load("mountain.png")
        #self.bg = pygame.transform.scale(self.bg, (400, 400))
        self.bgWidth = self.bg.get_width()
        self.bgX = 0
        self.bgX2 = self.bgWidth
        #self.clock = pygame.time.Clock()
        self.scrollSpeed = 3
        #self.lasers = []
        self.isPaused = False
        self.score = 0
        #self.lasers = pygame.sprite.Group()
        pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(4000, 5500)) # random obstacles event
        pygame.time.set_timer(pygame.USEREVENT+2, random.randrange(10000, 20000)) # random coins event

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
            
        elif self.mode == "game": 
            screen.blit(self.bg, (self.bgX, 0))
            screen.blit(self.bg, (self.bgX2, 0))
            self.playerGroup.draw(screen)
            self.obstacles.draw(screen)
            #print(self.stars)
            self.coins.draw(screen)
            if self.player.bullet != None and self.player.bullet.distanceTraveled <= 300:
                #print("obstacle", self.obstaclesLst[0].x)
                #print("player", self.player.x, self.player.y)
                #print(self.player.bullet.x, self.player.bullet.y)
                self.bulletGroup.draw(screen)
            if len(self.starsLst) != 0:
                for star in self.starsLst:
                    # print(star, star.show)
                    if star.show:
                        #print("draw star")
                        self.stars.draw(screen)
                    #print(star.x, star.y)
                #print(self.player.x, self.player.y)     
            #for hitbox in self.hitboxes:
                #hitbox.draw(screen)
            #pygame.display.update()

        pygame.display.update()
        
    def timerFired(self, dt):
        if not self.playerGroup.sprite.isAlive or (self.mode != "game") or self.isPaused:
            return
        # modified code inspired by: https://www.youtube.com/watch?v=PjgLeP0G5Yw
        if len(self.obstacles) != 0:
            for obstacle in self.obstacles:
                obstacle.scroll += self.scrollSpeed
        if len(self.coins) != 0:
            for coin in self.coins:
                coin.scroll += self.scrollSpeed
        if len(self.stars) != 0:
            for star in self.stars:
                star.scroll += self.scrollSpeed
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
        for star in self.stars:
            star.x -= self.scrollSpeed
        self.playerGroup.update(dt, self.isKeyPressed, self.width, self.height)
        self.obstacles.update(self.width, self.height)
        self.coins.update(self.width, self.height)
        self.stars.update(self.width, self.height)
        if self.player.bullet != None:
            self.bulletGroup = pygame.sprite.GroupSingle(self.player.bullet)
            self.player.bullet.update(self.width, self.height)
        (boolObstacle, obstacle) = self.player.collide(self.obstacles)
        #print(bools)
        if obstacle != None:
            self.player.isAlive = False
            #print(f"collide with obstacle {obstacle}")
        (boolCoin, coin) = self.player.collide(self.coins)
        if coin != None:
            self.score += 1
            coin.hit = True
            #print("turn true", coin.star.show)
            coin.star.show = True
            #self.stars.add(coin.star)
            #self.starsLst.append(coin.star)
            coin.kill()
            #print(f"collide with coin {coin}")
        
    def keyPressed(self, keyCode, modifier):
        #print(keyCode)
        if keyCode == 114: #keyCode for "r" --> restart
            self.init()
        elif keyCode == 112: #keyCode for "p" --> pause
            self.isPaused = not self.isPaused
        elif keyCode == 32 and (self.player.mode == "fly"): #keyCode for the space bar
            self.player.mode = "attack"
            self.player.count = 0
            self.player.bullet = Bullets(self.player.x, self.player.y)
            #print("space pressed", self.player.count)
            
Game(800, 390).run()
