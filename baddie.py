__author__ = 'kids'

import pygame


class Baddie:

    def __init__(self, x, y, width, height, color, speed):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        return

    def getPosition(self):
        return self.x, self.y

    def draw(self, surface, d_x, d_y, s_w, s_h, p_x, p_y):

        if (self.x > d_x + s_w) or (self.x + self.width < d_x) or (self.y > d_y + s_h) or (self.y + self.height < d_y):
            return
        dis_x = self.x - d_x
        dis_y = self.y - d_y
        rect = pygame.Rect(dis_x, dis_y, self.width, self.height)
        pygame.draw.rect(surface, self.color, rect)
        return
