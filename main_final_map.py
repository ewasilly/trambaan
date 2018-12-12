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
from map import Map
sys.path.insert(1, 'code/algorithms/')
from greedy import traject_generator_Greedy_new
from hillclimber_basic import hillclimber
from hillclimber_SA import hillclimber_SA
from breadthfirst import traject_generator_BF
from helpers import Stack, K_calculator
from plot_stations import all_plot


STATIONS_NH = 'data/StationsHolland.csv'
CONNECTIONS_NH = 'data/ConnectiesHolland.csv'

STATIONS_NL = 'data/StationsNationaal.csv'
CONNECTIONS_NL = 'data/ConnectiesNationaal.csv'


# NH = Map(STATIONS_NH, CONNECTIONS_NH)
# NH.load_stations()
# NH.load_connections()
# print(NH.all_connections)

NL = Map(STATIONS_NL, CONNECTIONS_NL)
NL.load_stations()
NL.load_connections()
print(NL.stations_dict)
print(NL.all_connections)


#  Create a trajects database
trajects_db = traject_generator_BF(NL.all_connections, 180)
print(trajects_db)
print(len(trajects_db))


#  create a starting set of 15 trajects to use for the hillclimber
start_set = {}
for i in range(15):
    traject = list(trajects_db.values())[-1 -i]
    start_set[i] = traject


hillclimber(start_set, 20, trajects_db, 1000, NL.critical_connections, NL.all_connections)




# traject_voor_jasper = list(trajects_db.values())[61]
# all_plot(traject_voor_jasper.connections)
#
# #  create a starting set of 3 trajects to use for the hillclimber
# start_set = {}
# for i in range(5):
#     traject = list(trajects_db.values())[i]
#     start_set[i] = traject
#
# final = hillclimber(start_set, trajects_db, 7, 1000, critical_connections, all_connections)
#
# print(f"finalset = {final}")
# print(K_calculator(final, critical_connections, all_connections))
# print(f"start_set = {start_set}")
# print(K_calculator(start_set, critical_connections, all_connections))

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
