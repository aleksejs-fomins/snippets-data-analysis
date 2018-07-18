import pygame
import numpy as np

import constants as const
import strategy as strat

# Constants
screenSize = (1000, 1000)
squareSpeed = 5
squarePos = np.array([100,100])

# Init Screen
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Decision Making Simulator")
screen.fill(const.BLACK)

# -------- Main Program Loop -----------
done = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Erase old rect
    pygame.draw.rect(screen, const.BLACK, [squarePos[0], squarePos[1], 10, 10])

    # Move rect towards the mouse
    mousePos = np.array(pygame.mouse.get_pos())
    #squarePos += strat.chase(squarePos, mousePos, squareSpeed).astype(int)
    #squarePos += strat.drunkChase(squarePos, mousePos, squareSpeed).astype(int)
    squarePos += strat.veryDrunkChase(squarePos, mousePos, squareSpeed).astype(int)

    # Draw new rect
    pygame.draw.rect(screen, const.WHITE, [squarePos[0], squarePos[1], 10, 10])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
