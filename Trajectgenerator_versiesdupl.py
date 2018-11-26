


"""
Versie 1: Hierin is eigenlijk het probleem dat de trajecten steeds veel te kort worden.
"""
for i in range(7):
    # generate a random number to use as starting connection in Traject
    start = np.random.randint(low=1, high=len)
    print(f"startconnectie is: {all_connections[start]}")
    traject = Traject(all_connections[start])
    # Prevent going back and forth by keeping track of used connections
    used = []
    length_used = 0
    while traject.total_time <= 90:
        # modulo is used to prevent "index out of range list" error.
        j = random.choice(numbers)
        index = j % len
        # using the Traject method add_connection, to add the
        # connection at [j] in all_connections
        if all_connections[index] not in used:
            traject.add_connection(all_connections[index])
            used.append(all_connections[index])
            length_used += 1
        if length_used == len or traject.total_time >= 110:
            print(traject)
            trajects[f"Traject{i+1}."] = (traject, traject.total_time)
            break
print(f"De opgestelde trajecten zijn: {trajects}")



"""
Versie 2: Hierin kun je een minimale lengte voor een traject instellen. Als je 50 min doet lukt het prima,
bij 80 min rekent hij al langer omdat de incidentie van een random opgesteld traject dat zo lang duurt klein is.

Heuristieken nog toepassen:
kritieke verbindingen mogen dubbel gebruikt worden,
niet kriteike niet.
"""

i = 1
# arbitrary :
min_time = 70
while i < 7:
    # generate a random number to use as starting connection in Traject
    start = np.random.randint(low=1, high=len)
    print(f"startconnectie is: {all_connections[start]}")
    traject = Traject(all_connections[start])
    # Prevent going back and forth by keeping track of used connections
    used = []
    length_used = 0
    while traject.total_time <= 120:
        # modulo is used to prevent "index out of range list" error.
        j = random.choice(numbers)
        index = j % len
        # using the Traject method add_connection, to add the connection at [j] in all_connections
        if all_connections[index] not in used:
            traject.add_connection(all_connections[index])
            used.append(all_connections[index])
            length_used += 1
        # if every option of all_connections has been tried:
        if length_used == len:
            # if the total time of the current traject overceeds min_time use this traject.
            if traject.total_time >= min_time:
                print(traject)
                trajects[f"Traject{i}."] = (traject, traject.total_time)
                i += 1
                break
            # if the traject is too short, start over.
            else:
                print("OVERNIEUW")
                break

print(f"De opgestelde trajecten zijn: {trajects}")


"""
versie 3 incl objective function variables
"""
# create random array of numbers to use as indices in all_connections
numbers = np.arange(10000)
trajects = {}

# OPTION: choose between critical or all connections
connections = all_connections
print(connections)
print(connections[4])

# count the use of connections during all 7 trajects
used_all = []
# keep track of total time, will be used in objective function
total_minutes = []
# keep track of used critical connections
used_critical = []

# the length of all_connections can be used with modulo. More info later.
length = len(connections)

i = 1
# arbitrary :
min_time = 50
while i < 7:
    # generate a random number to use as starting connection in Traject
    start = random.choice(range(length))
    traject = Traject(connections[start])
    # # Prevent going back and forth by keeping track of used connections
    # used = []
    tried = 1
    while traject.total_time <= 120:
        # modulo is used to prevent "index out of range list" error.
        j = random.choice(numbers)
        index = j % length
        # using the Traject method add_connection, to add the connection at [j] in all_connections
        if connections[index] not in traject.connections:
            traject.add_connection(connections[index])
            tried += 1
        # if every connection has been tried:
        if tried == length:
            # if the total time of the current traject overceeds min_time use this traject.
            if traject.total_time >= min_time:
                trajects[f"Traject{i}."] = traject
                total_minutes.append(traject.total_time)
                i += 1
                # add connections in this traject to used_all, eventually the use through all 7 trajects will be counted
                for conn in traject.connections:
                    used_all.append(conn)
                    if conn in critical_connections:
                        used_critical.append(conn)
                break
            # if the traject is too short, start over.
            else:
                break
