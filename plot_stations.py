import csv
import numpy as np
import math
import matplotlib.pyplot as plt

# with open("ConnectiesHolland.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

stationsnamen = []
x = []
y = []

with open("ConnectiesHolland.csv") as g:
    reader = csv.reader(g)
    for row in reader:
        stationsnamen.append(row[0])
        x.append(row[1])
        y.append(row[2])

myplot = plt.plot(x, y)
# for i, station in enumerate(stationsnamen):
#     i.annotate(station, (x[i], y[i]))
plt.show()
