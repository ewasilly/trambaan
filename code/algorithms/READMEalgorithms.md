# Algorithms
### Description   
In this folder some all used algorithms can be found.
We will now give some extra information on how all of these were generated and why.


### Trajectgenerator_greedy
Traject generator greedy creates a database of trajects in the most simple way. It takes a startconnection
and tries to add the first connection on the stack of all connections. If it fits, the traject will incorporate the connection.
If it doesnt fit, the algorithm tries adding the next connection on the stack. The traject is added to the database if it is not longer than maximal time and not shorter than minimal time. Later weve added the use of two subsequent stacks. One containing only critical connections, and the other stack containing all_connections(so this stack contains the critical ones aswell). This way we double the chances of incorporating a critical connection.


### Traject_genarator_BF
The breadthfirst algorithm emerged out of the greedy generator. In this algorithm a startstack is used to generate a 'one connection length' traject for every connection in the map. Than systematically all of these start trajects will be elongated with another stack. Every step inbetween will be saved in a temporary copy of the startdatabase. After all starttrajects were tried to be elongated with all possible connections, the temporary database will be merged with the startdatabase and this process is repeated untill the whole tree has been built.


### Hillclimber SA
The Steepest ascent hillclimber was actually built before the stochastic hillclimber. The main difference with the stochastic one is that instead of changing a traject in the set for a randomly chosen traject from the traject database, the steepest ascent tries changing it for all trajects in the trajects database, untill it finds one that is better.


### Hillclimber
The stochastic hillclimber.
