# modified code taken from: http://blog.lukasperaza.com/getting-started-with-pygame/
import pygame
import random
from Player import Player
from Obstacles import Obstacles
from Hitboxes import Hitboxes

class PygameGame(object):

    def init(self):
        Obstacles.init()
        self.obstacles = pygame.sprite.Group()
        pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(2000, 3500))
        Player.init()
        self.player = Player(self.width / 2, self.height / 2)
        self.playerGroup = pygame.sprite.GroupSingle(self.player)
        
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
        #self.bgColor = (255, 255, 255)
        self.mode = "start"
        self.obstaclesLst = []
        self.hitboxes = []
        pygame.init()
    
    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
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
                                maxX = prevX
                        x = random.randint(max(self.width / 2 + self.player.x,
                                               maxX + 300),
                                           max(self.width / 2 + self.player.x,
                                               maxX + 700))
                        y = random.randint(50, self.height - 50)
                    currentObstacle = Obstacles(x, y)
                    self.obstaclesLst.append(currentObstacle)
                    self.obstacles.add(currentObstacle)
                    self.hitboxes.append(currentObstacle.hitbox)
            #screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
