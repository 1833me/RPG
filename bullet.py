import pygame
IMG_1 = pygame.image.load("Stick.png")
class Bullet():

    def __init__(self,width,height,x,y,color, aang, img):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.alive  = True
        self.hit    = False
        self.dx =  0
        self.dy = 0
        self.life = 10
        self.aang = aang
        self.img = img

        return

    def moveBullet(self):
        self.x += self.dx
        self.x = int(self.x)
        self.y += self.dy
        self.y = int(self.y)
        return

    def setAlive(self,alive):
        self.alive = alive
        return
    
    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False
    
    def draw(self, surface):
        if self.alive:
            pygame.transform.rotate(IMG_1,self.aang)
            surface.blit(self.img,[self.x,self.y])
        return
        
