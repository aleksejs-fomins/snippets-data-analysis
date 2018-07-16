import matplotlib.pyplot as plt
import matplotlib.axes as axes

CELL_WIDTH = 0.02
CELL_GAP = 0.01
N_CELL_X = 100
N_CELL_Y = 10

CELL_DELTA = CELL_WIDTH+CELL_GAP

cell_pos = [(i*CELL_DELTA, j*CELL_DELTA)
              for i in range(0, N_CELL_X) for j in range(0, N_CELL_Y)]

cells = [plt.Rectangle(pos, CELL_WIDTH, CELL_WIDTH, color='r', clip_on=False) for pos in cell_pos]

fig, ax = plt.subplots()

for c in cells:
    ax.add_artist(c)

cells[1].set_color('b')


plt.axis('off')
plt.show()