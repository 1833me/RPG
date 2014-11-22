#
# Conway's game of life
#
# http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#
#


import pygame
import game_mouse
import random
from player import Player
from baddie import Baddie

class ConwaysLife(game_mouse.Game):

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.player = Player(self.width/2, self.height/2,
                             50, 50,
                            (255,0,0))

        self.baddies = []

        game_mouse.Game.__init__(self, "RPG",
                                 self.width,
                                 self.height,
                                 10)
        

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if pygame.K_EQUALS in newkeys:
            self.baddies.append(Baddie(random.randint(0,self.width), random.randint(0,self.height), 30, 30, (0, 255, 0)))
        if pygame.K_LEFT in keys:
            self.player.x -= 5
        if pygame.K_RIGHT in keys:
            self.player.x += 5
        if pygame.K_UP in keys:
            self.player.y -= 5
        if pygame.K_DOWN in keys:
            self.player.y += 5

        for b in self.baddies:
            b_x, b_y = b.getPosition()
            p_x, p_y = self.player.getPosition()
            if b_x > p_x:
                b.x -= 1
            elif b_x < p_x:
                b.x += 1
            if b_y > p_y:
                b.y -= 1
            elif b_y < p_y:
                b.y += 1
        return

            
    def paint(self, surface):
        color = (255,255,255)
        surface.fill(color)
        self.player.draw(surface)
        for b in self.baddies:
            b.draw(surface)

def main():
    c = ConwaysLife(900,800)
    c.main_loop()
    
if __name__ == "__main__":
    main()

