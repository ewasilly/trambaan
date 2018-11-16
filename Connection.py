# Louise
# Heuristieken / RailNL

"""
In this script the Class Connection will be defined.
"""


import csv


CONNECTIONS= 'ConnectiesHolland.csv'
STATIONS= "StationsHolland.csv"

class Connection():
    def __init__(self, id_from, id_to, time):
        # self.id kan weggelaten worden als we voor id als dictionary keys kiezen
        self.id_from = id_from
        self.id_to= id_to
        self.time = time


    def __repr__(self):
        return(f"{self.id_from}-{self.id_to}")



def give_id(infile):
    """
    Parses a csv file and returns a dictionary in the format [stationname]:id, and a list with critical ids.
    """
    with open(infile, 'r') as f:
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

        return(stations_ids)

# dictionary with [stationname]:id
stations_ids = give_id(STATIONS)



def load_connections(infile):
    """
    Loads all connections in connectiesHolland.csv as objects into a list
    """
    all_connections = []
    with open(infile, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            station_from = row[0]
            station_to = row[1]
            id_from = stations_ids[station_from]
            id_to = stations_ids[station_to]
            time = int(row[2])
            connection = Connection(id_from, id_to, time)
            all_connections.append(connection)

    return(all_connections)

all_connections = load_connections(CONNECTIONS)



# print(stations_ids)
print(all_connections)


for cn in all_connections:
    print(cn.id_from)
    print(cn.id_to)
    print(cn.time)
