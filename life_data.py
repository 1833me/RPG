#
# Conway's game of life
#
# http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#
#


import random

DEAD = 0
LIVE = 1

class LifeData:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.emptyBoard()

    def randomBoard(self):
        self.grid = []
        for i in range(self.width * self.height):
            r = random.randrange(0,10)
            if r < 2:
                self.grid.append(LIVE)
            else:
                self.grid.append(DEAD)
            
    def emptyBoard(self):
        self.grid = []
        for i in range(self.width*self.height):
            self.grid.append(DEAD)
            
    def fullBoard(self):
        self.grid = []
        for i in range(self.width*self.height):
            self.grid.append(LIVE)
            
    def getWidth(self):
        return self.width
        
    def getHeight(self):
        return self.height

    def calcIndex(self, x, y):
        if y >= 0 and y < self.height and x >=0 and x < self.width:
            return y * self.width + x
        return 0
    
    def getCell(self, x, y):
        return self.grid[self.calcIndex(x, y)]

    def setCell(self, x, y, value):
        if value == DEAD or value == LIVE:
            self.grid[self.calcIndex(x, y)] = value

    def evolve(self):
        neighbors = [ (-1, -1), (0, -1), (1, -1),
                      (-1, 0),           (1,0),
                      (-1,1),   (0,1),   (1,1) ]
        newgrid = []

        for y in range(self.height):
            for x in range(self.width):
                live_count = 0
                for (dx,dy) in neighbors:
                    x1 = (x + dx + self.width) % self.width
                    y1 = (y + dy + self.height) % self.height
                    if self.getCell(x1,y1) == LIVE:
                        live_count += 1
                if live_count < 2:
                    # under population
                    newgrid.append(DEAD)
                elif live_count > 3:
                    # over population
                    newgrid.append(DEAD)
                elif self.getCell(x,y) == LIVE:
                    # stay alive with 2 or 3 neighbors
                    newgrid.append(LIVE)
                elif live_count == 3:  # currently dead
                    # new cell with 3 neighbors
                    newgrid.append(LIVE)
                else:
                    # no new cell with 2 neighbors
                    newgrid.append(DEAD)
                    
        self.grid = newgrid
        

    def __str__(self):
        s = ''
        for y in range(self.height):
            for x in range(self.width):
                s = s + str(self.getCell(x, y))
            s = s + "\n"
        return s

