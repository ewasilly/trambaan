import csv
import matplotlib.pyplot as plt
import networkx as nx
STATIONS = 'data/StationsHolland.csv'
CONNECTIONS = 'data/ConnectiesHolland.csv'

def make_list_of_row():
    """
    Isolates the coordinates of a station.
    """
    stations_c = {}
    stations_n = {}
    with open(STATIONS, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[3] == "Kritiek":
                stations_c[row[0]] = (float(row[2]), float(row[1]))
            else:
                stations_n[row[0]] = (float(row[2]), float(row[1]))

    return stations_c, stations_n


def isolate_connections():
    """
    Isolates connections from the ConnectiesHolland file.
    """
    reader = csv.reader(open(CONNECTIONS, 'r'))
    connections = []
    for row in reader:
        connections.append((row[0], row[1]))
    return connections


def make_graph(dict_of_crits, dict_of_not, list_of_connections):
    """
    Make a graph plot.
    """
    G = nx.Graph()

    # adding a list of edge tuples:
    G.add_edges_from(list_of_connections)
    nx.draw_networkx(G, pos=dict_of_crits, node_color = 'b')
    nx.draw_networkx(G, pos=dict_of_not, node_color = 'r')
    plt.show()


if __name__ == "__main__":
    stations_crit, stations_not = make_list_of_row()
    connections_list = isolate_connections()
    make_graph(stations_crit, stations_not, connections_list)
