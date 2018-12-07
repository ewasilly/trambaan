# Rail NL
#### Description   
The Netherlands has many train stations, which are connected by railways.
Many people in the Netherlands make use of the rail network to travel through the country on a daily basis, it is important to set up a good railway network in order to connect all stations as efficiently as possible.

Our goal is to set up a combination of 7 trajectories at most. In the beginning, we will set trajectories through two provinces. After we have succeeded with that, we will proceed with the rest of Netherlands.

#### Definition trajectory
A trajectory is defined as a set of connections with a maximal total time of 120 minutes. All connections that include critical stations are considered critical and will yield extra points in our objective function.

#### How good is our solution?
The quality of our railway network can be calculated with the following objective function:

**K = p * 10000 - (T * 20 + Min/10)**

- K =  quality
- p =  fraction of critical connections used
- T =  amount of trajects (between 1 and 7)
- Min =  total minutes of the train system



We have determined the following statespace:
- Upper bound:
**u = (s * c_1 * (c_2)^a_m)^t**

    - u = upper bound
    - s = number of stations
    - c_1 = maximum number of connections
    - c_2 = maximum number of connections when travelling back is excluded
    - a_m = number of connections that fit into 120 minutes
    - t = number of maximal trajectoreies

- Louwer bound:
**l = c_crit**

    - l = lower bound
    - c_crit = number of critical connections


#### Prerequisites:
Our code has been written completely in Python 3.7

Please find all the necessary packages in order to run our code in **requirements.txt**.
These can be installed easily via the following pip command in your terminal:

**pip install -r requirements.txt**


#### Structure
All Python scripts are located in the folder **code**, as well as the script for assessment of the objective function.
The **data** folder contains information on all stations and connections
The folder **results** will contain all results generated by running the code.

#### Testing
Please use the following command to run the main code:
    python main_final.py


#### Authors
Ewa Sillem
Jasper Lankhorst
Louise Buijs


#### Acknowledgments
- StackOverflow
- W3 schools
- All the helpfull tutors en tech-assistants of the Minor Programmeren (University of Amsterdam)
