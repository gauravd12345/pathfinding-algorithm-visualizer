import pygame

pygame.init()

winSize = 700
boxSize = winSize // 50

win = pygame.display.set_mode((winSize, winSize))
pygame.display.set_caption("Pathfinding Algorithm Visualizer")

# Colors
colors = {'w': (255, 255, 255),
          'bl': (0, 0, 0),
          'r': (255, 0, 0),
          'g': (0, 255, 0),
          'b': (0, 0, 255)}


clock = pygame.time.Clock()
running = True


# Gameloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       

    win.fill(colors['w'])
    
    
    pygame.display.update()
    clock.tick(60)


pygame.quit()