# Jasper Lankhorst
# Heuristieken / RailNL

"""
In this script I do some calculations with the ConnectiesHolland file.
"""

import csv
import numpy as np
from requests import get

CONNECTIONS = 'ConnectiesHolland.csv'

def average_minutes():
    """
    Calculates the average amount of minutes for a connection.
    """
    minutes_list = []
    with open(CONNECTIONS, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            minutes_list.append(int(row[2]))
    return np.mean(minutes_list)

if __name__ == "__main__":
    print(f"The average amount of minutes of a connection is {average_minutes()}")
