# modified code taken from: http://blog.lukasperaza.com/getting-started-with-pygame/
import pygame
import random
from Player import Player
from Obstacles import Obstacles
from Coins import Coins
#from Hitboxes import Hitboxes
#from Stars import Stars
from ItemBoxes import ItemBoxes
from Rockets import Rockets
from pygame.locals import *
from WarningSigns import WarningSigns
from Lasers import Lasers
from LasersPrep import LasersPrep

class PygameGame(object):

    def init(self):
        Obstacles.init()
        self.obstacles = pygame.sprite.Group()
        pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(2000, 3500))
        Player.init()
        self.player = Player(self.width / 2, self.height / 2)
        self.playerGroup = pygame.sprite.GroupSingle(self.player)
        self.bulletGroup = pygame.sprite.Group()
        self.magnetGroup = pygame.sprite.GroupSingle(self.player.magnet)
        Coins.init()
        self.coins = pygame.sprite.Group()
        self.itemBoxes = pygame.sprite.Group()
        Rockets.init()
        self.rockets = pygame.sprite.Group()
        WarningSigns.init()
        self.warningSigns = pygame.sprite.Group()
        Lasers.init()
        self.lasers = pygame.sprite.Group()
        LasersPrep.init()
        self.lasersPrep = pygame.sprite.Group()
        
    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=400, fps=60, title="112 Jetpack Joyride"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.mode = "start"
        self.isPaused = False
        
        self.obstaclesLst = []
        #self.obstacleHitboxes = []
        
        self.coinsLst = []
        #self.coinsHitboxes = []
        
        #self.starsLst = []
        
        self.itemBoxesLst = []
        #self.itemBoxesHitBoxes = []

        self.rocketsLst = []
        self.warningSignsLst = []

        self.lasersLst = []
        self.lasersPrepLst = []
        
        self.objects = set()
        pygame.init()
    
    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        screen.set_alpha(None)
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.mode = "game"
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.USEREVENT+1:
                    if len(self.obstaclesLst) == 0:
                        x = random.randint(self.width, self.width * 2)
                        y = random.randint(50, self.height - 50)
                    else:
                        maxX = 0
                        for obstacle in self.obstaclesLst:
                            prevX, prevY = obstacle.x, obstacle.y
                            if prevX > maxX:
                                maxX = int(prevX)
                        x = random.randint(max(self.width / 2 + self.player.x,
                                               maxX + 300),
                                           max(self.width / 2 + self.player.x,
                                               maxX + 700))
                        y = random.randint(50, self.height - 50)
                    currentObstacle = Obstacles(x, y)
                    add = True
                    for obj in self.objects:
                        if currentObstacle.collide(obj):
                            add = False
                    if add:
                        self.obstaclesLst.append(currentObstacle)
                        self.obstacles.add(currentObstacle)
                        #self.obstacleHitboxes.append(currentObstacle.hitbox)
                        self.objects.add(currentObstacle)
                elif event.type == pygame.USEREVENT+2:
                    startX = 0
                    if len(self.coinsLst) == 0:
                        startX = random.randint(self.width, self.width * 2)
                    else:
                        maxX = 0
                        for coin in self.coinsLst:
                            if not coin.isVisible:
                                prevX, prevY = coin.x, coin.y
                                if prevX > maxX:
                                    maxX = int(prevX)
                        startX = random.randint(max(self.width / 2 + self.player.x,
                                                   maxX + 200),
                                               max(self.width / 2 + self.player.x,
                                                   maxX + 300))
                    y = random.randint(50, self.height - 50)
                    coinShape = random.choice(["lines", "heart"])
                    newCoins = []
                    if coinShape == "lines":
                        #print(Coins.lines)
                        for (xcor, ycor) in Coins.lines:
                            #print("coin created")
                            newCoin = Coins(startX + xcor, y + ycor)
                            newCoins.append(newCoin)
                    elif coinShape == "heart":
                        for (xcor, ycor) in Coins.heart:
                            #print("coin created")
                            newCoin = Coins(startX + xcor, y + ycor)
                            newCoins.append(newCoin)
                    add = True
                    for coin in newCoins:
                        for obj in self.objects:
                            if coin.collide(obj):
                                add = False
                    if add:
                        for coin in newCoins:
                            #print("coins added")
                            self.coinsLst.append(coin)
                            self.coins.add(coin)
                            #self.coinsHitboxes.append(coin.hitbox)
                            self.objects.add(coin)
                elif event.type == pygame.USEREVENT+3:
                    if len(self.itemBoxesLst) == 0:
                        x = random.randint(self.width, self.width * 2)
                        y = random.randint(50, self.height - 50)
                    else:
                        maxX = 0
                        for itemBox in self.itemBoxesLst:
                            prevX, prevY = itemBox.x, itemBox.y
                            if prevX > maxX:
                                maxX = int(prevX)
                        x = random.randint(max(self.width / 2 + self.player.x,
                                               maxX + 200),
                                           max(self.width / 2 + self.player.x,
                                               maxX + 300))
                        y = random.randint(50, self.height - 50)
                    itemType = random.choice(["invincible", "magnet suit"])
                    currentItemBox = ItemBoxes(x, y, itemType)
                    add = True
                    for obj in self.objects:
                        if currentItemBox.collide(obj):
                            add = False
                    if add:
                        self.itemBoxesLst.append(currentItemBox)
                        self.itemBoxes.add(currentItemBox)
                        #self.itemBoxesHitBoxes.append(currentItemBox.hitbox)
                        self.objects.add(currentItemBox)
                elif event.type == pygame.USEREVENT+4:
                    x = self.width * 3
                    y = random.randint(50, self.height - 50)
                    currentRocket = Rockets(x, y)
                    add = True
                    for laser in self.lasers:
                        if abs(currentRocket.x - laser.x) < 10:
                            add = False
                    if add:
                        self.rockets.add(currentRocket)
                        self.rocketsLst.append(currentRocket)
                        currentWarningSign = WarningSigns(self.width - 30, y)
                        self.warningSigns.add(currentWarningSign)
                        self.warningSignsLst.append(currentWarningSign)

                elif event.type == pygame.USEREVENT+5:
                    x = self.player.x
                    y = random.randint(50, self.height - 50)
                    currentLaser = Lasers(x, y)
                    add = True
                    for rocket in self.rockets:
                        if abs(currentLaser.x - rocket.x) < 10:
                            add = False
                    if add:
                        self.lasers.add(currentLaser)
                        self.lasersLst.append(currentLaser)
                        prepX1 = x - 340
                        prepX2 = x + 340
                        currentLasersPrep1 = LasersPrep(prepX1, y)
                        currentLasersPrep2 = LasersPrep(prepX2, y)
                        self.lasersPrep.add(currentLasersPrep1)
                        self.lasersPrep.add(currentLasersPrep2)
                        self.lasersPrepLst.append(currentLasersPrep1)
                        self.lasersPrepLst.append(currentLasersPrep2)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
