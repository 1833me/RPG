__author__ = 'kids'

import pygame


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
        self.inventory = inventory
        return

    def getPosition(self):
        return self.x, self.y

    def draw(self, surface, x, y, hp_x, hp_y):

        rect = pygame.Rect(x, y, self.width, self.height)
        pygame.draw.rect(surface, self.color, rect)
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
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False
