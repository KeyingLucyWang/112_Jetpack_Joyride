# modified code taken from: http://blog.lukasperaza.com/getting-started-with-pygame/
import pygame
import random
import os
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
from Bullets import Bullets

class PygameGame(object):

    def init(self):
        Obstacles.init()
        self.obstacles = pygame.sprite.Group()
        #pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(2000, 3500))
        Player.init()
        self.player = Player(self.width / 2, self.height / 2)
        self.playerGroup = pygame.sprite.GroupSingle(self.player)
        Bullets.init()
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

        # initialize user text file
        #self.loginText = open("loginText.txt","a+")
        #self.loginText.close()
        self.userFile = None
        self.userName = ""
        self.passWord = ""
        self.isTypingName = True
        self.isTypingPW = True
        self.recorded = False
        self.printInvalidUserIns = False
        self.printErrorIns = False
        self.userExist = False
        self.registerSuccessful = False
        self.moneyRecorded = False
        self.insufficientCoins = False
        self.bulletRecorded = False
        self.printNewRecord = False
        self.gamePlayed = False
        
        # score board
        self.highScores = dict()
        self.scoreLst = []
        self.name1 = ""
        self.score1 = None
        self.name2 = ""
        self.score2 = None
        self.name3 = ""
        self.score3 = None
        self.scoreFile = None
        self.scoreFile = open("scoreBoard.txt", "r")
        contents = self.scoreFile.read()
        print(contents)
        numScores = len(contents.splitlines())
        print(numScores)
        if numScores == 1 and contents.splitlines()[0] != ",":
            self.name1 = (contents.splitlines()[0].split(","))[0]
            self.score1 = int((contents.splitlines()[0].split(","))[1])
            self.highScores[self.name1] = self.score1
        elif numScores == 2:
            if contents.splitlines()[0] != ",":
                self.name1 = (contents.splitlines()[0].split(","))[0]
                self.score1 = int((contents.splitlines()[0].split(","))[1])
            if contents.splitlines()[1] != ",":
                self.name2 = (contents.splitlines()[1].split(","))[0]
                self.score2 = int((contents.splitlines()[1].split(","))[1])
            self.highScores[self.name1] = self.score1
            self.highScores[self.name2] = self.score2
        elif numScores == 3:
            if contents.splitlines()[0] != ",":
                self.name1 = (contents.splitlines()[0].split(","))[0]
                self.score1 = int((contents.splitlines()[0].split(","))[1])
            if contents.splitlines()[1] != ",":
                self.name2 = (contents.splitlines()[1].split(","))[0]
                self.score2 = int((contents.splitlines()[1].split(","))[1])
            if contents.splitlines()[2] != ",":
                self.name3 = (contents.splitlines()[2].split(","))[0]
                self.score3 = int((contents.splitlines()[2].split(","))[1])
            self.highScores[self.name1] = self.score1
            self.highScores[self.name2] = self.score2
            self.highScores[self.name3] = self.score3
        print(f"{self.name1},{self.score1}")
        print(f"{self.name2},{self.score2}")
        print(f"{self.name3},{self.score3}")
        print(self.highScores)
        self.scoreFile.close()
        
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
                    '''
                    if (self.mode == "start" and event.key == pygame.K_SPACE) or (self.mode == "login" and event.key == pygame.K_SPACE):
                        self.mode = "register"
                        self.userName = ""
                        self.passWord= ""
                        self.isTypingName = True
                        self.isTypingPW = True
                        self.userExist = False
                        self.registerSuccessful = False
                    elif (self.mode == "start" and event.key == pygame.K_ESCAPE) or (self.mode == "register" and event.key == pygame.K_SPACE):
                        self.mode = "login"
                        self.printInvalidUserIns = False
                        self.printErrorIns = False
                        self.isTypingName = True
                        self.isTypingPW = True
                        self.userName = ""
                        self.passWord= ""
                    '''
                    # shortcut to profile mode
                    #if self.mode == "start" and event.key == pygame.K_SPACE:
                    #    self.mode = "profile"
                    #if self.mode == "profile" and event.key == pygame.K_s:
                        #print("enter game mode")
                        #self.mode = "game"
                    #if self.mode == "start" and (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT):
                        #print("enter game mode")
                        #self.mode = "game"
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                    if self.isTypingName:
                        self.userExist = False
                        self.printInvalidUserIns = False
                        if event.key == pygame.K_a:
                            self.userName = self.userName + "a"
                        if event.key == pygame.K_b:
                            self.userName = self.userName + "b"
                        if event.key == pygame.K_c:
                            self.userName = self.userName + "c"
                        if event.key == pygame.K_d:
                            self.userName = self.userName + "d"
                        if event.key == pygame.K_e:
                            self.userName = self.userName + "e"
                        if event.key == pygame.K_f:
                            self.userName = self.userName + "f"
                        if event.key == pygame.K_g:
                            self.userName = self.userName + "g"
                        if event.key == pygame.K_h:
                            self.userName = self.userName + "h"
                        if event.key == pygame.K_i:
                            self.userName = self.userName + "i"
                        if event.key == pygame.K_j:
                            self.userName = self.userName + "j"
                        if event.key == pygame.K_k:
                            self.userName = self.userName + "k"
                        if event.key == pygame.K_l:
                            self.userName = self.userName + "l"
                        if event.key == pygame.K_m:
                            self.userName = self.userName + "m"
                        if event.key == pygame.K_n:
                            self.userName = self.userName + "n"
                        if event.key == pygame.K_o:
                            self.userName = self.userName + "o"
                        if event.key == pygame.K_p:
                            self.userName = self.userName + "p"
                        if event.key == pygame.K_q:
                            self.userName = self.userName + "q"
                        if event.key == pygame.K_r:
                            self.userName = self.userName + "r"
                        if event.key == pygame.K_s:
                            self.userName = self.userName + "s"
                        if event.key == pygame.K_t:
                            self.userName = self.userName + "t"
                        if event.key == pygame.K_u:
                            self.userName = self.userName + "u"
                        if event.key == pygame.K_v:
                            self.userName = self.userName + "v"
                        if event.key == pygame.K_w:
                            self.userName = self.userName + "w"
                        if event.key == pygame.K_x:
                            self.userName = self.userName + "x"
                        if event.key == pygame.K_y:
                            self.userName = self.userName + "y"
                        if event.key == pygame.K_z:
                            self.userName = self.userName + "z"
                        if event.key == pygame.K_1:
                            self.userName = self.userName + "1"
                        if event.key == pygame.K_2:
                            self.userName = self.userName + "2"
                        if event.key == pygame.K_3:
                            self.userName = self.userName + "3"
                        if event.key == pygame.K_4:
                            self.userName = self.userName + "4"
                        if event.key == pygame.K_5:
                            self.userName = self.userName + "5"
                        if event.key == pygame.K_6:
                            self.userName = self.userName + "6"
                        if event.key == pygame.K_7:
                            self.userName = self.userName + "7"
                        if event.key == pygame.K_8:
                            self.userName = self.userName + "8"
                        if event.key == pygame.K_9:
                            self.userName = self.userName + "9"
                        if event.key == pygame.K_0:
                            self.userName = self.userName + "0"
                        if event.key == pygame.K_PERIOD:
                            self.userName = self.userName + "."
                        if event.key == pygame.K_BACKSPACE:
                            self.userName = self.userName[:-1]
                        if event.key == pygame.K_RETURN:
                            if self.mode == "register":
                                #self.loginText = open("loginText.txt", "r")
                                print(f'userLogin/{self.userName}.txt')
                                #cleared what was in the text file everytime it is opened
                                self.userFile = open(f'userLogin/{self.userName}.txt', "a+")
                                self.userFile.close()
                                self.userFile = open(f'userLogin/{self.userName}.txt', "r")
                                if self.userFile.mode == "r":
                                    print(f"userLogin/{self.userName}.txt")
                                    print(os.path.getsize(f"userLogin/{self.userName}.txt"))
                                    if os.path.getsize(f"userLogin/{self.userName}.txt") != 0:
                                        print("user exists")
                                        self.userExist = True
                                    else:
                                        self.userExist = False
                                        contents = self.userFile.read()
                                #if contents != None or contents.strip() != "":
                                    #print("user exists")
                                    #self.userExist = True
                                '''
                                for line in contents.splitlines():
                                    data = line.split(",")
                                    if self.userName == data[0]:
                                        print("user exists")
                                        self.userExist = True
                                '''
                            if not self.userExist:
                                print("type password")
                                self.isTypingName = False
                            else:
                                print("clear")
                                self.userName = ""
                            #self.userFile.close()
                            
                    elif self.isTypingPW:
                        if event.key == pygame.K_a:
                            self.passWord = self.passWord + "a"
                        if event.key == pygame.K_b:
                            self.passWord = self.passWord + "b"
                        if event.key == pygame.K_c:
                            self.passWord = self.passWord + "c"
                        if event.key == pygame.K_d:
                            self.passWord = self.passWord + "d"
                        if event.key == pygame.K_e:
                            self.passWord = self.passWord + "e"
                        if event.key == pygame.K_f:
                            self.passWord = self.passWord + "f"
                        if event.key == pygame.K_g:
                            self.passWord = self.passWord + "g"
                        if event.key == pygame.K_h:
                            self.passWord = self.passWord + "h"
                        if event.key == pygame.K_i:
                            self.passWord = self.passWord + "i"
                        if event.key == pygame.K_j:
                            self.passWord = self.passWord + "j"
                        if event.key == pygame.K_k:
                            self.passWord = self.passWord + "k"
                        if event.key == pygame.K_l:
                            self.passWord = self.passWord + "l"
                        if event.key == pygame.K_m:
                            self.passWord = self.passWord + "m"
                        if event.key == pygame.K_n:
                            self.passWord = self.passWord + "n"
                        if event.key == pygame.K_o:
                            self.passWord = self.passWord + "o"
                        if event.key == pygame.K_p:
                            self.passWord = self.passWord + "p"
                        if event.key == pygame.K_q:
                            self.passWord = self.passWord + "q"
                        if event.key == pygame.K_r:
                            self.passWord = self.passWord + "r"
                        if event.key == pygame.K_s:
                            self.passWord = self.passWord + "s"
                        if event.key == pygame.K_t:
                            self.passWord = self.passWord + "t"
                        if event.key == pygame.K_u:
                            self.passWord = self.passWord + "u"
                        if event.key == pygame.K_v:
                            self.passWord = self.passWord + "v"
                        if event.key == pygame.K_w:
                            self.passWord = self.passWord + "w"
                        if event.key == pygame.K_x:
                            self.passWord = self.passWord + "x"
                        if event.key == pygame.K_y:
                            self.passWord = self.passWord + "y"
                        if event.key == pygame.K_z:
                            self.passWord = self.passWord + "z"
                        if event.key == pygame.K_1:
                            self.passWord = self.passWord + "1"
                        if event.key == pygame.K_2:
                            self.passWord = self.passWord + "2"
                        if event.key == pygame.K_3:
                            self.passWord = self.passWord + "3"
                        if event.key == pygame.K_4:
                            self.passWord = self.passWord + "4"
                        if event.key == pygame.K_5:
                            self.passWord = self.passWord + "5"
                        if event.key == pygame.K_6:
                            self.passWord = self.passWord + "6"
                        if event.key == pygame.K_7:
                            self.passWord = self.passWord + "7"
                        if event.key == pygame.K_8:
                            self.passWord = self.passWord + "8"
                        if event.key == pygame.K_9:
                            self.passWord = self.passWord + "9"
                        if event.key == pygame.K_0:
                            self.passWord = self.passWord + "0"
                        if event.key == pygame.K_BACKSPACE:
                            self.passWord = self.passWord[:-1]
                        if event.key == pygame.K_RETURN:
                            self.isTypingPW = False
                            
                    if self.mode == "register" and not self.isTypingPW and not self.isTypingName and not self.recorded:
                        #self.userFile = open(f'userLogin/{self.userName}.txt', "r+")
                        #if self.userFile.mode == "r+":
                        #    contents = self.userFile.read()
                        #if self.userFile != None and self.userFile != "":
                        #    print("user exists")
                        #    self.userExist = True
                        #else:
                        #    self.userExist = False
                        #self.userFile.close()
                        '''
                        self.loginText = open("loginText.txt", "r")
                        if self.loginText.mode == "r":
                            contents = self.loginText.read()
                        for line in contents.splitlines():
                            data = line.split(",")
                            if self.userName == data[0]:
                                print("user exists")
                                self.userExist = True
                        '''
                        if not self.userExist:
                            #self.loginText = open("loginText.txt", "a+")
                            self.userFile = open(f'userLogin/{self.userName}.txt', "a+")
                            #self.loginText.write(f"{self.userName},{self.passWord}\r\n")
                            self.userFile.write(f'{self.passWord}\r\n')
                            self.userFile.write('0\r\n')
                            self.userFile.write('0\r\n')
                            self.userFile.write('0\r\n')
                            #self.loginText.close()
                            self.userFile.close()
                            self.recorded = True
                            print("recorded")
                            self.registerSuccessful = True
                        self.userName = ""
                        self.passWord= ""

                    if self.mode == "login" and not self.isTypingName: #and not self.isTypingPW:
                        #self.loginText = open("loginText.txt", "r")
                        self.userFile = open(f'userLogin/{self.userName}.txt', 'a+')
                        self.userFile.close()
                        self.userFile = open(f'userLogin/{self.userName}.txt', 'r')
                        if self.userFile.mode == "r":
                            print("enter read")
                            if os.path.getsize(f'userLogin/{self.userName}.txt') == 0:
                                print("user not found")
                                self.printInvalidUserIns = True
                                self.userName = ""
                                self.passWord = ""
                                self.isTypingName = True
                        #if contents == None or contents == "":
                            #print("user not found")
                            #self.printInvalidUserIns = True
                            #self.userName = ""
                            #self.passWord = ""
                            #self.mode = "register"
                            elif not self.isTypingPW:
                                contents = self.userFile.read()
                                #print(contents)
                                #for line in contents.splitlines():
                                line = contents.splitlines()[0]
                                if self.passWord == line.strip():
                                    print("profile mode")
                                    print(int(contents.splitlines()[1]))
                                    self.money = int(contents.splitlines()[1])
                                    self.numBullets = int(contents.splitlines()[2])
                                    self.highestScore = int(contents.splitlines()[3])
                                    self.mode = "profile"
                                    print(self.name2, self.score2 ,self.score)
                                else:
                                    self.printErrorIns = True
                                    self.passWord = ""
                                    self.isTypingPW = True
                        self.userFile.close()
                        '''
                        pw = ""
                        for line in contents.splitlines():
                            data = line.split(",")
                            print(data)
                            #print(data[0], data[1])
                            if self.userName == data[0]:
                                pw = data[1]
                        if pw == "":
                            print("user not found")
                            self.printInvalidUserIns = True
                            self.userName = ""
                            self.passWord = ""
                            #self.mode = "register"
                        else:
                            if self.passWord == pw:
                                print("profile mode")
                                self.mode = "profile"
                            else:
                                self.printErrorIns = True
                                self.passWord = ""
                                self.isTypingPW = True
                        self.loginText.close()
                    '''
                    #if not self.isTypingName:
                    #    print("userName", self.userName)
                    #if not self.isTypingPW:
                    #    print("PW", self.passWord)
                elif event.type == pygame.QUIT:
                    playing = False
                elif not self.isPaused and self.mode == "game" and event.type == pygame.USEREVENT+1:
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
                elif not self.isPaused and self.mode == "game" and event.type == pygame.USEREVENT+2:
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
                elif not self.isPaused and self.mode == "game" and event.type == pygame.USEREVENT+3:
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
                elif not self.isPaused and self.mode == "game" and event.type == pygame.USEREVENT+4 and self.score >= 800:
                    x = self.width * 3
                    y = random.randint(50, self.height - 50)
                    currentRocket = Rockets(x, y)
                    add = True
                    for laser in self.lasers:
                        if abs(currentRocket.y - laser.y) < 10:
                            add = False
                    if add:
                        self.rockets.add(currentRocket)
                        self.rocketsLst.append(currentRocket)
                        currentWarningSign = WarningSigns(self.width - 30, y)
                        self.warningSigns.add(currentWarningSign)
                        self.warningSignsLst.append(currentWarningSign)

                elif not self.isPaused and self.mode == "game" and event.type == pygame.USEREVENT+5 and self.score >= 500:
                    x = self.player.x
                    y = random.randint(50, self.height - 50)
                    currentLaser = Lasers(x, y)
                    add = True
                    for rocket in self.rockets:
                        if abs(currentLaser.y - rocket.y) < 10:
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
    
                if not self.player.isAlive and not self.moneyRecorded:
                    print("recorded")
                    self.document()
                    self.gamePlayed = True
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()

    def document(self):
        self.userFile = open(f'userLogin/{self.userName}.txt', 'r')
        contents = self.userFile.read()
        currentPW = contents.splitlines()[0].strip()
        print(currentPW)
        currentCoins = self.score // 10                
        totalCoins = currentCoins + self.money               
        print(totalCoins)
        self.money = totalCoins
        currentHighScore = int(contents.splitlines()[3].strip())
        self.userFile.close()
        self.userFile = open(f'userLogin/{self.userName}.txt', 'a+')
        self.userFile.seek(0)
        self.userFile.truncate()
        self.userFile.write(f'{currentPW}\r\n')
        self.userFile.write(f'{totalCoins}\r\n')
        self.userFile.write(f'{self.numBullets}\r\n')
        if self.score > currentHighScore:
            self.printNewRecord = True
            self.highestScore = self.score
            print(self.highestScore)
        self.userFile.write(f'{self.highestScore}\r\n')
        self.userFile.close()
        deletePlayer = None
        recorded = False
        for player in self.highScores:
            # if user is already on the score board
            if player == self.userName:
                if self.highScores[player] < self.score:
                    self.highScores[player] = self.score
                    recorded = True
                    print("record",self.highScores)
                else:
                    recorded = True
        for player in self.highScores:
            if self.highScores[player] < self.score and not recorded:
                self.highScores[self.userName] = self.score
                recorded = True
                deletePlayer = player
                print("replaced", self.highScores)
        if len(self.highScores) < 3 and not recorded:
            self.highScores[self.userName] = self.score
            print("added", self.highScores)
        if deletePlayer != None:
            del self.highScores[deletePlayer]
        '''
        if self.score3 != "" and self.userName != self.name2 and self.userName != self.name1: #and self.userName != self.name3
            if self.score > self.score3:
                if self.score > self.score2:
                    if self.score > self.score1:
                        self.score3 = self.score2
                        self.name3 = self.name2
                        self.score2 = self.score1
                        self.name2 = self.name1
                        self.score1 = self.score
                        self.name1 = self.userName
                    else:
                        self.score3 = self.score2
                        self.name3 = self.name2
                        self.score2 = self.score
                        self.name2 = self.userName
                elif self.userName != self.score3:
                    self.score3 = self.score
                    self.name3 = self.userName
        elif self.score2 != "" and self.userName != self.name1: #and self.userName != self.name2
            if self.score > self.score2:
                if self.score > self.score1:
                    self.score3 = self.score2
                    self.name3 = self.name2
                    self.score2 = self.score1
                    self.name2 = self.name1
                    self.score1 = self.score
                    self.name1 = self.userName
                else:
                    self.score3 = self.score2
                    self.name3 = self.name2
                    self.score2 = self.score
                    self.name2 = self.userName
            elif self.userName != self.name2:
                self.score3 = self.score
                self.name3 = self.userName
        elif self.score1 != "" and self.userName != self.name1:
            if self.score > self.score1:
                self.score2 = self.score1
                self.name2 = self.name1
                self.score1 = self.score
                self.name1 = self.userName
            else:
                self.score2 = self.score
                self.name2 = self.userName
        elif self.userName != self.name1 or (self.userName == self.name1 and self.score > self.score1):
            self.score1 = self.score
            self.name1 = self.userName
        elif self.userName == self.name2 and self.score > self.score2:
            self.score2 = self.score
        elif self.userName == self.name3 and self.score > self.score3:
            self.score3 = self.score
        '''
        print(self.userName, self.score)
        self.scoreFile = open('scoreBoard.txt', "a")
        self.scoreFile.seek(0)
        self.scoreFile.truncate()
        # order the players based on their scores
        print(len(self.highScores))
        self.scoreLst = []
        for name in self.highScores:
            self.scoreLst.append(self.highScores[name])
        print(self.scoreLst)
        self.scoreLst.sort()
        self.scoreLst.reverse()
        print("sorted", self.scoreLst)
        if len(self.scoreLst) > 0:
            self.score1 = self.scoreLst[0]
            if len(self.scoreLst) > 1:
                self.score2 = self.scoreLst[1]
                if len(self.scoreLst) > 2:
                    self.score3 = self.scoreLst[2]
        for name in self.highScores:
            if self.highScores[name] == self.score1:
                self.name1 = name
            elif self.highScores[name] == self.score2:
                self.name2 = name
            elif self.highScores[name] == self.score3:
                self.name3 = name
        if self.name1 != "" and self.score1 != None:
            self.scoreFile.write(f'{self.name1},{self.score1}\r\n')
        if self.name2 != "" and self.score2 != None:
            self.scoreFile.write(f'{self.name2},{self.score2}\r\n')
        if self.name3 != "" and self.score3 != None:
            self.scoreFile.write(f'{self.name3},{self.score3}\r\n')
        self.scoreFile.close()
        '''
        self.scoreFile = open(f'scoreBoard.txt', 'r')
        scoreContents = self.scoreFile.read()
        numScores = len(contents.splitlines())
        if numScores == 1:
            self.name1 = (contents.splitlines()[0].split(","))[0]
            self.score1 = (contents.splitlines()[0].split(","))[1]
        elif numScores == 2:
            self.name1 = (contents.splitlines()[0].split(","))[0]
            self.score1 = (contents.splitlines()[0].split(","))[1]
            self.name2 = (contents.splitlines()[1].split(","))[0]
            self.score2 = (contents.splitlines()[1].split(","))[1]
        elif numScores == 3:
            self.name1 = (contents.splitlines()[0].split(","))[0]
            self.score1 = (contents.splitlines()[0].split(","))[1]
            self.name2 = (contents.splitlines()[1].split(","))[0]
            self.score2 = (contents.splitlines()[1].split(","))[1]
            self.name3 = (contents.splitlines()[2].split(","))[0]
            self.score3 = (contents.splitlines()[2].split(","))[1]
        '''
        self.moneyRecorded = True

def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
