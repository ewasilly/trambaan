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

#
# trajects_db_NH = traject_generator_greedy(NH, 10000, 1)




trajects_db = traject_generator_BF(NH, 120)
i = len(trajects_db)//2
tr = []
for j in range(7):
    traj = list(trajects_db.values())[i+20]
    tr.append(traj)
traj_plot(tr, NH, i)
