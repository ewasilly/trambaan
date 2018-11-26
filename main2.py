"""
main.py
>>> Moet alle Connections en Stations inladen
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

STATIONS = 'StationsHolland.csv'
CONNECTIONS = 'ConnectiesHolland.csv'

import csv
import random
import numpy as np
import collections
from station import Station
from traject import Traject
from connection import Connection


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



# inladen stations check:
stations_dict = load_stations(STATIONS)
# print(f"stationsdict: {stations_dict}")
# print(f"critical ids: {critical_ids}")

# print(name_id_dict)


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
# print(f"All connections: {all_connections}")
# print(f"Critical connections: {critical_connections}")


"""
Create routes
"""
# create random array of numbers to use as indices in all_connections
numbers = np.arange(10000)
trajects = {}

# OPTION: choose between critical or all connections
connections = all_connections
print(connections)
print(connections[4])

# count the use of connections during all 7 trajects
used_all = []
# keep track of total time, will be used in objective function
total_minutes = []
# keep track of used critical connections
used_critical = []

# the length of all_connections can be used with modulo. More info later.
length = len(connections)

i = 1
# arbitrary :
min_time = 50
while i < 7:
    # generate a random number to use as starting connection in Traject
    start = random.choice(range(length))
    traject = Traject(connections[start])
    # # Prevent going back and forth by keeping track of used connections
    # used = []
    tried = 1
    while traject.total_time <= 120:
        # modulo is used to prevent "index out of range list" error.
        j = random.choice(numbers)
        index = j % length
        # using the Traject method add_connection, to add the connection at [j] in all_connections
        if connections[index] not in traject.connections:
            traject.add_connection(connections[index])
            tried += 1
        # if every connection has been tried:
        if tried == length:
            # if the total time of the current traject overceeds min_time use this traject.
            if traject.total_time >= min_time:
                trajects[f"Traject{i}."] = traject
                total_minutes.append(traject.total_time)
                i += 1
                # add connections in this traject to used_all, eventually the use through all 7 trajects will be counted
                for conn in traject.connections:
                    used_all.append(conn)
                    if conn in critical_connections:
                        used_critical.append(conn)
                break
            # if the traject is too short, start over.
            else:
                break


print(f"De opgestelde trajecten zijn: {trajects}")
counter = collections.Counter(used_all)
print(counter)

p = len(used_critical) / len(critical_connections)
t = len(trajects.keys())
total_minutes = sum(total_minutes)
K = p*10000 - (t*20 + total_minutes/10)
print(f"K is {K}")
# K de kwaliteit van de lijnvoering is, p de fractie van de bereden kritieke verbindingen (dus tussen 0 en 1),
# T het aantal trajecten en Min het aantal minuten in alle trajecten samen.
