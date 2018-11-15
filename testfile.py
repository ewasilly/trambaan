import csv



STATIONS = "StationsHolland.csv"




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
