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
print(f"all connections: {all_connections}")
# print(f"All connections: {all_connections}\n")
# print(f"Critical connections: {critical_connections}\n")


"""
Create trajects
"""

traject = Traject
# Note on connections; choose critical_connections OR all_connections
def traject_generator_depth(connections):

    # create random array of numbers to use for indexing through connections
    numbers = np.arange(10000)
    trajects = {}
    # count the use of connections during all trajects
    used_all = []
    # keep track of total time, will be used in objective function
    total_minutes = []
    # keep track of used critical connections
    used_critical = []
    # length of connections = the amount of stations in this list.
    length = len(stations_dict)


    # List to save the possible connections from a certain station
    possibilities = []
    possible_time = []

    # generate a random number to use as starting station in Traject
    #start = random.choice(range(length))
    start = 2
    dict_trajects = {}

    # Ensure that no more than 7 trajects are made
    # Don't forget to change 1 to 7!!!
    i = 0
    time = 0
    while i < 1:
        # while loop to make one traject
        while time < 120:
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
                break

            min_time = min(possible_time)

            print(f"possibilities: {possibilities}")
            print(f"possible_time: {possible_time}")
            print(f"min_time: {min_time}")

            # make dictionary per station
            for value in stations_dict:
                if value != "True" and value != "False":
                    value = {}


            for connection in possibilities:
                if connection.time == min_time:
                    if i == 0:
                        traject = Traject(connection)
                        # add station to dictionary
                        name_key = stations_dict[connection.id_from][0]
                        print(name_key)

                        time = time + connection.time
                        start = connection.id_to
                    else:
                        traject.add_connection(connection)
                        time = time + connection.time
                        start = connection.id_to


            i += 1


        print(f"traject: {traject}")
        print(f"dict_trajects: {dict_trajects}")
        print(f"stations_dict: {stations_dict}")

    return

traject_generator_depth(all_connections)





        #tried = 1
        #while traject.total_time <= 120:
            # using the Traject method add_connection, to add the connection at [j] in all_connections
        #    if connections[index] not in traject.connections:
        #        traject.add_connection(connections[index])
        #        tried += 1
            # if every connection has been tried:
        #    if tried == length:
                # if the total time of the current traject overceeds min_time use this traject.
        #        if traject.total_time >= min_time:
        #            trajects[f"Traject {i}."] = (traject, traject.total_time)
        #            total_minutes.append(traject.total_time)
        #            i += 1
                    # add connections in this traject to used_all, eventually the use through all 7 trajects will be counted
        #            for conn in traject.connections:
        #                used_all.append(conn)
        #                if conn in critical_connections:
        #                    used_critical.append(conn)
        #            break
                # if the traject is too short, start over.
        #        else:
        #            break

    #p = len(used_critical) / len(critical_connections)
    #t = len(trajects.keys())
    #total_minutes = sum(total_minutes)
    #K = p*10000 - (t*20 + total_minutes/10)

    #return(K)

    # print(f"Greedy approach trajects output: {trajects} \n")
    # # Counter lists the use of all connections
    # counter = collections.Counter(used_all)
    # print(f"Counter: {counter}\n")


#K_distribution = []
#for i in range(100):
#    K = traject_generator_greedy(all_connections, 7, 90)
#    K_distribution.append(K)

#print(K_distribution)
#plt.hist(K_distribution, bins='auto')  # arguments are passed to np.histogram
#plt.title("K spread - 100 iterations - 6 trajects, 90 minutes max")
#plt.show()






# K de kwaliteit van de lijnvoering is, p de fractie van de bereden kritieke verbindingen (dus tussen 0 en 1),
# T het aantal trajecten en Min het aantal minuten in alle trajecten samen.
