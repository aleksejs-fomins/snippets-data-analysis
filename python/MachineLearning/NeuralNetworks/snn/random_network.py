import time
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# INIT RNG
np.random.seed(int(time.time()))

# CONSTANTS
N_NODES = 100
P_EDGE = 0.3

# Generate edge map
edge_tuplelist = []
for i in range(0, N_NODES):
    for j in range (0, i-1):
        if np.random.uniform(0.0, 1.0, 1)[0] < P_EDGE:
            edge_tuplelist.append((str(i), str(j)))

G = nx.DiGraph()
G.add_edges_from(edge_tuplelist)

colors = np.random.uniform(0.0, 1.0, N_NODES)
val_map = dict([(str(i), it) for i, it in enumerate(colors)])

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
red_edges = [edge_tuplelist[0], edge_tuplelist[1]]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
#pos = nx.spring_layout(G)
#nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = values, with_labels = True)
#nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
#nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
nx.draw(G, with_labels=True, node_color= values, edge_color='gray')
plt.show()