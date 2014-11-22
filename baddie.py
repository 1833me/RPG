__author__ = 'kids'

import pygame

GOBLIN = 1
BOSS_1 = 10
IMG_G1 = pygame.image.load("Goblin.png")
IMG_G2 = pygame.image.load("GoblinWalk1.png")
IMG_G3 = pygame.image.load("GoblinWalk2.png")
IMG_BOSS1 = pygame.image.load("FinalDemon.png")

class Baddie:

    def __init__(self, x, y, width, height, color, speed, drops, type, hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.boxes = []
        self.alive = True
        self.x_tile = x/50
        self.y_tile = y/50
        self.drops = drops
        self.walk = 0
        self.img = IMG_G2
        self.type = type
        self.hp = hp
        return

    def getPosition(self):
        return self.x, self.y

    def draw(self, surface, d_x, d_y, s_w, s_h):

        if (self.x > d_x + s_w) or (self.x + self.width < d_x) or (self.y > d_y + s_h) or (self.y + self.height < d_y):
            return
        dis_x = self.x - d_x
        dis_y = self.y - d_y
        if self.type == GOBLIN:
            self.walk += 1
            if self.walk >= 3:
                self.walk = 0
                if self.img == IMG_G2:
                    self.img = IMG_G3
                else:
                    self.img = IMG_G2


        if self.type == BOSS_1:
            self.img = IMG_BOSS1

        surface.blit(self.img,[dis_x,dis_y])
        '''rect = pygame.Rect(dis_x, dis_y, self.width, self.height)
        pygame.draw.rect(surface, self.color, rect)'''
        return

    def checkHit(self, x, y, w, h):
        this_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        that_rect = pygame.Rect(x, y, w, h)
        return this_rect.colliderect(that_rect)
