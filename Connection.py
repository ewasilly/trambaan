# Louise
# Heuristieken / RailNL

"""
In this script the Class Connection will be defined.  Also all connections will be loaded from CSV file.
"""

import csv


CONNECTIONS= 'ConnectiesHolland.csv'
STATIONS= "StationsHolland.csv"

class Connection():
    def __init__(self, station_1, station_2, duration):
        # self.id kan weggelaten worden als we voor id als dictionary keys kiezen
        self.id_from = id_from
        self.id_to= id_to
        self.duration = duration

    def is_critical = critical

    def __repr__(self):
        return(f"{self.id_from} - {self.id_to}, duration:{duration} min")



def give_id():
    """
    Parses a csv file and returns a dictionary in the format [stationname]:id, and a list with critical ids.
    """
    with open(STATIONS, 'r') as f:
        reader = csv.reader(f)
        stations_ids = {}
        critical_ids = []
        id = 0
        for row in reader:
            station_name = row[0]
            id = id
            stations_ids[station_name] = id
            if row[3]:
                critical_ids.append(id)
            id += 1

        return(critical_ids)


print(give_id())


def load_connections():









def load_connections():
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
