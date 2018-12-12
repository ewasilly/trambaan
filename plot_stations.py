# Team Trambaan
# Made for the course Heuristieken
# This file contains some functions that you could use to plot trajects

import csv
import matplotlib.pyplot as plt
import networkx as nx

STATIONS = 'data/StationsHolland.csv'
CONNECTIONS = 'data/ConnectiesHolland.csv'


def all_plot(traj):
    """
    Combines some other functions to make a plot of a traject, i.e. a list of
    connections. The connections need to be in the format (id_from, id_to).
    """

    stations_dict = make_list_of_row()
    connections_list = isolate_connections()
    traj = fix_input(stations_dict, traj)
    make_graph(stations_dict, traj)


def fix_input(stat_dict, traject_conns):
    """
    Takes a traject (so a list of connection objects) and switches it to
    the names of the stations, so make_graph works on it.
    stat_dict is {station name: coordinates} with all stations
    traject_conns is a list of connection objects
    """

    conn_names_list = []

    # Take a connection, isolate the stations from and to
    for conn in traject_conns:
        conn = (conn.id_from, conn.id_to)
        # Switch id to name
        for id, stat in enumerate(stat_dict.keys()):
            if id == conn[0]:
                station_from = stat
            if id == conn[1]:
                station_to = stat

        # Make uple of the names and append to list
        tuple_of_conn = (station_from, station_to)
        conn_names_list.append(tuple_of_conn)

    return conn_names_list


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


def make_list_of_row():
    """
    Isolates the coordinates of a station.
    """

    stations = {}
    with open(STATIONS, 'r') as f:
        reader = csv.reader(f)
        # Make tuple of coordinates
        for row in reader:
            stations[row[0]] = (float(row[2]), float(row[1]))

    return stations


def traj_plot(tr, map):
    """
    Plots a traject object.
    tr is the traject (class Traject) that you want to be plotted.
    map is which Map is used.
    """

    list_of_connections = tr.connections

    # Create station name: coordinates dict
    coordinates_dict = {}
    for station in map.stations_dict:
        coordinates_dict[station.name] = station.coordinates

    conn_plot_list = []
    for conn in list_of_connections:
        # Retrieve stations, save names
        stat_from = map.stations_dict[conn.id_from].name
        stat_to = map.stations_dict[conn.id_to].name
        conn_plot_list.append((stat_from, stat_to))

    G = nx.Graph()

    # adding a list of edge tuples:
    G.add_edges_from(conn_plot_list)
    nx.draw_networkx(G, pos=coordinates_dict, node_color = 'r')
    plt.title("K-waarde hier")
    plt.show()


if __name__ == "__main__":
    all_plot([(0,1)])
