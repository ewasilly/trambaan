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
# print(f"all connections: {all_connections}")
# print(f"All connections: {all_connections}\n")
# print(f"Critical connections: {critical_connections}\n")


"""
Create trajects
"""

def back_track(traject, last_track, used_depth):
    print("Inside BACKTRACK")
    traject.connections.pop()
    last_id = traject.connections[-1].id_to
    print(last_track)
    print(last_id)
    for track in last_track:
        if track not in used_depth:
            possibilities.append(track)


def traject_generator_depth(all_connections):
    # create random array of numbers to use for indexing through connections
    numbers = np.arange(10000)
    random.shuffle(numbers)
    trajects = {}

    # length of connections = the amount of stations in this list.
    length = len(stations_dict)

    # List to save the possible connections from a certain station
    possibilities = []
    possible_time = []
    last_track = []

    s = 0
    # loop through stations
    while s < 8:

        pos_starts = []
        pos_times = []

        start = stations_dict[s].id
        print(f"station id = {start}")

        children = 0
        for conn in all_connections:
            if conn.id_from == start:
                pos_starts.append(conn)
                pos_times.append(conn.time)

        if len(pos_starts) == 0:
            print("dead end station")
            s += 1
        else:
            # dit slaat ie over als er geen opties zijn, en dan gaat ie terug naar boven met hogere s
            for conn in pos_starts:
                if conn.time == min(pos_times):
                    start_connection = conn
                    c = 0
                    traject = Traject(start_connection)
                    print(traject)
                    print("START traject\n")
                    used_depth = []
                    s += 1

        while traject.total_time < 120:

            last_id = traject.connections[-1].id_to

            # search for the possible connections
            for connection in all_connections:
                # if start is starting point of a connection, add to possibilities
                if connection.id_from == last_id
                    # print("Match")
                    possibilities.append(connection)
                    possible_time.append(connection.time)


            if len(possibilities) == 0:
                trajects[f"S{s}- c{c}"] = traject
                c += 1

                if len(traject.connections) > 1:
                    print("BACKTRACKING: ...")
                    popped = traject.connections.pop()
                    print(traject)
                    print(traject.last_id)
                    print("last track INSIDE :")
                    print(last_track)
                    possibilities.clear()
                    for track in last_track:
                        if track != popped:
                            possibilities.append(track)
                            possible_time.append(track.time)
                            c += 1
                            print("gotta use this one:")
                            print(track)

                else:
                    print("nobacktrack")
                    c -= 1
                    break
                # print("BACKTRACKING: .....")
                # back_track(traject, last_track)


            # add the shortest connection
            for connection in possibilities:
                print("possibilities:")
                print(connection)
                if connection.time == min(possible_time):
                    print("shortest:")
                    print(connection)
                    traject.add_connection(connection)
                    print(traject)
                    used_depth.append(connection)



            last_track = possibilities.copy()

            possibilities.clear()
            possible_time.clear()

            # oke er is iets met het overwriten van possibilities en last_track



    # print(f"traject: {traject}")
    return(trajects)







# assign the output of traject_generator_deph into new variable
test = traject_generator_depth(all_connections)
#used_depth = traject_generator_depth(used_depth)
print(test)

connections_bt = []
possibilities_bt = []




# function for backtracking
def backtrack(traject):
    print(f"backtrack_connectie: {traject.connections[-1]}")
    print(f"backtrack station: {traject.connections[-1].id_from}")
    i = 0
    #for i in range(len(traject - 1)):
    for connection in all_connections:
        # backtrack through traject
        # search for other unvisited possible stations per station
        if traject.connections[-2-i].id_from == connection.id_from:
            connections_bt.append(traject.connections[-2-i].id_from)

    for connections in traject:
        print(connection)

    #for connection in connections_bt:
    #    if connection not in used_depth:
    #        possibilities_bt.append(connection)


#print(f"used depth: {used_depth}")
print(f"connections_bt: {connections_bt}")
print(f"possibilities_bt: {possibilities_bt}")





    #for connection in all_connections:
    #    if
    #return

# backtrack(traject)








# K de kwaliteit van de lijnvoering is, p de fractie van de bereden kritieke verbindingen (dus tussen 0 en 1),
# T het aantal trajecten en Min het aantal minuten in alle trajecten samen.
