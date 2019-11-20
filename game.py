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
        self.bgWidth = self.bg.get_width()
        self.bgX = 0
        self.bgX2 = self.bgWidth
        #self.clock = pygame.time.Clock()
        self.scrollSpeed = 1.5
        #self.lasers = []

        #Laser.in it()
        #self.lasers = pygame.sprite.Group()
        pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(4000, 5500))
        
    def redrawAll(self, screen):
        if not self.playerGroup.sprite.isAlive:
            #screen.blit(self.bg, (self.bgX, 0))
            #screen.blit(self.bg, (self.bgX2, 0))
            screen.fill((0, 0, 0))
            font = pygame.font.Font("Amatic-Bold.ttf", 50)
            text = font.render('GAME OVER', True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (self.width / 2, self.height / 2)
            screen.blit(text, textRect)
            pygame.display.update()
            return
        
        screen.blit(self.bg, (self.bgX, 0))
        screen.blit(self.bg, (self.bgX2, 0))
        #self.timerFired()
        self.playerGroup.draw(screen)
        self.lasers.draw(screen)
        pygame.display.update()

    def timerFired(self, dt):
        if not self.playerGroup.sprite.isAlive:
            return
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

    
Game(800, 390).run()
