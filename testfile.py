
def traject_generator(connections, traject):
    """
    Neemt een Traject, zorgt ervoor dat dit gevuld wordt met een willekeurige
    route die niet twee keer over dezelfde connectie rijdt of 120+ min duurt.
    Neemt als argumenten de mogelijke connecties en het te vullen traject.
    """

    # Nieuwe lijst met connecties verkrijgen
    id_new_station = self.traject.connections[-1]
    for station in insert_stations_list:
        if self.station.id == id_new_station:
            # Moet in class station een lijst met de connecties daarvandaan hebben
            # Hiermee dit updaten
            connections =

    while self.traject.total_time < 120:
        if connections[0] in traject:
            random.shuffle(connections)
        else:
            traject.append(connections[0])
            time += self.numbers[0].time
            traject_generator()
    return traject




#  ALGORITME APPEAAAR()!!!!


# # vast
# all_connections = []
# critical_connections = []
#
# # varierend per iteratie
# next_possibilities = []
#
# # uitbreidend per iteratie. maximaal totdat eindtijd bereikt is.
# traject = []
# traject_time = []
# traject_time = traject_time.sum()
