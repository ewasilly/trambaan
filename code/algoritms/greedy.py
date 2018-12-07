
'''
This traject generator creates an arbitrary amount of trajects and returns a traject_database (dictionary)
The key is contains startconnection and total_time. This way, trajects that are identical will be overwritten
resulting in no duplicates in the traject database.
'''

def traject_generator_Greedy_new(connections, critical_connections, nr_of_trajects, min_time):

    # this will be the output dictionary
    trajects_db = {}
    # length of connections = the nr of connections
    len_all = len(connections)
    len_crit = len(critical_connections)

    # build a stack to prevent to ensure use of all connections
    stack_all = Stack(connections)
    stack_crit = Stack(critical_connections)

    def shuffle_stacks():
        random.shuffle(stack_all.array)
        random.shuffle(stack_crit.array)

    i = 0
    while i < nr_of_trajects:
        shuffle_stacks()
        start_connection = stack_all.take()
        traject = Traject(start_connection)
        # dictionary for this startconnection
        tries = 0
        rounds = 0

        while tries < 1000:

            time_before = traject.total_time
            for j in range(len_crit):
                traject.add_connection(stack_crit.take())
                tries += 1
                traject.add_connection(stack_all.take())
                tries += 1
            time_after = traject.total_time
            rounds += 1
            shuffle_stacks()

            if time_after > min_time:
                trajects_db[f"Traject{start_connection}-{traject.total_time}"]= traject
                i += 1

            # if connection is a dead end
            if time_before == time_after:
                break

    return(trajects_db)



"""""
If it is intended to save the traject_db, execute the following code
"""""

# with open('traject_db.csv', 'w') as f:
#     w = csv.DictWriter(f, fieldnames=trajects_db.keys())
#     w.writeheader()
#     w.writerow(trajects_db)
