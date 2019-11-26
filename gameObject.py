import pygame

# framework taken from: https://github.com/LBPeraza/Pygame-Asteroids
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.baseImage = image.copy()
        self.width, self.height = image.get_size()
        self.updateRect()
        self.velocity = (0, 0)
        self.angle = 0

    def updateRect(self):
        #self.width, self.height = self.image.get_size()
        self.rect = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2,
                                self.width, self.height)
        

    def update(self, screenWidth, screenHeight, image):
        self.image = image
        self.updateRect()

    def collide(self, obj):
        (x0, y0, x1, y1) = (self.x - self.width/2,
                            self.y - self.height/2,
                            self.x + self.width/2,
                            self.y + self.height/2)
        (a0, b0, a1, b1) = (obj.x - obj.width/2,
                            obj.y - obj.height/2,
                            obj.x + obj.width/2,
                            obj.y + obj.height/2)
        return (x1 >= a0) and (y1 >= b0) and (a1 >= x0) and (b1 >= y0)
    
