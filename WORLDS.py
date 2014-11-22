__author__ = 'kids'
#def __init__(self, x, y, width, height, color, speed, drops):
#     Spawn x, y, speed, drops{ name, chance/100, weapon/armor, damage}, chance/1000, type, HP
from  item import Item
GOBLIN = 1
SLIME = 2
TROLL = 3
PIRATE = 4

WORLD_1 = [
    [
        50, 100, 2, [[Item("Stone Sword", "WEAPON", 5), 7]], 25, SLIME, 2,
    ],
    [
        1450, 1400, 2, [[Item("Stone Sword", "WEAPON", 5), 7]], 25, SLIME, 2
    ]
]

WORLD_2 = [

    [
        750, 750, 3, [[Item("Obsidian Sword", "WEAPON", 15), 7]], 15, SLIME, 9
    ],
    [
        750, 0, 3, [[Item("Obsidian Sword", "WEAPON", 15), 7]], 15, GOBLIN, 15
    ]
]

WORLD_3 = [
    [
        1200, 100, 3, [[Item("Paper Butterfly", "WEAPON", 50), 10]], 10, SLIME, 15
    ],
    [
        100, 1200, 3, [[Item("Paper Butterfly", "WEAPON", 50), 10]], 10, GOBLIN, 30
    ],
    [
        1200, 1200, 2, [[Item("Paper Butterfly", "WEAPON", 50), 10]], 15, PIRATE, 45
    ]
]
