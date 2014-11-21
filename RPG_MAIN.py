import pygame
import game_mouse
import random
from player import Player
from baddie import Baddie

class RPG(game_mouse.Game):

    def __init__(self, full_w, full_h, width, height):
        self.full_w = full_w
        self.full_h = full_h
        self.screen_width = width
        self.screen_height = height
        self.display_x = width
        self.display_y = height

        self.player = Player(self.screen_width/2, self.screen_height/2,
                             50, 50,
                            (255,0,0))

        self.baddies = []

        game_mouse.Game.__init__(self, "RPG",
                                 self.screen_width,
                                 self.screen_height,
                                 10)
        

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if pygame.K_EQUALS in newkeys:
            self.baddies.append(Baddie(random.randint(0,self.full_w), random.randint(0,self.full_h), 30, 30, (0, 255, 0), 3))
        if pygame.K_LEFT in keys:
            self.display_x -= 5
        if pygame.K_RIGHT in keys:
            self.display_x += 5
        if pygame.K_UP in keys:
            self.display_y -= 5
        if pygame.K_DOWN in keys:
            self.display_y += 5

        for b in self.baddies:
            b_x, b_y = b.getPosition()
            p_x, p_y = self.player.getPosition()
            if b_x > p_x:
                b.x -= 1 * b.speed
            elif b_x < p_x:
                b.x += 1 * b.speed
            if b_y > p_y:
                b.y -= 1 * b.speed
            elif b_y < p_y:
                b.y += 1 * b.speed
        return

            
    def paint(self, surface):
        color = (255,255,255)
        surface.fill(color)
        for b in range(0, self.full_h, 20):
            pygame.draw.line(surface ,(0,0,0),(0,b),(self.full_w, b), 5)
        for a in range(0, self.full_w, 20):
            pygame.draw.line(surface, (0,0,0),(a,0),(a, self.full_h), 5)
        self.player.draw(surface)
        for b in self.baddies:
            b.draw(surface, self.display_x, self.display_y, self.screen_width, self.screen_height)

def main():
    c = RPG(1500, 1500, 900, 800)
    c.main_loop()
    
if __name__ == "__main__":
    main()

