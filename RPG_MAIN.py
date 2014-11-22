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

        self.player = Player(self.screen_width / 2, self.screen_height / 2,
                             50, 50,
                             (255, 0, 0),
                             100)

        self.baddies = []
        self.grid = []
        for i in range(0, self.full_h, 50):
            for j in range(0, self.full_w, 50):
                self.grid.append([])

        game_mouse.Game.__init__(self, "RPG",
                                 self.screen_width,
                                 self.screen_height,
                                 10)

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.grid = []
        if pygame.K_EQUALS in newkeys:
            self.baddies.append(
                Baddie(random.randint(0, self.full_w), random.randint(0, self.full_h), 30, 30, (0, 255, 0), 3), [])
        if pygame.K_MINUS in keys:
            self.player.hp -= 1
            if self.player.hp < 0:
                self.player.hp = 0
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

        for i in range(0, self.full_h, 50):
            for j in range(0, self.full_w, 50):
                self.grid.append([])

        a = (self.full_w / 50 * self.player.y / 50) + self.player.x / 50
        b = (self.full_w / 50 * self.player.y / 50) + (self.player.x + 50) / 50
        c = (self.full_w / 50 * (self.player.y + 50) / 50) + self.player.x / 50
        d = (self.full_w / 50 * (self.player.y + 50) / 50) + (self.player.x + 50) / 50
        boxes = [a]
        r_flag = False
        d_flag = False
        self.player.x_tile = self.player.x / 50
        self.player.y_tile = self.player.y / 50
        if self.player.x_tile >= self.full_w / 50 - 1:
            r_flag = True
        if self.player.y_tile >= self.full_h / 50 - 1:
            d_flag = True
        if not r_flag:
            boxes.append(b)
        if not d_flag:
            boxes.append(c)
        if (not r_flag) and (not d_flag):
            boxes.append(d)
        self.player.boxes = boxes
        counter = 0
        livers = []
        for bad in self.baddies:

            b_x, b_y = bad.getPosition()
            p_x, p_y = self.player.getPosition()
            if b_x > p_x:
                bad.x -= 1 * bad.speed
            elif b_x < p_x:
                bad.x += 1 * bad.speed
            if b_y > p_y:
                bad.y -= 1 * bad.speed
            elif b_y < p_y:
                bad.y += 1 * bad.speed
            flag = False
            if bad.checkHit(self.player.x, self.player.y, self.player.width, self.player.height):
                self.player.hp -= 5
                if self.player.hp < 0:
                    self.player.hp = 0
                flag = True
            if not flag:
                livers.append(bad)
            """  a = (self.full_w / 50 * bad.y / 50) + bad.x / 50
            b = (self.full_w / 50 * bad.y / 50) + (bad.x + 50) / 50
            c = (self.full_w / 50 * (bad.y + 50) / 50) + bad.x / 50
            d = (self.full_w / 50 * (bad.y + 50) / 50) + (bad.x + 50) / 50
            boxes = []
            bad.x_tile = bad.x / 50
            bad.y_tile = bad.y / 50
            if a < 900:
                self.grid[a].append(counter)
                boxes.append(a)
                bad.boxes = boxes
            if b < 900:
                boxes.append(b)
                self.grid[b].append(counter)
            if c < 900:
                boxes.append(c)
                self.grid[c].append(counter)
            if d < 900:
                boxes.append(d)
                self.grid[d].append(counter)
            counter += 1

            for box in bad.boxes:
                if box in self.player.boxes and not flag: """

        self.baddies = livers

        return

    def paint(self, surface):
        color = (255, 255, 255)
        surface.fill(color)
        for bad in self.baddies:
            bad.draw(surface, self.display_x, self.display_y, self.screen_width, self.screen_height)
        pygame.draw.circle(surface, (0, 0, 255), (1000 - self.display_x, 900 - self.display_y), 40)
        self.drawwalls(surface)
        self.player.draw(surface, self.screen_width / 2, self.screen_height / 2, self.screen_width, self.screen_height)

    def drawwalls(self, surface):
        pygame.draw.line(surface, (0, 0, 0), (0 - self.display_x, 0 - self.display_y),
                         (self.full_w - self.display_x, 0 - self.display_y))
        pygame.draw.line(surface, (0, 0, 0), (0 - self.display_x, self.full_h - self.display_y),
                         (self.full_w - self.display_x, self.full_h - self.display_y))
        pygame.draw.line(surface, (0, 0, 0), (0 - self.display_x, 0 - self.display_y),
                         (0 - self.display_x, self.full_h - self.display_y))
        pygame.draw.line(surface, (0, 0, 0), (self.full_w - self.display_x, 0 - self.display_y),
                         (self.full_w - self.display_x, self.full_h - self.display_y))
        return


def main():
    c = RPG(1500, 1500, 900, 800)
    c.main_loop()


if __name__ == "__main__":
    main()