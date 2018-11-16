# Louise
# Heuristieken / RailNL

"""
In this script the Class Station will be defined.
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





"""
Stations laden moet uiteindelijk in de main file denk ik. Maar het belang van deze class is voor nu een beetje onduidelijk
Ook wat er in moet is nog onduidelijk.
"""

def load_stations(infile):
    """
    Loads stations from CSV file. Returns list containing station objects
    """
    stations = []
    # stations = [] kan ook weg als we voor dictionary kiezen
    stations_dict = {}
    with open(infile, 'r') as f:
        reader = csv.reader(f)
        id = 0
        for row in reader
            name = row[0]
            id = id
            if row[3]:
                critical = True
            else:
                critical = False
            station = Station(name, id, critical)
            stations.append(station)
            stations_dict[id] = station
            id += 1
    return(stations_dict)


print(load_stations(STATIONS))
