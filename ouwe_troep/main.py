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



# inladen stations check:
stations_dict = load_stations(STATIONS)
# print(f"stationsdict: {stations_dict}")
# print(f"critical ids: {critical_ids}")

print(name_id_dict)


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
print(f"All connections: {all_connections}")
print(f"Critical connections: {critical_connections}")




class Stack():
    def __init__(self, array):
        self.array = array

    #  takes first item and puts it back at the end of the array
    def take(self):
        taken = self.array[0]
        self.array.pop(0)
        self.array.append(taken)
        return(taken)

    def __repr__(self):
        return(f"{self.array}")


def K_calculator(trajects):

    used_conns = []
    used_crit = []
    total_minutes = []
    for key in trajects.keys():
        traject = trajects[key]
        total_minutes.append(traject.total_time)
        for conn in traject.connections:
            used_conns.append(conn)
            if conn in critical_connections:
                used_crit.append(conn)

    # fraction of used connections
    f= len(collections.Counter(used_conns))/len(all_connections)

    p = len(collections.Counter(used_crit))/ len(critical_connections)
    t = len(trajects.keys())
    total_minutes = sum(total_minutes)
    K = p*10000 - (t*20 + (total_minutes/10))

    print(f"F: {f}")
    print(f"P: {p}")
    print(f"K: {K}\n")

    return(K)




"""
Create routes
"""
# create random array of numbers to use as indices in all_connections
numbers = np.arange(10000)
np.random.shuffle(numbers)

# the length of all_connections can be used with modulo. More info later.
len = len(critical_connections)

# generate a random number to use as starting connection in Traject
start = np.random.randint(low=1, high=len)
print(f"startconnectie is: {start}")

# Build a random Traject
traject = Traject(critical_connections[start])
# Prevent going back and forth by keeping track of used indices
length_used = 0
used = []

for i in range(7):
    for j in numbers:
        # modulo is used to prevent "index out of range list" error.
        index = j % len
        # using the Traject method add_connection, to add the
        # connection at [j] in all_connections
        traject.add_connection(critical_connections[index])
        if critical_connections[index] not in used:
            used.append(critical_connections[index])
            length_used += 1
    if length_used == len:
        break


print(f"used: {used}")
print(f"len: {len}")

print(f"Critical connections route: {traject}")
print(f"Total time critical connections route: {traject.total_time}")
