# Louise
# Heuristieken / RailNL

"""
In this script the Class Station will be defined.
"""

import csv


STATIONS = 'StationsHolland.csv'

class Station():
    def __init__(self, name, id, critical):
        # self.id kan weggelaten worden als we voor id als dictionary keys kiezen
        self.id = id
        self.name = name
        self.critical = critical
    def __repr__(self):
        return(f"{self.name}, {self.critical}")


"""
Stations laden moet uiteindelijk in de main file denk ik. Maar het belang van deze class is voor nu een beetje onduidelijk
Ook wat er in moet is nog onduidelijk.
"""
