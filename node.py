# Colors
colors = {'white': (255, 255, 255),
          'black': (0, 0, 0),
         'silver': (128, 128, 128),
            'red': (255, 0, 0),
          'green': (0, 255, 0),
           'blue': (0, 0, 255),
      'lightblue': (66, 245, 239),
    'lightorange': (252, 186, 3)}


class Node:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.neighbours = []

    # Returns the node's position
    def getPos(self):
        return self.row, self.col


    # Returns the node's color
    def getColor(self):
        return self.color


    # Returns the node's neighbours
    def getNeighbours(self, grid):
        row, col = self.getPos()
        if row + 1 <= 49:
            if grid[row + 1][col].getColor() != colors['black']:
                self.neighbours.append(grid[row + 1][col])

        if 0 <= row - 1:
            if grid[row - 1][col].getColor() != colors['black']:
                self.neighbours.append(grid[row - 1][col])

        if col + 1 <= 49:
            if grid[row][col + 1].getColor() != colors['black']:
                self.neighbours.append(grid[row][col + 1])

        if 0 <= col - 1:
            if grid[row][col - 1].getColor() != colors['black']:
                self.neighbours.append(grid[row][col - 1])

        return self.neighbours
         
         
    # Returns the G score of the node
    def get_gScore(self, startX, startY):
        x, y = self.getPos()
        return abs(x - startX) + abs(y - startY)


    # Returns the H score of the node
    def get_hScore(self, endX, endY):
        x, y = self.getPos()
        return abs(x - endX) + abs(y - endY)


    # Returns the F score of the node
    def get_fScore(self, startX, startY, endX, endY):
        g_score = self.get_gScore(startX, startY)
        h_score = self.get_hScore(endX, endY)
        return g_score + h_score


    # Changes the color of a node
    def setColor(self, color):
        self.color = color

    
