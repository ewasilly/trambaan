"""
Main.py
>>> Moet alle Connections en Stations inladen
>>> Moet  stations_ids,  all_connections,  critical_connections  lists declaren
>>>>> Bevat het algoritme om trajecten mee op te bouwen. (depth-first?????)
        >>>> Dit moet in main omdat het al het bovenstaande nodig heeft.

Station.py
>>> bevat de class Station
Connection.py
>>> bevat de class Connection
Traject.py
>>> bevat de class traject
"""


#  ALGORITME APPEAAAR()!!!!


# vast
all_connections = []
critical_connections = []

# varierend per iteratie
next_possibilities = []

# uitbreidend per iteratie. maximaal totdat eindtijd bereikt is.
traject = []
traject_time = []
traject_time = traject_time.sum()





























# def give_id():
#     """
#     Parses a csv file and returns a dictionary in the format [stationname]:id, and a list with critical ids.
#     """
#     with open(STATIONS, 'r') as f:
#         reader = csv.reader(f)
#         stations_ids = {}
#         critical_ids = []
#         id = 0
#         for row in reader:
#             station_name = row[0]
#             id = id
#             stations_ids[station_name] = id
#             if row[3]:
#                 critical_ids.append(id)
#             id += 1
#
#         return(critical_ids)
#
#
#
# print(give_id())
