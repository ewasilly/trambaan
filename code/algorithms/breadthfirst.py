"""
This traject generator uses a breadth first approach to generate all possible trajects with the given connections.
"""

import helpers as h
from code.classes.traject import Traject
import copy

def traject_generator_BF(connections, max_minutes):

    # this will be the output dictionary
    trajects_db = {}
    # length of connections = the nr of connections
    len_all = len(connections)

    # build a stack to prevent to ensure use of all connections
    stack_all = h.Stack(connections)
    # this stack will be used for starting connections
    stack_start = h.Stack(connections)

    i = 0

    # start trajects from every possible connection
    while i < len_all:

        start_connection = stack_start.take()
        traject = Traject(start_connection)

        # add to trajects database with as unique key visited stations and time
        trajects_db[f"Traject{traject.visited_ids}-{traject.total_time}"]= traject

        i += 1

    # this loop will go on forever untill broken
    while True:
        temp_trajects_db = {}

        # for every traject in the database so far:
        for key, traject in trajects_db.items():

            j = 0

            while j < len_all:

                # copy the existing traject
                new_traject = copy.deepcopy(traject)
                # try to add every possible connection to this traject (one "breadth" iteration)
                new_traject.add_connection(connections[j])
                if new_traject.total_time > max_minutes:
                    j += 1
                else:
                    # add this new traject to the temporary traject database with its unique key
                    print(new_traject)
                    temp_trajects_db[f"Traject{new_traject.visited_ids}-{new_traject.total_time}"] = new_traject
                    j += 1


        if len(trajects_db) == len(temp_trajects_db):
            # if no new trajects were generated and added to the database:
            break

        # combine the old trajects database with the temporary database.
        trajects_db = {**trajects_db, **temp_trajects_db}


    return(trajects_db)
