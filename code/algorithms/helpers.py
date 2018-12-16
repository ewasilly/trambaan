"""
All helping functions
"""

import collections
import csv
import random

class Stack():
    """
    Repositions the first item of the array to the end of the array.
    """

    def __init__(self, array):
        self.array = array

    def take(self):
        taken = self.array[0]
        self.array.pop(0)
        self.array.append(taken)
        return(taken)

    def remove(self, element):
        self.array.remove(element)

    def __repr__(self):
        return(f"{self.array}")




def K_calculator(trajects, critical_connections, all_connections):
    """
    Calculates the K-value of a given set of trajectories
    """

    used_conns = []
    used_crit = []
    total_minutes = []
    for key in trajects.keys():
        traject = trajects[key]
        total_minutes.append(traject.total_time)
        for conn in traject.connections:
            used_conns.append(conn)
            if conn in critical_connections:
                used_crit.append(conn)

    # fraction of used connections
    f= len(collections.Counter(used_conns))/len(all_connections)

    p = len(collections.Counter(used_crit))/ len(critical_connections)
    t = len(trajects.keys())
    total_minutes = sum(total_minutes)
    K = p*10000 - (t*20 + (total_minutes/10))
    #
    # print(f"F: {f}")
    # print(f"P: {p}")
    # print(f"K: {K}\n")

    return(K)



def get_startset(n, mode, trajects_db):
    """
    Creates a starting set of n trajects to use for e.g. a hillclimber. Mode should be 'random', 'last' or 'first'.
    and applies to which trajects from the traject database will be used.
    """
    start_set = {}
    trajects_db = list(trajects_db.values())
    ln = len(trajects_db)

    if mode == 'first':
        for i in range(n):
            traject = trajects_db[i]
            start_set[i] = traject

    elif mode == 'random':

        for i in range(n):
            j = random.randint(0,ln)
            traject = trajects_db[j]
            start_set[i] = traject

    elif mode == 'last':
        for i in range(n):
            traject = trajects_db[-1-i]
            start_set[i] = traject

    return(start_set)



def get_trajects_from_csv(trajects_db_csv):
    """
    Reads a csv file containing all possible trajects and returns all trajects as a list without keys.
    This is way we can get quicker access to the trajects database,
    and it is no longer necessary to recreate the database.
    Unfortunately it is useless as it only returns strings.
    """
    csv_output = []
    with open(trajects_db_csv, newline='') as c:
        reader = csv.reader(c)
        for row in reader:
            traject = row
            csv_output.append(traject)

    # keys = csv_output[0]
    trajects_list = csv_output[1]

    return(trajects_list)
