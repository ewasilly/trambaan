import csv
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# with open("ConnectiesHolland.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#
# stationsnamen = []
# x = []
# y = []
#
# with open("ConnectiesHolland.csv") as g:
#     reader = csv.reader(g)
#     for row in reader:
#         stationsnamen.append(row[0])
#         x.append(row[1])
#         y.append(row[2])
#
#
#
# for connection in connections:
#     id_from = connection.id_from
#     id_to = connection.id_to
#     plt.plot()


# myplot = plt.plot(x, y)
# plt.show()

stations_frame = pd.read_csv("StationsHolland.csv", header=None)
# print(stations_frame)

stations_punten = np.linspace(0.0, (2 * np.pi), 22)

for i in stations_punten:
    plt.plot(np.cos(i), np.sin(i), 'ro')
plt.plot([np.cos(stations_punten[1]), np.sin(stations_punten[1])], [np.cos(stations_punten[6]), np.sin(stations_punten[6])])
# plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.show()
