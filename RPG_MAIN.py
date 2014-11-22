import pygame
import game_mouse
from player import Player
from WORLDS import *
from world import World
import random


GOBLIN = 1
ORC = 2
TROLL = 3
PIRATE = 4
BOSS_1 = 10
IMG_B = pygame.image.load("background.png")
STONE_SWORD = pygame.image.load("stoneSword.png")

class RPG(game_mouse.Game):
    def __init__(self, full_w, full_h, width, height):
        self.full_w = full_w
        self.full_h = full_h
        self.screen_width = width
        self.screen_height = height
        self.display_x = 0
        self.display_y = 0
        self.curr_world = World(WORLD_1)
        self.stage = 1

        self.player = Player(self.screen_width / 2, self.screen_height / 2,
                             31, 50,
                             (255, 0, 0),
                             100, [])

        self.baddies = []
        self.bullet = False
        game_mouse.Game.__init__(self, "RPG",
                                 self.screen_width,
                                 self.screen_height,
                                 20)

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        if self.player.hp <= 0:
            return
        self.player.standing = True
        if self.stage == 1:
            self.baddies += self.curr_world.spawn()
        if self.stage == 1.5 and self.baddies == []:
            self.stage = 1.75
            self.baddies.append(self.curr_world.spawn_boss(self.full_w/2,self.full_h/2, 1))

        if 1 in newbuttons:
            if self.player.ready:
                self.bullet = self.player.attack(mouse_position, self.display_x, self.display_y)
        if pygame.K_MINUS in keys:
            self.player.hp -= 1
            if self.player.hp < 0:
                self.player.hp = 0
        if pygame.K_LEFT in keys:
            self.player.standing = False
            self.player.stance += 1
            if self.player.x <= 5:
                self.display_x -= self.player.x
                self.player.x -= self.player.x
            else:
                self.display_x -= 5
                self.player.x -= 5

        if pygame.K_RIGHT in keys:
            self.player.standing = False
            self.player.stance += 1
            if self.player.x + self.player.width >= self.full_w - 5:
                self.display_x += self.full_w - self.player.width - self.player.x
                self.player.x += self.full_w - self.player.width - self.player.x
            else:
                self.display_x += 5
                self.player.x += 5

        if pygame.K_UP in keys:
            self.player.standing = False
            self.player.stance += 1
            if self.player.y <= 5:
                self.display_y -= self.player.y
                self.player.y -= self.player.y
                print self.display_y
            else:
                self.display_y -= 5
                self.player.y -= 5

        if pygame.K_DOWN in keys:
            self.player.standing = False
            self.player.stance += 1
            if self.player.y + self.player.height >= self.full_h - 5:
                self.display_y += self.full_h - self.player.height - self.player.y
                self.player.y += self.full_h - self.player.height - self.player.y

            else:
                self.display_y += 5
                self.player.y += 5

        if pygame.K_p in keys:
            print self.player.inventory

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
            if self.bullet and self.bullet.alive:
                print self.bullet.x, self.bullet.y
                if self.bullet.hitRectangle(bad.x, bad.y, bad.width, bad.height):
                    bad.hp -= self.player.damage
                    if bad.hp <= 0:
                        flag = True
                        for d in bad.drops:
                            r = random.randint(1,100)
                            if r <= d[1]:
                                if d[0].type == "WEAPON":
                                    self.player.damage = d[0].value
                                    if d[0].name == "Stone Sword":
                                        self.player.sword = STONE_SWORD
                                        self.stage = 1.5

                    self.bullet.setAlive(False)

            if bad.checkHit(self.player.x, self.player.y, self.player.width, self.player.height):
                if bad.type == BOSS_1:
                    self.player.hp -= 100

                self.player.hp -= 5
                if self.player.hp < 0:
                    self.player.hp = 0
                flag = True
            if not flag:
                livers.append(bad)

        self.baddies = livers

        return

    def paint(self, surface):
        color = (255, 255, 255)
        surface.blit(IMG_B,[0-self.display_x,0-self.display_y])
        for bad in self.baddies:
            bad.draw(surface, self.display_x, self.display_y, self.screen_width, self.screen_height)

        self.drawwalls(surface)
        x,y = self.screen_width / 2, self.screen_height / 2
        self.player.draw(surface, x,y, self.screen_width, self.screen_height)
        if self.player.ready:
            surface.blit(self.player.sword, [x+23,y-2])
        if not self.player.ready:
            self.player.bullet.moveBullet()

            self.player.bullet.draw(surface, self.display_x, self.display_y)
            self.player.bullet.life -= 1
            if self.player.bullet.life <= 0:
                self.player.ready = True
                self.player.bullet = False

    def drawwalls(self, surface):
        pygame.draw.line(surface, (0, 0, 0), (0 - self.display_x, 0 - self.display_y),
                         (self.full_w - self.display_x, 0 - self.display_y),10)
        pygame.draw.line(surface, (0, 0, 0), (0 - self.display_x, self.full_h - self.display_y),
                         (self.full_w - self.display_x, self.full_h - self.display_y),10)
        pygame.draw.line(surface, (0, 0, 0), (0 - self.display_x, 0 - self.display_y),
                         (0 - self.display_x, self.full_h - self.display_y),10)
        pygame.draw.line(surface, (0, 0, 0), (self.full_w - self.display_x, 0 - self.display_y),
                         (self.full_w - self.display_x, self.full_h - self.display_y),10)
        return


def main():
    c = RPG(1500, 1500, 900, 800)
    c.main_loop()


if __name__ == "__main__":
    main()
