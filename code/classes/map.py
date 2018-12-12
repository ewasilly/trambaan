Map(stations_csv, connections_csv, )
"""
Put in the stations and connections csv of choice (either Noordholland or Holland) and all data will be loaded in.
map = tuple(stations.csv, connections.csv)
"""



class Map():
    def __init__(self, csv_files):
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


    def load_stations(csv_files[0]):
        """
        Loads stations from the stations csv into dictionary {id: stationobject}
        Also adds every critical id to the critical_ids list.
        """
        with open(infile, 'r') as f:
            reader = csv.reader(f)
            id = 0
            for row in reader:
                name = row[0]
                # check whether station is critical
                if row[3]:
                    critical = True
                    critical_ids.append(id)
                else:
                    critical = False
                # create station with all attributes
                station = Station(name, id, critical)
                # add station to dictionary
                stations_dict[id] = station
                name_id_dict[name] = id
                id += 1


    def load_connections(csv_files[1]):
        """
        Loads all connections in connectiesHolland.csv as objects into a list.
        """
        with open(infile, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                # Alkmaar
                name_from = row[0]
                # Hoorn
                name_to = row[1]
                # 24
                time = int(row[2])
                # Find the id of these stations:
                id_from = name_id_dict[name_from]
                id_to = name_id_dict[name_to]
                # make the connection object and add to all_connections
                connection = Connection(id_from, id_to, time)
                all_connections.append(connection)

                # add to critical_connections if either of two ids is critical
                if id_from in critical_ids or id_to in critical_ids:
                    critical_connections.append(connection)

    def __repr__(self):
        return(f"self")
