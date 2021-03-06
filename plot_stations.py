# Team Trambaan
# Made for the course Heuristieken
# This file contains a funtion that plots a traject

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random


def make_plottable(tr, map, plot_list):
    """
    This function takes all connections from tr and adds them to plot_list.
    tr is a Traject object
    map is which Map is used
    plot_list is a list of connections
    """

    # Change to list for easier manipulation
    list_of_connections = list(tr.connections)

    for conn in list_of_connections:
        # Retrieve stations, save names
        stat_from = map.stations_dict[conn.id_from].name
        stat_to = map.stations_dict[conn.id_to].name
        plot_list.append((stat_from, stat_to))


def traj_plot(tr, map, traject_nr):
    """
    Plots a traject object.
    tr is either the traject (class Traject) that you want to be plotted or a
    list of multiple trajects
    map is which Map is used,
    traject_nr is which traject you're plotting (for title)
    """

    # Create station name: coordinates dict
    coordinates_dict = {}
    critical_dict = {}
    for station in list(map.stations_dict.values()):
        coordinates_dict[station.name] = (float(station.coordinates[1]),
                                          float(station.coordinates[0]))

    # Check if more than one traject
    conn_plot_list = []
    if isinstance(tr, list):
        plot_multiple = True
        # Add to list of trajects to be plotted
        for traj in tr:
            new_plot_list = []
            make_plottable(traj, map, new_plot_list)
            conn_plot_list.append(new_plot_list)
    else:
        plot_multiple = False
        make_plottable(tr, map, conn_plot_list)

    G = nx.Graph()
    # Adding all stations, plotting
    G.add_nodes_from(coordinates_dict, color='b')
    if plot_multiple == True:
        # Plot each traject in random color
        for traj_plot_list in conn_plot_list:
            color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
            nx.draw_networkx(G, pos=coordinates_dict, edgelist=traj_plot_list,
                             with_labels=False, node_size=20, edge_color = color,
                             width=3)
    # If just one traject, plot that one in black
    else:
        nx.draw_networkx(G, pos=coordinates_dict, edgelist=conn_plot_list,
                         with_label=False, node_size=20, width=3)
    plt.title(f"Traject {traject_nr}")
    plt.xlabel("Breedtegraad")
    plt.ylabel("Lengtegraad")
    plt.show()
