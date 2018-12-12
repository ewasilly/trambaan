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
from map import Ruimte
sys.path.insert(1, 'code/algorithms/')
from greedy import traject_generator_Greedy_new
from hillclimber_basic import hillclimber
from hillclimber_SA import hillclimber_SA
from breadthfirst import traject_generator_BF
from helpers import *
from plot_stations import all_plot


STATIONS = 'data/StationsHolland.csv'
CONNECTIONS = 'data/ConnectiesHolland.csv'


nederland = ()

NH = Ruimte('data/StationsHolland.csv', 'data/ConnectiesHolland.csv')
NH.load_stations()
NH.load_connections()
print(NH.all_connections)



#
# #  Create a trajects database
# trajects_db = traject_generator_Greedy_new(all_connections, critical_connections, 1000, 7)
# # print(trajects_db)
# # print(len(trajects_db))
#
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




#
# with open('linevoering.csv', 'w') as f:
#     w = csv.DictWriter(f, fieldnames=final.keys())
#     w.writeheader()
#     w.writerow(final)
