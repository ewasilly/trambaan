"""
Put in the stations and connections csv of choice (either Noordholland or Holland) and all data will be loaded in.
map = tuple(stations.csv, connections.csv)
"""
import csv
from station import Station
from connection import Connection

class Map():
    def __init__(self, csv_stations, csv_connections):
        # Dictionary {id: Stationobject}
        self.stations_dict = {}
        # Dictionary {name : id}
        self.name_id_dict = {}
        #  List with critical station ids
        self.critical_ids = []
        # Array with all connection objects
        self.all_connections = []
        # Subset of critical connection objects
        self.critical_connections = []
        self.csv_stations = csv_stations
        self.csv_connections = csv_connections




    def load_stations(self):
        """
        Loads stations from the stations csv into dictionary {id: stationobject}
        Also adds every critical id to the critical_ids list.
        """
        with open(self.csv_stations, 'r') as f:
            reader = csv.reader(f)
            id = 0
            for row in reader:
                name = row[0]
                # check whether station is critical
                if len(row) > 3:
                    if row[3]:
                        critical = True
                        self.critical_ids.append(id)
                else:
                    critical = False
                # create station with all attributes
                station = Station(name, id, critical)
                # add station to dictionary
                self.stations_dict[id] = station
                self.name_id_dict[name] = id
                id += 1


    def load_connections(self):
        """
        Loads all connections in connectiesHolland.csv as objects into a list.
        """
        with open(self.csv_connections, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                # Alkmaar
                name_from = row[0]
                # Hoorn
                name_to = row[1]
                # 24
                time = int(float(row[2]))
                # Find the id of these stations:
                id_from = self.name_id_dict[name_from]
                id_to = self.name_id_dict[name_to]
                # make the connection object and add to all_connections
                connection = Connection(id_from, id_to, time)
                self.all_connections.append(connection)

                # add to critical_connections if either of two ids is critical
                if id_from in self.critical_ids or id_to in self.critical_ids:
                    self.critical_connections.append(connection)

    def __repr__(self):
        return(f"self")
