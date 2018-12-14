"""

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
from greedy import traject_generator_greedy
from hillclimber_basic import hillclimber
from hillclimber_SA import hillclimber_SA
from breadthfirst import traject_generator_BF
from helpers import Stack, K_calculator, get_trajects_from_csv, get_startset
from plot_stations import traj_plot


STATIONS_NH = 'data/StationsHolland.csv'
CONNECTIONS_NH = 'data/ConnectiesHolland.csv'

STATIONS_NL = 'data/StationsNationaal.csv'
CONNECTIONS_NL = 'data/ConnectiesNationaal.csv'


NH = Map(STATIONS_NH, CONNECTIONS_NH)
NH.load_stations()
NH.load_connections()

# NL = Map(STATIONS_NL, CONNECTIONS_NL)
# NL.load_stations()
# NL.load_connections()


trajects_db_NH = traject_generator_greedy(NH, 1000, 20)
# i = len(trajects_db_NL)//2
# tr = list(trajects_db_NL.values())[i]
# traj_plot(tr, NL, i)


for i in range(3):
    start_set = get_startset(5, 'random', trajects_db_NH)
    print(start_set)

    hillclimber(NH, start_set, trajects_db_NH, 1000, 7, 'plotON')

    hillclimber_SA(NH, start_set, trajects_db_NH, 7, 'plotON')


#
# traject_voor_jasper = list(trajects_db.values())[61]
# all_plot(traject_voor_jasper.connections)
#

# final = hillclimber(start_set, trajects_db, 7, 1000, critical_connections, all_connections)
#
# print(f"finalset = {final}")
# print(K_calculator(final, critical_connections, all_connections))
# print(f"start_set = {start_set}")
# print(K_calculator(start_set, critical_connections, all_connections))
#
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





# #  Create a trajects database for NL and save as csv
# with open('alltrajectsNH120.csv', 'w') as f:
#     w = csv.DictWriter(f, fieldnames=trajects_db.keys())
#     w.writeheader()
#     w.writerow(trajects_db)
#
# NHcsv = 'alltrajectsNH120.csv'
# NLcsv = 'alltrajectsNL180.csv'
#
# trajects_list_NL = get_trajects_from_csv(NLcsv)
# print(trajects_list_NL[58])
