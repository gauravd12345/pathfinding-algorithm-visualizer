import sys
import time
import pygame
from node import Node

pygame.init()

winSize = 800
boxNum = 50
boxSize = winSize // boxNum

win = pygame.display.set_mode((winSize, winSize))
pygame.display.set_caption("Pathfinding Algorithm Visualizer")

# Colors
colors = {'white': (255, 255, 255),
          'black': (0, 0, 0),
         'silver': (128, 128, 128),
            'red': (255, 0, 0),
          'green': (0, 255, 0),
           'blue': (0, 0, 255),
      'lightblue': (66, 245, 239),
    'lightorange': (252, 186, 3)}


# Initializes the blank grid of nodes
nodeGrid = []
for i in range(boxNum):
    gridRow = []
    for j in range(boxNum):
        gridRow.append(Node(i, j, colors['white']))

    nodeGrid.append(gridRow)


# Clears all the nodes in the grid
def clearNodeGrid(nodeGrid):
    for gridRow in nodeGrid:
        for node in gridRow:
            if node.getColor() == colors['white'] or node.getColor() == colors['black']:
                node.setColor(colors['white'])


# Draws the grid of nodes onto the window
def drawGrid():

    # Draws each node based on its position
    for x in range(len(nodeGrid)):
        for y in range(len(nodeGrid[x])):
            row, col = nodeGrid[x][y].getPos()
            color = nodeGrid[x][y].getColor()
            pygame.draw.rect(win, color, (row * boxSize, col * boxSize, boxSize, boxSize))


    # Draws the lines to form the grid        
    for i in range(boxNum):
        pygame.draw.line(win, colors['silver'], (i * boxSize, 0), (i * boxSize, winSize))

    for j in range(boxNum):
        pygame.draw.line(win, colors['silver'], (0, j * boxSize), (winSize, j * boxSize))



# Returns the mouse position on the grid  
def getMousePos():
    x, y = pygame.mouse.get_pos()
    return x // boxSize, y // boxSize


# Returns the node directly under the mouse cursor
def getNodeUnderMouse():
    x, y = getMousePos()
    return nodeGrid[x][y]


# Returns the node with the lowest f score
def getMinScore(node, grid):
    minScore, minNode = float("inf"), node
    for i in node.getNeighbours(grid):

        newNodeScore = i.get_fScore(startX, startY, endX, endY)
        if newNodeScore < minScore:
            minScore, minNode = newNodeScore, i

    return minNode
        

# Some constants
clock = pygame.time.Clock()
running, selected = True, False

startX, startY = 10, 10
endX, endY = 40, 40
startNode = nodeGrid[startX][startY]
endNode = nodeGrid[endX][endY]

startNode.setColor(colors['lightblue'])
endNode.setColor(colors['lightorange'])


openList, closeList = [startNode], []


# Gameloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            selected = True

        if event.type == pygame.MOUSEBUTTONUP:
            selected = False

      
        if event.type == pygame.KEYDOWN:
            # Clears the node grid
            if event.key == pygame.K_RETURN:
                clearNodeGrid(nodeGrid)

            if event.key == pygame.K_SPACE:
                while len(openList) > 0:
                    minNode, minScore = startNode, float("inf")
                    for i in openList:
                        if i.get_fScore(startX, startY, endX, endY) < minScore:
                            minNode = i
                            #print(minNode.getPos())
                            minScore = i.get_fScore(startX, startY, endX, endY)
                        


                    openList.remove(minNode)
                    children = minNode.getNeighbours(nodeGrid)
                    for j in children:
                        if j == endNode:
                            break

                        if j in openList:
                            """index = openList[openList.index(j)]
                            if j.get_fScore(startX, startY, endX, endY) > openList[index].get_fScore(startX, startY, endX, endY):
                                continue"""
                            continue
                        
                        if j in closeList:
                            """index = closeList[openList.index(j)]
                            if j.get_fScore(startX, startY, endX, endY) > closeList[index].get_fScore(startX, startY, endX, endY):
                                continue    

                            else:
                                openList.append(j)"""
                            continue
                        
                        openList.append(j)


                    closeList.append(minNode)
                    

    # Changes the color of the node 
    # if the mouse is clicked
    if selected:

        # Draws the node
        if pygame.mouse.get_pressed()[0]:
            node = getNodeUnderMouse()
            if node.getColor() == colors['white']:
                node.setColor(colors['black'])
                
        # Erases the node
        elif pygame.mouse.get_pressed()[2]:
            node = getNodeUnderMouse()
            node.setColor(colors['white'])
        

    drawGrid()
    pygame.display.update()
    clock.tick(60)



pygame.quit()
