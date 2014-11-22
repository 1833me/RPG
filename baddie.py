__author__ = 'kids'

import pygame


class Baddie:

<<<<<<< HEAD
    def __init__(self, x, y, width, height, color, speed, drops):
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
        return

    def getPosition(self):
        return self.x, self.y

    def draw(self, surface, d_x, d_y, s_w, s_h):

        if (self.x > d_x + s_w) or (self.x + self.width < d_x) or (self.y > d_y + s_h) or (self.y + self.height < d_y):
            return
        dis_x = self.x - d_x
        dis_y = self.y - d_y
        rect = pygame.Rect(dis_x, dis_y, self.width, self.height)
        pygame.draw.rect(surface, self.color, rect)
        return

    def checkHit(self, x, y, w, h):
        this_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        that_rect = pygame.Rect(x, y, w, h)
        return this_rect.colliderect(that_rect)
