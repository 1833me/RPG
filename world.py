__author__ = 'kids'
#(self, x, y, width, height, color, speed, drops, type)
import random
from baddie import Baddie

BOSS_1 = 10

class World:

    def __init__(self, raw_world):
        self.spawn_points = []
        for s in raw_world:
            self.spawn_points.append(s)
        return

    def spawn(self):
        new_baddies = []
        for s in self.spawn_points:
            summon = random.randint(0, 1000)
            if summon <= s[4]:
                new_baddies.append(Baddie(s[0], s[1], 30, 30, (0, 255, 0), s[2], s[3], s[5], s[6]))
        return new_baddies

    def spawn_boss(self, x, y, num):
        if num == 1:
            return Baddie(x,y, WIDTH, HEIGHT, (0,0,0), 5, [], BOSS_1)