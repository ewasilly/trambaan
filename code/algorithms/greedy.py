import helpers as h
import random
from code.classes.traject import Traject

def traject_generator_greedy(map, iterations, min_time, max_time):
    """
    This traject generator creates an arbitrary amount of trajects of a minimal time duration
    and returns a traject_database (dictionary).
    The key is a startconnection and total_time. This way, trajects that are identical will be overwritten
    resulting in no duplicates in the traject database.
    """
    connections = map.all_connections
    critical_connections = map.critical_connections

    # this will be the output dictionary
    trajects_db = {}
    # length of connections = the nr of connections
    len_all = len(connections)
    len_crit = len(critical_connections)

    # build a stack to prevent to ensure use of all connections
    stack_all = h.Stack(connections)
    stack_crit = h.Stack(critical_connections)

    def shuffle_stacks():
        random.shuffle(stack_all.array)
        random.shuffle(stack_crit.array)

    i = 0
    while i < iterations:
        shuffle_stacks()
        start_connection = stack_all.take()
        traject = Traject(start_connection)
        # dictionary for this startconnection
        tries = 0
        rounds = 0

        while tries < 1000:

            time_before = traject.total_time
            for j in range(len_crit):
                # try adding a critical connection first
                traject.add_connection(stack_crit.take())
                tries += 1
                traject.add_connection(stack_all.take())
                tries += 1
            time_after = traject.total_time
            rounds += 1
            shuffle_stacks()

            if time_after > max_time:
                break

            if time_after > min_time:
                print(traject)
                trajects_db[f"Traject{start_connection}-{traject.total_time}"]= traject
                i += 1

            # if connection is a dead end
            if time_before == time_after:
                break

    return(trajects_db)
