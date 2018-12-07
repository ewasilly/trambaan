# Trambaan
# Class Traject
# Heuristieken 2018 UvA

class Traject():
    def __init__(self, startconnection):
        self.connections = [startconnection]
        # [(#,#), (#,#), etc]    LETOP: haakjes staan er niet echt, alleen voor leesbaarheid
        self.total_time = startconnection.time
        self.visited_ids = [startconnection.id_from, startconnection.id_to]


    def add_connection(self, new_connection):
        # last connection in self.connections list:
        last_connection = self.connections[-1]

        # if new_connection follows the last_connection, add it.
        if new_connection.id_from == last_connection.id_to and new_connection.id_to not in self.visited_ids:
            self.visited_ids.append(new_connection.id_to)
            self.connections.append(new_connection)
            self.total_time += new_connection.time
        else:
            pass

    def __repr__(self):
        return(f"{self.connections}")
