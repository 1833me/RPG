__author__ = 'kids'

import random
from baddie import Baddie

class World:

    def __init__(self, raw_world):
        self.spawn_points = []
        for s in raw_world:
            self.spawn_points.append(s)
        return

    def draw(self, surface):
        return

    def spawn(self):
        new_baddies = []
        for s in self.spawn_points:
            summon = random.randint(0, 1000)
            if summon <= s[4]:
                new_baddies.append(Baddie(s[0], s[1], 30, 30, (0, 255, 0), s[2], s[3], s[5]))
        return new_baddies