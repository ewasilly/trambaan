"""
backup voor als we dit kwijtraken. WEeet nog niet echt waar het moet.
"""
import collections
import csv

class Stack():
    def __init__(self, array):
        self.array = array

    #  takes first item and puts it back at the end of the array
    def take(self):
        taken = self.array[0]
        self.array.pop(0)
        self.array.append(taken)
        return(taken)

    def __repr__(self):
        return(f"{self.array}")




def K_calculator(trajects, critical_connections, all_connections):

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

    print(f"F: {f}")
    print(f"P: {p}")
    print(f"K: {K}\n")

    return(K)



def get_trajects_from_csv(trajects_db_csv):
    """
    This function reads a csv file containing all possible trajects and returns all trajects as a list without keys.
    This is way we can get quicker access to the trajects database than by creating the trajects_db everytime with
    the breadthfirst traject_generator algorithm.
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
