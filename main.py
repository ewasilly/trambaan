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
            id = id
            if row[3]:
                critical = True
                critical_ids.append(id)
            else:
                critical = False
            station = Station(name, id, critical)
            stations_dict[id] = station
            name_id_dict[name] = id
            id += 1

    return(stations_dict)

# inladen stations check:
stations_dict = load_stations(STATIONS)
# print(f"stationsdict: {stations_dict}")
# print(f"critical ids: {critical_ids}")



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
Vanaf hier wordt er wat aangekloot met trajecten
"""
# create random array of numbers to use as indices in all_connections
numbers = np.arange(100000)
np.random.shuffle(numbers)

# the length of all_connections can be used with modulo. More info later.
len = len(all_connections)

# generate a random number to use as starting connection in Traject
start = np.random.randint(low=1, high=len)

# Build a random Traject
first_traject = Traject(all_connections[start])
# Prevent going back and forth by keeping track of used indices
used = []
for i in numbers:
    index = i%len
    # using the Traject method add_connection, to add the connection at [i] in all_connections
    # modulo is used to prevent "index out of range list" error.
    first_traject.add_connection(all_connections[index])
    used.append(index)
print(first_traject)
print(first_traject.total_time)
