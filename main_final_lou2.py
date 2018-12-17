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
from hillclimber_SA2 import hillclimber_SA2
from breadthfirst import traject_generator_BF
from helpers import Stack, K_calculator, get_trajects_from_csv, get_startset
from plot_stations import traj_plot


STATIONS_NH = 'data/StationsHolland.csv'
CONNECTIONS_NH = 'data/ConnectiesHolland.csv'

STATIONS_NL = 'data/StationsNationaal.csv'
CONNECTIONS_NL = 'data/ConnectiesNationaal.csv'


# NH = Map(STATIONS_NH, CONNECTIONS_NH)
# NH.load_stations()
# NH.load_connections()

NL = Map(STATIONS_NL, CONNECTIONS_NL)
NL.load_stations()
NL.load_connections()
print(NL.all_connections)

# # trajects_db_NL = traject_generator_greedy(NL, 100000, 1, 180)
# trajects_db_NL = traject_generator_BF(NL, 180)
# db_size =len(trajects_db_NL)
# print(db_size)

tr_db = []
for conn in NL.all_connections:
    tr = Traject(conn)
    tr_db.append(tr)

traj_plot(tr_db, NL, 'Nederland')




# K_dist = []
# for i in range(10):
#     start_set = get_startset(1, 'random', trajects_db_NL)
#     final = hillclimber_SA2(NL, start_set, trajects_db_NL, 20, 'plotON')
#     K = K_calculator(final, NL.critical_connections, NL.all_connections)
#     K_dist.append(K)
#
#
# plt.hist(K_dist, bins=10)
# plt.ylabel(f"K spread finalset by SA hillclimber - BFsetsize: {db_size}")
# plt.show()
#
#
#




#
# NHcsv = 'alltrajectsNH120.csv'
# NLcsv = 'alltrajectsNL180.csv'
#
# trajects_list_NL = get_trajects_from_csv(NLcsv)
# print(trajects_list_NL[58])
