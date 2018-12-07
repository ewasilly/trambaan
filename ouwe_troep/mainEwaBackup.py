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

def K_calculator(trajects):

    used_conns = []
    used_crit = []
    total_minutes = []
    for traject in trajects:
        total_minutes.append(traject.total_time)
        for conn in traject.connections:
            used_conns.append(conn)
            if conn in critical_connections:
                used_crit.append(conn)

    # fraction of used connections
    f= len(collections.Counter(used_conns))/len(all_connections)

    p = len(collections.Counter(used_crit))/ len(critical_connections)
    t = len(traject.connections)
    total_minutes = sum(total_minutes)
    K = p*10000 - (t*20 + total_minutes/10)

    # print(f"F: {f}")
    # print(f"P: {p}\n")
    # print(f"K: {K}")

    return(K)

traject = Traject
# Note on connections; choose critical_connections OR all_connections
def traject_generator_depth(connections):

    # List to save the possible connections from a certain station
    possibilities = []
    possible_time = []
    length = len(connections)

    # generate a random number to use as starting station in Traject
    start = random.choice(range(length))
    # start = 2
    dict_trajects = {}

    # Ensure that no more than 7 trajects are made
    # Don't forget to change 1 to 7!
    i = 0
    time = 0
    while i < 1:
        # while loop to make one traject
        while time < 100:
            possibilities.clear()
            possible_time.clear()
            # search for the possible connections from start
            for connection in all_connections:
                # if start is starting point of a connection, add to possibilities
                if start == connection.id_from:
                    possibilities.append(connection)

            # search for the possible connection with the shortest time
            for connection in possibilities:
                possible_time.append(connection.time)

            if len(possibilities) == 0:
                start = random.choice(range(length))
                break

            min_time = min(possible_time)


            for connection in possibilities:
                if connection.time == min_time:
                    if i == 0:
                        traject = Traject(connection)
                        # add station to dictionary
                        # name_key = stations_dict[connection.id_from][0]
                        # print(name_key)

                        time = time + connection.time
                        start = connection.id_to
                    else:
                        traject.add_connection(connection)
                        time = time + connection.time
                        start = connection.id_to


            i += 1

        naam = stations_dict[1].name

        # print(f"traject: {traject}")
        # print(f"dict_trajects: {dict_trajects}")
        # print(f"stations_dict[1]: {naam}")

    # print(f"connection added: {connection}")
    # print(f"Traject: {traject}\n"
    #       f"Time: {traject.total_time}")

    # Try again if traject too short
    if traject.total_time < 60:
        traject = traject_generator_depth(connections)

    return traject


if __name__ == "__main__":
    traject_list = []
    while len(traject_list) < 7:
        traject_temp = traject_generator_depth(all_connections)
        if traject_temp in traject_list:
            print("Not added:")

        # print(traject_list)
        else:
            traject_list.append(traject_temp)
        print(f"Traject created: {traject_temp}")
    print(f"K value:{K_calculator(traject_list)}")
