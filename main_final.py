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

#
# NH = Map(STATIONS_NH, CONNECTIONS_NH)
# NH.load_stations()
# NH.load_connections()

NL = Map(STATIONS_NL, CONNECTIONS_NL)
NL.load_stations()
NL.load_connections()


trajects_db_NL = traject_generator_BF(NL, 180)
# i = len(trajects_db_NL)//2
# tr = list(trajects_db_NL.values())[i]
# traj_plot(tr, NL, i)


for i in range(5):
    start_set = get_startset(3, 'first', trajects_db_NL)
    print(start_set)

    hillclimber(NL, start_set, trajects_db_NL, 10000, 20, 'plotON')

print(start_set)
hillclimber_SA(NL, start_set, trajects_db_NL, 20, 'plotON')

print("RANDOM")

for i in range(5):
    start_set = get_startset(2, 'random', trajects_db_NL)
    print(start_set)

    hillclimber(NL, start_set, trajects_db_NL, 10000, 20, 'plotON')

print(start_set)
hillclimber_SA(NL, start_set, trajects_db_NL, 20, 'plotON')







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
