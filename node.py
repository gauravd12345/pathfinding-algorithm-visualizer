class Node:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color


    # Returns the node's position
    def getPos(self):
        return self.row, self.col


    # Returns the node's color
    def getColor(self):
        return self.color


    # Returns the node's neighbours
    def getNeighbours(self):
        pass
    

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

    
