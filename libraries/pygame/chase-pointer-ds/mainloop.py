import pygame
import numpy as np

import constants as const
import strategy as strat

# Constants
screenSize = (1000, 1000)
param = {
  'm'  : 1,    # Mass, kg
  'k'  : 2,    # Spring constant, N/m, 
  'dt' : 0.05, # Time-step, s
  'g'  : -1    # Dimensionless Damping constant (-2 : critical damping)
}

# Init Screen
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Decision Making Simulator")
screen.fill(const.BLACK)

mouse_pos = [np.array(pygame.mouse.get_pos())] * 3
square_pos = [np.array([400,400])] * 3





# -------- Main Program Loop -----------
done = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Erase old rect
    pygame.draw.rect(screen, const.BLACK, [square_pos[-1][0], square_pos[-1][1], 10, 10])

    # Move rect towards the mouse
    mouse_pos = mouse_pos[-2:] + [np.array(pygame.mouse.get_pos())]
    square_pos = square_pos[-2:] + [strat.update3(mouse_pos, square_pos, param)]

    # Draw new rect
    pygame.draw.rect(screen, const.WHITE, [square_pos[-1][0], square_pos[-1][1], 10, 10])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
