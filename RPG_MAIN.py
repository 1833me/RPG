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
        self.display_x = 0
        self.display_y = 0

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
            if self.player.x <= 5:
                self.display_x -= self.player.x
                self.player.x -= self.player.x
            else:
                self.display_x -= 5
                self.player.x -= 5
        if pygame.K_RIGHT in keys:
            if self.player.x + self.player.width >= self.full_w - 5:
                self.display_x += self.full_w - self.player.width - self.player.x
                self.player.x += self.full_w - self.player.width - self.player.x

            else:
                self.display_x += 5
                self.player.x += 5
        if pygame.K_UP in keys:
            if self.player.y <= 5:
                self.display_y -= self.player.y
                self.player.y -= self.player.y
            else:
                self.display_y -= 5
                self.player.y -= 5
        if pygame.K_DOWN in keys:
            if self.player.y + self.player.height >= self.full_h - 5:
                self.player.y = self.full_h - self.player.height - self.player.y
                self.display_y = self.full_h - self.player.height - self.player.y
            else:
                self.display_y += 5
                self.player.y += 5
        if pygame.K_p in newkeys:
            print self.player.x, self.player.y
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
        self.player.draw(surface, self.screen_width/2, self.screen_height/2)
        for b in self.baddies:
            b.draw(surface, self.display_x, self.display_y, self.screen_width, self.screen_height, self.player.x, self.player.y)
        pygame.draw.circle(surface, (0,0,255), (1000-self.display_x,900-self.display_y), 40)
        self.drawWalls(surface)

    def drawWalls(self, surface):
        pygame.draw.line(surface, (0,0,0,), (0-self.display_x, 0-self.display_y), (self.full_w - self.display_x, 0-self.display_y))
        pygame.draw.line(surface, (0,0,0,), (0-self.display_x, self.full_h-self.display_y), (self.full_w - self.display_x, self.full_h-self.display_y))
        pygame.draw.line(surface, (0,0,0,), (0-self.display_x, 0-self.display_y), (0 - self.display_x, self.full_h-self.display_y))
        pygame.draw.line(surface, (0,0,0,), (self.full_w-self.display_x, 0-self.display_y), (self.full_w - self.display_x, self.full_h-self.display_y))
        return


def main():
    c = RPG(1500, 1500, 900, 800)
    c.main_loop()
    
if __name__ == "__main__":
    main()

