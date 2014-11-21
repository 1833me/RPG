__author__ = 'kids'

import pygame


class Player:

    def __init__(self, x, y, width, height, color):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        return

    def getPosition(self):
        return self.x, self.y

    def draw(self, surface, x, y):

        rect = pygame.Rect(x, y, self.width, self.height)
        pygame.draw.rect(surface, self.color, rect)
        return
