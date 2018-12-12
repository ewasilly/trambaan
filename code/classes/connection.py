# Louise
# Heuristieken / RailNL

# In this script the Class Connection will be defined.

class Connection():
    """
    Is the connection between two stations.
    id_from and id_to are station ids
    time is the time it takes between the two stations
    """
    def __init__(self, id_from, id_to, time):
        # self.id kan weggelaten worden als we voor id als dictionary keys kiezen
        self.id_from = id_from
        self.id_to= id_to
        self.time = time
        self.tuple = (id_from, id_to)


    def __repr__(self):
        # let op dit is dus geen tuple, het print alleen in de layout zo
        # return(f"({self.id_from},{self.id_to})")
        return(f"{self.tuple}")
