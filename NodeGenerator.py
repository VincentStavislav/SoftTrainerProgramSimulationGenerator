import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class NodeGenerator:
    
    def create_node(node):
        simu = nx.Graph()
        simu.add_node(node)
        simu.nodes()
        return simu
    
    def create_edge(simu, node, sec_node):
        simu.add_node(sec_node)
        simu.add_edge(node, sec_node)
        return simu
    
    def node_draw(simulation):

        return 0
    pass



simulationGenerator = NodeGenerator()
simulation = simulationGenerator.create_node(1)
nx.draw_planar(simulation, with_labels=True) #shape without edge crossing(not intersect)
plt.show()
g = nx.Graph()
# multig = nx.MultiDiGraph()

# g.add_node(1)
# g.add_edge(2, 3, waight=0.3) #2 and 3 nodes ware automaticly added
# g.add_node("Str as object")
# g.add_edge("Str as object", "draw value of a node")

#   Draw graph without and with labels
# nx.draw_spring(g)
# plt.show()

# nx.draw_spring(g, with_labels=True)
# plt.show()

#   Create graph from tuple
# edge_list = [(3, 4), (2, 5), (4, 5), (1, 5), (1, 1)]
# g.add_edges_from(edge_list)

#  Theory: adjacency matrix is a square matrix used to represent a finite graph.
#  elements of matrix indicates conection where 1 between two crossaxіs means connection

#   Create graph from adjacency matrix
# ajc_matrix = np.array([[0, 1, 1],
#                        [1, 1, 0],
#                        [1, 0, 1]])
# g = nx.from_numpy_array(ajc_matrix)

#   Create graph from array
g_array = np.array([(3, 4), (2, 8), (4, 5), (1, 8), (1, 1), (5, 7), (9, 8), (7, 9)])
g.add_edges_from(g_array)

#   Nodes draw position(shapes)
# nx.draw_spring(g, with_labels=True) #spring shape
# plt.show()

# nx.draw_circular(g, with_labels=True) #cirular shape
# plt.show()

# nx.draw_shell(g, with_labels=True) # invertial to circular
# plt.show()

# nx.draw_spectral(g, with_labels=True) #spectral 2D layout
# plt.show()

# nx.draw_random(g, with_labels=True) #draw in random positioning every time
# plt.show()

nx.draw_planar(g, with_labels=True) #shape without edge crossing(not intersect)
plt.show()


