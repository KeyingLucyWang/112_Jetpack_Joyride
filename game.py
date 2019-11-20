import pygame
import random
from pygamegame import PygameGame
from Player import Player
from Laser import Laser
  
class Game(PygameGame):
    def init(self):
        super().init()
        Player.init()
        player = Player(self.width / 2, self.height / 2)
        self.playerGroup = pygame.sprite.GroupSingle(player)
        self.bg = pygame.image.load("mountain.png")
        #self.bg = pygame.transform.scale(self.bg, (400, 400))
        self.bgWidth = self.bg.get_width()
        self.bgX = 0
        self.bgX2 = self.bgWidth
        #self.clock = pygame.time.Clock()
        self.scrollSpeed = 3
        #self.lasers = []
        self.isPaused = False
        #Laser.in it()
        #self.lasers = pygame.sprite.Group()
        pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(4000, 5500))

    def redrawAll(self, screen):
        if not self.playerGroup.sprite.isAlive:
            screen.fill((0, 0, 0))
            font = pygame.font.Font("Amatic-Bold.ttf", 50)
            text = font.render('GAME OVER', True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (self.width / 2, self.height / 2)
            screen.blit(text, textRect)
            pygame.display.update()
            return
        
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

        if self.isPaused:
            screen.fill((255, 255, 255))
            pauseFont = pygame.font.Font("Amatic-Bold.ttf", 50)
            pause = pauseFont.render('GAME PAUSED', True, (0, 0, 0))
            pauseIns = pauseFont.render('Hit "p" to unpause', True, (0, 0, 0))
            pauseRect = pause.get_rect()
            pauseRect.center = (self.width / 2, self.height / 2 - 70)
            pauseInsRect = pauseIns.get_rect()
            pauseInsRect.center = (self.width / 2, self.height / 2)
            screen.blit(pause, pauseRect)
            screen.blit(pauseIns, pauseInsRect)
            
        elif self.mode == "game": 
            screen.blit(self.bg, (self.bgX, 0))
            screen.blit(self.bg, (self.bgX2, 0))
            #self.timerFired()
            self.playerGroup.draw(screen)
            self.lasers.draw(screen)
            pygame.display.update()

        pygame.display.update()
        
    def timerFired(self, dt):
        if not self.playerGroup.sprite.isAlive or (self.mode != "game") or self.isPaused:
            return
        # modified code inspired by: https://www.youtube.com/watch?v=PjgLeP0G5Yw
        self.bgX -= self.scrollSpeed
        self.bgX2 -= self.scrollSpeed
        if self.bgX < (self.bgWidth * -1):
            self.bgX = self.bgWidth
        elif self.bgX2 < (self.bgWidth * -1):
            self.bgX2 = self.bgWidth
        for laser in self.lasers:
            laser.x -= self.scrollSpeed
        self.playerGroup.update(dt, self.isKeyPressed, self.width, self.height)
        self.lasers.update(self.width, self.height)

    def keyPressed(self, keyCode, modifier):
        #print(keyCode)
        if keyCode == 114: #keyCode for "r" --> restart
            self.init()
        elif keyCode == 112: #keyCode for "p" --> pause
            self.isPaused = not self.isPaused
    
Game(800, 390).run()
