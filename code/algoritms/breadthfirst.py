def traject_generator_BF(connections, critical_connections, min_time):

    # this will be the output dictionary
    trajects_db = {}
    # length of connections = the nr of connections
    len_all = len(connections)
    len_crit = len(critical_connections)

    # build a stack to prevent to ensure use of all connections
    stack_all = Stack(connections)
    stack_crit = Stack(critical_connections)

    stack_start = Stack(connections)

    i = 0
    while i < len_all:

        start_connection = stack_start.take()
        traject = Traject(start_connection)

        # add to trajects database with unique identifier
        trajects_db[f"Traject{traject.visited_ids}-{traject.total_time}"]= traject

        i += 1

    rounds = 0
    print(len(trajects_db))

    while True:
        temp_trajects_db = {}

        for key, traject in trajects_db.items():

            i = 0

            while i < len_all:
                new_traject = copy.deepcopy(traject)

                new_traject.add_connection(connections[i])
                temp_trajects_db[f"Traject{new_traject}-{new_traject.total_time}"] = new_traject

                i += 1

        if len(trajects_db) == len(temp_trajects_db):
            break

        trajects_db = {**trajects_db, **temp_trajects_db}

        print(len(trajects_db))


    return(trajects_db)
