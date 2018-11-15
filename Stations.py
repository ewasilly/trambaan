# Louise
# Heuristieken / RailNL

"""
In this script the Class Station will be defined.  Also all stations will be loaded.
"""

import csv


STATIONS = 'StationsHolland.csv'

class Station():
    def __init__(self, name, id, critical):
        # self.id kan weggelaten worden als we voor id als dictionary keys kiezen
        self.id = id
        self.name = name
        self.critical = critical
    def __repr__(self):
        return(f"{self.id}, {self.name}, {self.critical}")

def load_stations():
    """
    Loads stations from CSV file. Returns list containing station objects
    """
    stations = []
    # stations = [] kan ook weg als we voor dictionary kiezen
    stations_dict = {}
    with open(STATIONS, 'r') as f:
        reader = csv.reader(f)
        numbers = list(range(len(STATIONS)))
        for row, number in zip(reader, numbers):
            name = row[0]
            id = number
            if row[3]:
                critical = True
            else:
                critical = False
            station = Station(name, id, critical)
            stations.append(station)
            stations_dict[id] = station
    return(stations_dict)


print(load_stations())
