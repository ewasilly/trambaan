import helpers as h
import random
import copy
import matplotlib.pyplot as plt


def hillclimber(map, startset, trajects_database, iterations, max_nr_of_trajects, plot):

    """""
    This stochastic hillclimber takes as arguments a startset with an arbitrary amount of
    trajects, and a trajects database. It takes a traject from the database and evaluates the effect
    of adding it into a temporary copy of the startset.
    You can specify how much trajects you maximally want in the final set by max_nr_of_trajects.
    The plot parameter must be 'plotON' or 'plotOFF' depending on whether or not a plot should be generated.

    """""
    critical_connections = map.critical_connections
    connections = map.all_connections

    # create a stack of the trajects database
    possible_trajects = list(trajects_database.values())
    stack = h.Stack(possible_trajects)
    random.shuffle(stack.array)

    # keep track of K-values for plots
    K_distribution = {}

    i = 0

    while i < iterations:

        # index for which traject in the set will be changed
        change_index = iterations%max_nr_of_trajects

        # calculate the old K
        old_K = h.K_calculator(startset, critical_connections, connections)

        # take a traject from the stack
        new_traject = stack.take()
        # create a copy of the startset where in the new_traject will be added.
        tempset = copy.copy(startset)
        # change traject at change_index, or add traject to startset if change_index not yet in startset.
        tempset[change_index] = new_traject
        # calculate new K
        new_K = h.K_calculator(tempset, critical_connections, connections)

        # if the change results in higher K update startset
        if new_K > old_K:
            startset = tempset
            K_distribution[i] = new_K
        i += 1


    if plot == 'plotON':
        # plot linechart of K values
        plt.plot(K_distribution.keys(), K_distribution.values())
        plt.xlabel('iterations')
        plt.ylabel('K_value')
        plt.title(f"K spread Stochastic hillclimber - {iterations} iterations - {map}")
        plt.show()


    final_set = startset

    return(final_set)
