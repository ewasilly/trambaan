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
print(f"All connections: {len(all_connections)}\n")
print(f"Critical connections: {len(critical_connections)}\n")


"""
Create trajects
"""

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
    K = p*10000 - (t*20 + total_minutes/10)

    print(f"F: {f}")
    print(f"P: {p}\n")
    print(f"K: {K}")

    return(K)




'''
This traject generator creates an arbitrary nr of trajects and returns a traject_database (dictionary)
The key is defined as startconnection - total_time. This way, the same trajects will be overwritten
resulting in no duplicates in the traject database
'''
def traject_generator_new(connections, nr_of_trajects, min_time):

    # this will be the output dictionary
    trajects = {}
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
                trajects[f"Traject{start_connection}-{traject.total_time}"]= traject
                i += 1


            # if connection is a dead end
            if time_before == time_after:
                break

    return(trajects)


# changing_set is used to specify which traject will be changed
def hillclimber(startset, trajects_db, changing_set):

    old_K = K_calculator(startset)
    print(f"old_K: {old_K}")

    possible_trajects = list(trajects_db.values())
    stack = Stack(possible_trajects)

    for i in range(len(possible_trajects)):
        new_traject = stack.take()
        tempset = startset.copy()
        tempset[index]= new_traject
        new_K = K_calculator(tempset)
        if new_K > old_K:
            print(f"new_K: {new_K}")
            startset = tempset

    final_set = startset

    return(final_set)


trajects_db = traject_generator_new(critical_connections, 1000, 40)

startset = {}
for i in range(7):
    traject = list(trajects_db.values())[i]
    startset[i]= traject
print(f"len trajects db: {len(trajects_db)}")
print(f"startset{startset}")

K_set = {}
for k in range(20):
    new_set = hillclimber(startset, trajects_db, 0)
    print(f"new_set: {new_set}")
    K = K_calculator(new_set)
    K_set[K] = new_set




recursive_set = hillclimber(startset, trajects_db)















# with open('traject_db.csv', 'w') as f:
#     w = csv.DictWriter(f, fieldnames=trajects_db.keys())
#     w.writeheader()
#     w.writerow(trajects_db)



# plt.hist(K_distribution_newGreedy, bins='auto')
# plt.title("K spread - 500 iterations - 6 trajects, min 40 minutes new")
# plt.show()

# highest_k = max(K_distribution_newGreedy)
# print("BEST TRAJECT EVER")
# print(highest_k)
# print(all_trajects[highest_k])
