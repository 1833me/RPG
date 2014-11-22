__author__ = 'kids'
#def __init__(self, x, y, width, height, color, speed, drops):
#     Spawn x, y, speed, drops{ name, chance/100, weapon/armor, damage}, chance/1000, type
from  item import Item
GOBLIN = 1
ORC = 2
TROLL = 3
PIRATE = 4

WORLD_1 = [
    [
        50, 100, 2, [[Item("Stone Sword", "WEAPON", 5), 10]], 10, GOBLIN, 2
    ],
    [
        1450, 1400, 2, [[Item("Stone Sword", "WEAPON", 5), 10]], 10, GOBLIN, 2
    ]
]
