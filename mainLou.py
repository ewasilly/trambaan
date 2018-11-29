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
# Note on connections; choose critical_connections OR all_connections
def traject_generator_greedy(connections, nr_of_trajects, min_time):

    trajects = {}
    # count the use of connections during all trajects
    used_all = []
    # keep track of total time, will be used in objective function
    total_minutes = []
    # keep track of used critical connections
    used_critical = []
    # length of connections = the amount of connections in this list.
    length = len(connections)

    counter = collections.Counter(connections)

    i = 1
    while i < nr_of_trajects:
        random.shuffle(connections)
        # generate a random starting connection for the Traject
        start = random.choice(range(length))
        traject = Traject(connections[start])
        while traject.total_time <= 120:
            tries = 1
            random.shuffle(connections)
            for index in range(length):
                # add connection if not yet in traject and not yet used more than 3 times
                if connections[index] not in traject.connections and counter[connections[index]] <= 2:
                    traject.add_connection(connections[index])
                    tries += 1
            # if the total time of the current traject overceeds min_time use this traject.
            if traject.total_time >= min_time:
                print("BUAAA")
                trajects[f"Traject {i}."] = (traject, traject.total_time)
                total_minutes.append(traject.total_time)
                i += 1
                # add connections in this traject to used_all, eventually the use through all 7 trajects will be counted
                for conn in traject.connections:
                    used_all.append(conn)
                    counter = collections.Counter(used_all)
                    if conn in critical_connections:
                        used_critical.append(conn)
                break
            elif tries == 500:
                break
            # if the traject is too short, start over.
            else:
                break



    p = len(collections.Counter(used_critical)) / len(critical_connections)
    t = len(trajects.keys())
    total_minutes = sum(total_minutes)
    K = p*10000 - (t*20 + total_minutes/10)
    f= len(counter)/len(connections)
    print(p)
    print(f"Greedy approach trajects output: {trajects} \n")
    print(f"Fraction: {f}\n")
    print(f"K: {K}\n")
    print(counter)
    return(K)




K_distribution = []
for i in range(10):
    K = traject_generator_greedy(all_connections, 6, 80)
    K_distribution.append(K)

plt.hist(K_distribution, bins='auto')
plt.title("K spread - 500 iterations - 5 trajects, min 80 minutes")
plt.show()


# K de kwaliteit van de lijnvoering is, p de fractie van de bereden kritieke verbindingen (dus tussen 0 en 1),
# T het aantal trajecten en Min het aantal minuten in alle trajecten samen.
