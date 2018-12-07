import csv
import matplotlib.pyplot as plt
import networkx as nx

STATIONS = 'data/StationsHolland.csv'
CONNECTIONS = 'data/ConnectiesHolland.csv'


def fix_input(stat_dict, traject_of_ids):
    """
    Takes a list of ids of connections used in a traject and switches it to
    the names, so make_graph works on it.
    """

    output_list = []

    for conn in traject_of_ids:
        conn = (conn.id_from, conn.id_to)
        for id, stat in enumerate(stat_dict.keys()):
            if id == conn[0]:
                station_from = stat
            if id == conn[1]:
                station_to = stat
        tuple_of_conn = (station_from, station_to)
        output_list.append(tuple_of_conn)

    return output_list


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


def make_graph(dict_of_stations, list_of_connections):
    """
    Make a graph plot.
    """
    G = nx.Graph()

    # adding a list of edge tuples:
    G.add_edges_from(list_of_connections)
    nx.draw_networkx(G, pos=dict_of_stations, node_color = 'r')
    plt.title("K-waarde hier")
    plt.show()


def all_plot(traj):
    """
    Combines some other functions to make a plot of a traject, i.e. a list of
    connections. The connections need to be in the format (id_from, id_to).
    """

    stations_dict = make_list_of_row()
    connections_list = isolate_connections()
    traj = fix_input(stations_dict, traj)
    make_graph(stations_dict, traj)


if __name__ == "__main__":
    all_plot([(0,1)])
