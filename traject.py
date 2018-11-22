

class Traject():
    def __init__(self, startconnection):
        self.connections = [startconnection]
        # [(#,#), (#,#), etc]    LETOP: haakjes staan er niet echt, alleen voor leesbaarheid
        self.total_time = 0

    def add_connection(self, new_connection):
        # last connection in self.connections list:
        last_connection = self.connections[-1]

        # if new_connection follow the last_connection, add it.
        if new_connection.id_from == last_connection.id_to:
            self.connections.append(new_connection)
            self.total_time += new_connection.time
        else:
            pass

    def __repr__(self):
        return(f"{self.connections}")
