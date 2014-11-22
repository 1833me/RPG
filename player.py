__author__ = 'kids'

import pygame, math
from bullet import Bullet
IMG_1 = pygame.image.load('Man_left_leg_up.png')
IMG_2 = pygame.image.load("Man_right_leg_up.png")
IMG_3 = pygame.image.load("Basic_Man.png")
STONE_SWORD = pygame.image.load("stoneSword.png")

class Player:

    def __init__(self, x, y, width, height, color, hp, inventory):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hp = hp
        self.max_hp = hp
        self.boxes = []
        self.x_tile = x/50
        self.y_tile = y/50
        self.img = IMG_1
        self.stance = 0
        self.standing = True
        self.inventory = inventory
        self.ready = True
        self.sword = pygame.image.load("Stick.png")
        self.bullet = False
        self.damage = 1
        return

    def getPosition(self):
        return self.x, self.y

    def draw(self, surface, x, y, hp_x, hp_y):

        if self.standing == True:
            self.img = IMG_3
        if self.stance >= 3 and self.standing != True:
            self.stance = 0
            self.standing = True
            if self.img == IMG_1:
                self.img = IMG_2
            else:
                self.img = IMG_1

        surface.blit(self.img, [x,y])

        self.drawHP(surface, hp_x, hp_y)
        return

    def drawHP(self, surface, hp_x, hp_y):
        rect = pygame.Rect(hp_x - hp_x + 50, hp_y - 75, int((self.hp/(self.max_hp+.0)) * 250) , 50)
        rect_out = pygame.Rect(hp_x - hp_x + 50, hp_y - 75, 250, 50)
        pygame.draw.rect(surface, (255,0,0), rect)
        pygame.draw.rect(surface, (255,0,0), rect_out, 1)

    def checkHit(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if(((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def attack(self, mouse_pos, off_x, off_y,):
        self.ready = False
        m_x = mouse_pos[0]
        m_y = mouse_pos[1]
        #m_x -= 900
        #m_y -= 800
        ang = math.atan2(m_y + self.y, m_x + self.x)
        ang = math.degrees(ang)
        pygame.transform.rotate(self.sword, ang)

        dx = m_x - (self.x - off_x)
        dy = m_y - (self.y - off_y)
        l = math.sqrt(dx**2 + dy**2)
        dx /= l
        dy /= l
        self.bullet = Bullet(12, 35, self.x - off_x + 23,self.y - off_y - 2, (0,0,0), ang, self.sword)
        self.bullet.dx = dx * 20
        self.bullet.dy = dy * 20

        #if m_x + self.x < 0:
        #    self.bullet.dx *= -1
        #if m_y + self.y< 0:
        #    self.bullet.dy *= -1

        return self.bullet



