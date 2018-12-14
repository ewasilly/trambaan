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
from helpers import Stack, K_calculator, get_trajects_from_csv
from plot_stations import traj_plot


STATIONS_NH = 'data/StationsHolland.csv'
CONNECTIONS_NH = 'data/ConnectiesHolland.csv'

STATIONS_NL = 'data/StationsNationaal.csv'
CONNECTIONS_NL = 'data/ConnectiesNationaal.csv'


NH = Map(STATIONS_NH, CONNECTIONS_NH)
NH.load_stations()
NH.load_connections()

NL = Map(STATIONS_NL, CONNECTIONS_NL)
NL.load_stations()
NL.load_connections()





#  Create a trajects database and save as csv
trajects_db = traject_generator_BF(NL.all_connections, 180)
i = len(trajects_db)//2
tr = []
for j in range(20):
    traj = list(trajects_db.values())[i+30*j]
    tr.append(traj)
traj_plot(tr, NL, i)



#
# with open('alltrajectsNH120.csv', 'w') as f:
#     w = csv.DictWriter(f, fieldnames=trajects_db.keys())
#     w.writeheader()
#     w.writerow(trajects_db)
#
#
# #  Create a trajects database for NL and save as csv
# trajects_db_NL = traject_generator_BF(NL.all_connections, 180)
#
#
# with open('alltrajectsNL180.csv', 'w') as f:
#     w = csv.DictWriter(f, fieldnames=trajects_db_NL.keys())
#     w.writeheader()
#     w.writerow(trajects_db_NL)



# NH = 'alltrajectsNH120.csv'
# NL = 'alltrajectsNL180.csv'
# trajects_list_NH = get_trajects_from_csv(NH)
# print(trajects_list)
# print(len(trajects_list_NH))

# print("HERKENNNEEN")
# print(trajects_list_NH[0])
# print(trajects_list_NH[130])


# trajects_list_NL = get_trajects_from_csv(NL)
# print("NEDERLAND WHOEHOOO")
# print(trajects_list_NL[58])
# print(type(trajects_list_NL[500]))





#
# #  create a starting set of 15 trajects to use for the hillclimber
# start_set = {}
# for i in range(15):
#     traject = list(trajects_db.values())[random.randint(0, len(trajects_db))]
#     start_set[i] = traject
#
#
# hillclimber(start_set, 20, trajects_db, 100000, NL.critical_connections, NL.all_connections)




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
