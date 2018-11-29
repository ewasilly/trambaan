import csv
import matplotlib.pyplot as plt
import networkx as nx
STATIONS = 'data/StationsHolland.csv'
CONNECTIONS = 'data/ConnectiesHolland.csv'

def make_list_of_row():
    """
    Isolates the coordinates of a station.
    """
    stations = {}
    with open(STATIONS, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            stations[row[0]] = (float(row[2]), float(row[1]))
    return stations


def isolate_connections():
    """
    Isolates connections from the ConnectiesHolland file.
    """
    reader = csv.reader(open(CONNECTIONS, 'r'))
    connections = []
    for row in reader:
        connections.append((row[0], row[1]))
    return connections


def make_graph(dict_of_units, list_of_connections):
    """
    Make a graph plot.
    """
    G = nx.Graph()
    name_list = []
    for i in dict_of_units.keys():
        G.add_node(i, pos=dict_of_units[i])

    # adding a list of edge tuples:
    print(type(list_of_connections), type(list_of_connections[0][0]))
    G.add_edges_from(list_of_connections)
    print(f"Nodes of graph: {G.nodes()}, so {G.number_of_nodes()} nodes.")
    print(f"Edges of graph: {G.edges()}, so {G.number_of_edges()} edges.")
    print(dict_of_units)
    nx.draw_networkx(G, pos=dict_of_units)
    # for i in dict_of_units.keys():
    #     plt.annotate(i, G.node[i]['pos'])
    plt.show()


if __name__ == "__main__":
    stations_list = make_list_of_row()
    connections_list = isolate_connections()
    make_graph(stations_list, connections_list)
