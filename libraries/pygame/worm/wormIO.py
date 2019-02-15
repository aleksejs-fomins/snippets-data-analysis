import pygame
import numpy as np

# Define some colors
BLACK   = 0x000000
WHITE   = 0xFFFFFF
GRAY    = 0x333333
RED     = 0xFF0000
GREEN   = 0x00FF00
GREEN2  = 0x003300


def heightFn(t):
    return t*(1-t)

def drawWorm(surf, traj):
    LENWORM = len(traj)
    for i in range(1, LENWORM):
        x = traj[i][0]
        y = traj[i][1]

        dx = traj[i][0] - traj[i - 1][0]
        dy = traj[i][1] - traj[i - 1][1]
        cos_dx = dx / np.sqrt(dx**2 + dy**2)
        sin_dx = dy / np.sqrt(dx ** 2 + dy ** 2)
        rad = 20*heightFn(i/100)
        pygame.draw.line(surf, GREEN, [x - rad*sin_dx, y + rad*cos_dx], [x + rad*sin_dx, y - rad*cos_dx])

def rotate(vec, phi):
    return np.array([[np.cos(phi), np.sin(phi)], [-np.sin(phi), np.cos(phi)]]).dot(vec)

"""
This is our main program.
"""
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode([600, 600])

pygame.display.set_caption("Bouncing Balls")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# wormtraj = [(200+i, 200 + 2 * np.sin(2*np.pi*i / 20)) for i in range(100)]
wormtraj = [np.array((200+i, 200)) for i in range(100)]
speed = 1.0
dir = np.array((1, 0))
dphi = 2*np.pi / 180 * 4

# -------- Main Program Loop -----------
done = False
stepcount = 0
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         print("I'M IN SPACE")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dir = rotate(dir, dphi)
    elif keys[pygame.K_RIGHT]:
        dir = rotate(dir, -dphi)
    elif keys[pygame.K_UP]:
        speed *= 1.02
    elif keys[pygame.K_DOWN]:
        speed /= 1.02
    elif keys[pygame.K_SPACE]:
        wormtraj = [wormtraj[-j] for j in range(len(wormtraj))]

    # --- Drawing
    # Set the screen background
    screen.fill(BLACK)


    stepcount = (stepcount + 1) % 70000
    dir = rotate(dir, 0.5*dphi*np.sin(stepcount/7))

    # wormtraj = wormtraj[1:] + (wormtraj[-1] + dir)
    wormtraj = wormtraj[1:] + [wormtraj[-1] + speed*dir]
    drawWorm(screen, wormtraj)

    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close everything down
pygame.quit()
