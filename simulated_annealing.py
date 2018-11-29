"""
main.py
>>> Loads all Connections en Stations
>>> Moet  stations_ids,  all_connections,  critical_connections  lists declareren
>>>>> Bevat het algoritme om trajecten mee op te bouwen. (depth-first?????)
        >>>> Dit moet in main omdat het al het bovenstaande nodig heeft.

Station.py
>>> bevat de class Station
Connection.py
>>> bevat de class Connection
Traject.py
>>> bevat de class traject
"""

import csv
import random
import sys
import numpy as np
import matplotlib.pyplot as plt
import collections

sys.path.insert(0, 'code/classes/')
from station import Station
from traject import Traject
from connection import Connection


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
# print(f"All connections: {all_connections}\n")
# print(f"Critical connections: {critical_connections}\n")


"""
Create trajects
"""

# def count_critical(connections_array, critical_connections):
#
#     for conn in connections_array:
#         if conn in critical_connections:
#             used_crit.append(conn)
#
#     counter = collections.Counter(used_crit)
#     return(len(counter))
class Stack():
    def __init__(self, array):
        self.array = array
    #  takes first item and puts it last in the array
    def take(self):
        taken = self.array[0]
        self.array.pop(0)
        self.array.append(taken)
        return(taken)
    def __repr__(self):
        return(f"{self.array}")


# Note on connections; choose critical_connections OR all_connections
def traject_generator_greedy(connections, nr_of_trajects, min_time):

    # this will be the output dictionary
    trajects = {}
    # keep track of used connections during all trajects
    used_all = []
    # keep track of use of connections; first we start it for all possible connections
    counter = collections.Counter(connections)
    # length of connections = the amount of possible connections
    length = len(connections)

    # keep track of critical connections used
    used_critical = []
    goal = len(critical_connections)
    count_critical = 0

    i = 0
    tries = 0
    while i < nr_of_trajects and tries < 1000:
        # prevent using the same order of presenting options
        random.shuffle(connections)

        # since already shuffled, take the first connection as starting point for the traject
        traject = Traject(connections[0])

        # keep track of tries, to use as break mechanism in case of dead ends
        stack_all = Stack(connections)
        stack_crit = Stack(critical_connections)
        while traject.total_time <= 120 and tries < 1000:
            first_c = stack_crit.take()
            first_a = stack_all.take()
            # first try adding a critical connection, if not yet in traject and not yet used more than 3 times
            if first_c not in traject.connections and counter[first_c] <= 3:
                traject.add_connection(first_c)
                print(traject.connections, traject.total_time)
                tries += 1
            # else try one from all connections
            elif first_a not in traject.connections and counter[first_a] <= 3:
                traject.add_connection(first_a)
                tries += 1
                # print(f"A{first_a}")
            if tries >= 100:
                # if the total time of the current traject exceeds min_time use this traject.
                if traject.total_time >= min_time:
                    trajects[f"Traject {i}."] = traject
                    print("BUAAH")
                    i += 1
                    # add connections in this traject to used_all, eventually the use through all 7 trajects will be counted
                    for conn in traject.connections:
                        print(conn)
                        used_all.append(conn)
                        counter = collections.Counter(used_all)
                        print(counter(first_c))
                        if conn in critical_connections:
                            used_critical.append(conn)
                            count_critical = len(collections.Counter(used_critical))
                            print(counter)
                    break
            else:
                break


    return(trajects)


def K_calculator(trajects, all_connections, critical_connections):

    used_conns = []
    used_crit = []
    total_minutes = []
    for traject in trajects:
        total_minutes.append(traject.total_time)
        for conn in traject:
            used_conns.append(conn)
            if conn in critical_connections:
                used_crit.append(conn)

    # f is eigenlijk alleen voor ons interessant, fractie gebruikte connecties
    f= len(collections.Counter(used_conns))/len(all_connections)

    p = len(collections.Counter(used_crit))/ len(critical_connections)
    t = len(trajects.keys())
    total_minutes = sum(total_minutes)
    K = p*10000 - (t*20 + total_minutes/10)

    print(f"Greedy approach trajects output: {trajects} \n")
    print(f"Fraction: {f}\n")
    print(p)
    print(f"K: {K}\n")

    return(K)


def hillclimber(trajects):

    old_K = K_calculator(trajects)





trajects = traject_generator_greedy(all_connections, 7, 60)
print(trajects)








# K de kwaliteit van de lijnvoering is, p de fractie van de bereden kritieke verbindingen (dus tussen 0 en 1),
# T het aantal trajecten en Min het aantal minuten in alle trajecten samen.
