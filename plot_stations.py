import matplotlib.pyplot as plt
import networkx as nx
STATIONS = 'StationsHolland.csv'

def average_minutes():
    """
    Isolates the coordinates of a station.
    """
    stations_ = []
    with open(STATIONS, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            minutes_list.append(int(row[2]))
    return np.mean(minutes_list)

G=nx.Graph()
G.add_node("a")
G.add_nodes_from(["b","c"])

G.add_edge(1,2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)

# Input: [(1,5), (8,4), ...]
for i in G:
    print(G[i])
# adding a list of edges:
G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])
print(f"Nodes of graph: {G.nodes()}, so {G.number_of_nodes()} nodes.")
print(f"Edges of graph: {G.edges()}, so {G.number_of_edges()} edges.")
nx.draw(G)
# plt.savefig("simple_path.png") # save as png
# for i, name in enumerate(G.nodes()):
#     plt.annotate(name, G.node["a"]['pos'])
plt.show() # display
