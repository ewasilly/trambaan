import csv
import matplotlib.pyplot as plt
import networkx as nx
STATIONS = 'data/StationsHolland.csv'

def make_list_of_row():
    """
    Isolates the coordinates of a station.
    """
    stations = {}
    with open(STATIONS, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            stations[row[0]] = (row[1], row[2])
    return stations


def make_graph(dict_of_units):
    """
    Make a nice graph plot.
    """
    G = nx.Graph()
    name_list = []
    for i in dict_of_units.keys():
        G.add_node(i, pos=dict_of_units[i])

    # # adding a list of edges:
    # G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])
    # print(f"Nodes of graph: {G.nodes()}, so {G.number_of_nodes()} nodes.")
    # print(f"Edges of graph: {G.edges()}, so {G.number_of_edges()} edges.")
    nx.draw(G, dict_of_units)
    for i in dict_of_units.keys():
        plt.annotate(i, G.node[i]['pos'])
    plt.show() # display

if __name__ == "__main__":
    stations_list = make_list_of_row()
    make_graph(stations_list)
