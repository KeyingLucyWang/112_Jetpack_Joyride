import pygame
import random
from pygamegame import PygameGame
from Player import Player
from Obstacles import Obstacles
#from Hitboxes import Hitboxes
from Coins import Coins
from Bullets import Bullets
#from Stars import Stars
from ItemBoxes import ItemBoxes
from Rockets import Rockets
from Magnet import Magnet
from WarningSigns import WarningSigns

class Game(PygameGame):
    def init(self):
        super().init()
        # image taken from: https://opengameart.org/sites/default/files/Free-Horizontal-2D-Game-Backgrounds-3.jpg
        self.bg = pygame.image.load("mountain.png")
        self.bgWidth = self.bg.get_width()
        self.bgX = 0
        self.bgX2 = self.bgWidth
        #self.clock = pygame.time.Clock()
        self.scrollSpeed = 3
        self.oriScrollSpeed = self.scrollSpeed
        self.score = 0
        pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(4000, 6000)) # random obstacles event
        pygame.time.set_timer(pygame.USEREVENT+2, random.randrange(2000, 5000)) # random coins event
        pygame.time.set_timer(pygame.USEREVENT+3, random.randrange(12000, 15000))# random item boxes event
        pygame.time.set_timer(pygame.USEREVENT+4, random.randrange(15000, 20000)) # random rockets event
        pygame.time.set_timer(pygame.USEREVENT+5, random.randrange(9000, 10000))
        
    def redrawAll(self, screen):
        # text font from: https://www.fontsquirrel.com/fonts/amatic
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

        if self.mode == "register":
            screen.fill((0, 0, 0))
            if self.userExist or self.registerSuccessful:
                textFont = pygame.font.SysFont("comicsansms", 20)
                if self.userExist:
                    text = textFont.render("Username already exists. Choose another username or log in.", True, (255, 255, 255))
                elif self.registerSuccessful:
                    text = textFont.render("Register successful. Press SPACE to log in.", True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (self.width / 2, self.height / 2 - 40)
                screen.blit(text, textRect)
            modeFont = pygame.font.SysFont("comicsansms", 30)
            mode = modeFont.render("REGISTER", True, (255, 255, 255))
            modeRect = mode.get_rect()
            modeRect.center = (self.width / 2, self.height / 2 - 70)
            screen.blit(mode, modeRect)
            if not self.registerSuccessful:
                textFont = pygame.font.SysFont("comicsansms", 20)
                prompt = textFont.render("Please type in your username and password. Press enter to confirm.", True, (255, 255, 255))
                promptRect = prompt.get_rect()
                promptRect.center = (self.width / 2, self.height / 2 - 20)
                screen.blit(prompt, promptRect)
                nameFont = pygame.font.SysFont("comicsansms", 20)
                userName = nameFont.render(f'Username: {self.userName}', True, (255, 255, 255))
                nameRect = userName.get_rect()
                nameRect.center = (self.width / 2, self.height / 2)
                screen.blit(userName, nameRect)
                pwFont = pygame.font.SysFont("comicsansms", 20)
                password = pwFont.render(f'Password: {self.passWord}', True, (255, 255, 255))
                pwRect = password.get_rect()
                pwRect.center = (self.width / 2, self.height / 2 + 20)
                screen.blit(password, pwRect)

        # login screen
        if self.mode == "login":
            screen.fill((0, 0, 0))
            if self.printInvalidUserIns:
                font = pygame.font.SysFont("comicsansms", 20)
                text = font.render("Username not found. Press SPACE to register", True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (self.width / 2, self.height / 2 - 40)
                screen.blit(text, textRect)
            elif self.printErrorIns:
                font = pygame.font.SysFont("comicsansms", 20)
                text = font.render("Password incorrect. Login failed. Please re-enter the password", True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (self.width / 2, self.height / 2 - 40)
                screen.blit(text, textRect)
            modeFont = pygame.font.SysFont("comicsansms", 30)
            mode = modeFont.render("LOGIN", True, (255, 255, 255))
            modeRect = mode.get_rect()
            modeRect.center = (self.width / 2, self.height / 2 - 70)
            screen.blit(mode, modeRect)
            textFont = pygame.font.SysFont("comicsansms", 20)
            prompt = textFont.render("Please type in your username and password. Press enter to confirm.", True, (255, 255, 255))
            promptRect = prompt.get_rect()
            promptRect.center = (self.width / 2, self.height / 2 - 20)
            screen.blit(prompt, promptRect)
            nameFont = pygame.font.SysFont("comicsansms", 20)
            userName = nameFont.render(f'Username: {self.userName}', True, (255, 255, 255))
            nameRect = userName.get_rect()
            nameRect.center = (self.width / 2, self.height / 2)
            screen.blit(userName, nameRect)
            pwFont = pygame.font.SysFont("comicsansms", 20)
            password = pwFont.render(f'Password: {self.passWord}', True, (255, 255, 255))
            pwRect = password.get_rect()
            pwRect.center = (self.width / 2, self.height / 2 + 20)
            screen.blit(password, pwRect)
    
        if self.mode == "profile":
            screen.fill((0, 0, 0))
            modeFont = pygame.font.SysFont("comicsansms", 30)
            mode = modeFont.render("PROFILE", True, (255, 255, 255))
            modeRect = mode.get_rect()
            modeRect.center = (self.width / 2, self.height / 2 - 70)
            screen.blit(mode, modeRect)
            nameFont = pygame.font.SysFont("comicsansms", 30)
            userName = nameFont.render(f'Welcome {self.userName}!', True, (255, 255, 255))
            nameRect = userName.get_rect()
            nameRect.center = (self.width / 2, self.height / 2)
            screen.blit(userName, nameRect)
            messageFont = pygame.font.SysFont("comicsansms", 20)
            message = messageFont.render("Profile mode waiting to be implemented. Press 's' to start the game", True, (255, 255, 255))
            messageRect = message.get_rect()
            messageRect.center = (self.width / 2, self.height / 2 + 50)
            screen.blit(message, messageRect)
        
        # start screen
        if self.mode == "start":
            screen.blit(self.bg, (self.bgX, 0))
            titleFont = pygame.font.Font("Amatic-Bold.ttf", 50)
            title = titleFont.render('112 Jetpack Joyride', True, (0, 0, 0))
            titleRect = title.get_rect()
            titleRect.center = (self.width / 2, self.height / 2 - 70)
            screen.blit(title, titleRect)
            insFont = pygame.font.Font("Amatic-Bold.ttf", 25)
            ins = insFont.render('Press "space" to register! Press "escape" to log in!', True, (0, 0, 0))
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
        elif self.mode == "game" and not self.isPaused: 
            screen.blit(self.bg, (self.bgX, 0))
            screen.blit(self.bg, (self.bgX2, 0))
            font = pygame.font.Font("Amatic-Bold.ttf", 20)
            text = font.render(f'score: {self.score}', True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (40, 20)
            screen.blit(text, textRect)
            if self.player.mode != "invincible":
                self.playerGroup.draw(screen)
            self.obstacles.draw(screen)
            #print(self.stars)
            self.coins.draw(screen)
            self.itemBoxes.draw(screen)
            if self.player.bullets != None and len(self.player.bullets) != 0:
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
            self.lasers.draw(screen)
            self.lasersPrep.draw(screen)
            self.rockets.draw(screen)
            self.warningSigns.draw(screen)
            if self.player.mode == "invincible":
                self.playerGroup.draw(screen)
        pygame.display.update()
        
    def timerFired(self, dt):
        if self.player.mode == "invincible":
            self.scrollSpeed = 5 * self.oriScrollSpeed
        else:
            self.scrollSpeed = self.oriScrollSpeed
        if not self.playerGroup.sprite.isAlive or (self.mode != "game") or self.isPaused:
            return
        self.score += 1
        if len(self.obstacles) != 0:
            for obstacle in self.obstacles:
                obstacle.scroll += self.scrollSpeed
        if len(self.coins) != 0:
            for coin in self.coins:
                coin.scroll += self.scrollSpeed
        if len(self.rockets) != 0:
            for rocket in self.rockets:
                rocket.scroll += self.scrollSpeed
        if len(self.itemBoxes) != 0:
            for itemBox in self.itemBoxes:
                itemBox.scroll += self.scrollSpeed
        if self.player.mode != "invincible":
            self.scrollSpeed += 1/500
            self.oriScrollSpeed = self.scrollSpeed
                
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
            
        #self.obstacles.update(self.width, self.height)
        self.obstacles.update(self.width, self.height, self.player.x, self.player.y)
        self.playerGroup.update(dt, self.isKeyPressed, self.width, self.height)
        self.coins.update(self.width, self.height, self.player.x, self.player.y, self.player.mode)
        #self.stars.update(self.width, self.height)
        self.itemBoxes.update(self.width, self.height, self.player.x, self.player.y)
        self.warningSigns.update(self.width, self.height)
        self.rockets.update(self.width, self.height, self.player.x, self.player.y)
        self.lasersPrep.update(self.width, self.height, self.player.x, self.player.y)
        self.lasers.update(self.width, self.height, self.player.x, self.player.y)
        #self.hitboxes.update(self.width, self.height)
        
        if self.player.bullets != None and len(self.player.bullets) != 0:
            self.bulletGroup.add(self.player.bullets[-1])
            self.bulletGroup.update(self.width, self.height)

        if self.player.magnet != None:
            self.magnetGroup = pygame.sprite.GroupSingle(self.player.magnet)
            self.player.magnet.update(self.width, self.height, self.player.x, self.player.y)
        
        (boolObstacle, obstacle) = self.player.collide(self.obstacles)
        if self.player.mode != "invincible" and obstacle != None:
            self.player.isAlive = False
            #print(f"collide with obstacle {obstacle}")
            
        (boolCoin, coins) = self.player.collideCoins(self.coins)
        if coins != None:
            for coin in coins:
                if not coin.hit:
                    self.score += 50
                    coin.hit = True
                    coin.count = 0
            #print(f"collide with coin {coin}")

        (boolItemBox, itemBox) = self.player.collide(self.itemBoxes)
        if self.player.mode != "invincible" and itemBox != None:
           #print("invincible mode entered")
            self.player.mode = itemBox.itemType
            #print(self.player.mode)
            self.player.count = 0
            itemBox.hit = True
            itemBox.kill()
            if self.player.mode == "magnet suit":
                self.player.magnet = Magnet(self.player.x, self.player.y)

        (boolRocket, rocket) = self.player.collide(self.rockets)
        if self.player.mode != "invincible" and rocket != None:
            self.player.isAlive = False
            rocket.kill()

        (boolLaser, laser) = self.player.collide(self.lasers)
        if self.player.mode != "invincible" and laser != None and laser.laserOn:
            self.player.isAlive = False
            laser.kill()
        
    def keyPressed(self, keyCode, modifier):
        #print(keyCode)
        if self.mode != "game":
            return
        if keyCode == 114: #keyCode for "r" --> restart
            self.init()
            self.__init__(800, 390)
            #print(self.mode)
        elif keyCode == 112: #keyCode for "p" --> pause
            self.isPaused = not self.isPaused
        elif not self.isPaused and keyCode == 32 and (self.player.mode == "fly"): #keyCode for the space bar
            self.player.mode = "attack"
            self.player.count = 0
            self.player.bullets.append(Bullets(self.player.x, self.player.y))
            #print("space pressed", self.player.count)
            
Game(800, 390).run()
