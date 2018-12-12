"""
The current script:

>>> Loads in all Connections en Stations
>>> Declares the lists: stations_ids,  all_connections,  critical_connections
>>> defines the class Stack()
>>> defines K_calculator()
    >>>>> Is able to call the algoritms in the folder trambaan/code/algoritms


hieronder staat nu breadth first van wuter
"""

import csv
import random
import sys
import numpy as np
import matplotlib.pyplot as plt
import collections
import copy

sys.path.insert(0, 'code/classes/')
from station import Station
from traject import Traject
from connection import Connection
sys.path.insert(1, 'code/algorithms/')
from greedy import traject_generator_Greedy_new
from hillclimber_basic import hillclimber
from hillclimber_SA import hillclimber_SA
from breadthfirst import traject_generator_BF
from helpers import *
from plot_stations import all_plot


STATIONS = 'data/StationsHolland.csv'
CONNECTIONS = 'data/ConnectiesHolland.csv'

# Dictionary {id: Stationobject}
stations_dict = {}
# Dictionary {name : id}
name_id_dict = {}
#  List with critical station ids
critical_ids = []
# Array with all connection objects
all_connections = []
# Subset of critical connection objects
critical_connections = []



def load_stations(infile):
    """
    Loads stations from StationsHolland.csv into dictionary {id: stationobject}
    Also adds every critical id to the critical_ids list.
    """
    with open(infile, 'r') as f:
        reader = csv.reader(f)
        id = 0
        for row in reader:
            name = row[0]
            # check whether station is critical
            if row[3]:
                critical = True
                critical_ids.append(id)
            else:
                critical = False
            # create station with all attributes
            station = Station(name, id, critical)
            # add station to dictionary
            stations_dict[id] = station
            name_id_dict[name] = id
            id += 1

    return(stations_dict)

stations_dict = load_stations(STATIONS)



def load_connections(infile):
    """
    Loads all connections in connectiesHolland.csv as objects into a list.
    """
    with open(infile, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # Alkmaar
            name_from = row[0]
            # Hoorn
            name_to = row[1]
            # 24
            time = int(row[2])
            # Find the id of these stations:
            id_from = name_id_dict[name_from]
            id_to = name_id_dict[name_to]
            # make the connection object and add to all_connections
            connection = Connection(id_from, id_to, time)
            all_connections.append(connection)

            # add to critical_connections if either of two ids is critical
            if id_from in critical_ids or id_to in critical_ids:
                critical_connections.append(connection)

    return(all_connections)

# inladen connecties check:
load_connections(CONNECTIONS)
# print(f"All connections: {len(all_connections)}\n")
# print(f"Critical connections: {len(critical_connections)}\n")


def traject_generator_Greedy_new(connections, critical_connections, nr_of_trajects, min_time):

    # this will be the output dictionary
    trajects_db = {}
    # length of connections = the nr of connections
    len_all = len(connections)
    len_crit = len(critical_connections)

    # build a stack to prevent to ensure use of all connections
    stack_all = Stack(connections)
    stack_crit = Stack(critical_connections)

    def shuffle_stacks():
        random.shuffle(stack_all.array)
        random.shuffle(stack_crit.array)

    i = 0
    while i < nr_of_trajects:
        shuffle_stacks()
        start_connection = stack_all.take()
        traject = Traject(start_connection)
        # dictionary for this startconnection
        tries = 0
        rounds = 0

        while tries < 1000:

            time_before = traject.total_time
            for j in range(len_crit):
                traject.add_connection(stack_crit.take())
                tries += 1
                traject.add_connection(stack_all.take())
                tries += 1
            time_after = traject.total_time
            rounds += 1
            shuffle_stacks()

            if time_after > min_time:
                trajects_db[f"Traject{start_connection}-{traject.total_time}"]= traject
                i += 1

            # if connection is a dead end
            if time_before == time_after:
                break

    return(trajects_db)


#  Create a trajects database
trajects_db = traject_generator_Greedy_new(all_connections, critical_connections, 1000, 7)
# print(trajects_db)
# print(len(trajects_db))

traject_voor_jasper = list(trajects_db.values())[61]
all_plot(traject_voor_jasper.connections)

#  create a starting set of 3 trajects to use for the hillclimber
start_set = {}
for i in range(5):
    traject = list(trajects_db.values())[i]
    start_set[i] = traject

final = hillclimber(start_set, trajects_db, 7, 1000, critical_connections, all_connections)

print(f"finalset = {final}")
print(K_calculator(final, critical_connections, all_connections))
print(f"start_set = {start_set}")
print(K_calculator(start_set, critical_connections, all_connections))

# K_dist = []
# for j in range(10):
#
#     #  create a starting set of 3 trajects to use for the hillclimber
#     start_set = {}
#     for i in range(3):
#         traject = list(trajects_db.values())[i]
#         start_set[i] = traject
#
#     final = hillclimber(start_set, trajects_db, 7, 1000, critical_connections, all_connections)
#     print(final)
#     K = K_calculator(final, critical_connections, all_connections)
#     K_dist.append(K)
#
#
#
#
# plt.hist(K_dist, bins=50)
# plt.title("K spread Stochastic hillclimber - 1000 iterations - startset 3 trajects")
# plt.show()




#
# with open('linevoering.csv', 'w') as f:
#     w = csv.DictWriter(f, fieldnames=final.keys())
#     w.writeheader()
#     w.writerow(final)
