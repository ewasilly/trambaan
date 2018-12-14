import helpers as h
import random
import copy
import matplotlib.pyplot as plt


def hillclimber_SA(map, startset, trajects_database, max_nr_of_trajects, plot):
    """
    This steepest ascent hillclimber takes as arguements a startset with an
    arbitrary amount of trajects, as well as the trajects database. Systematically each traject
    from the database will be added in the startset and the effect on K-value will be evaluated.
    The max_nr_of_trajects parameter specifies how much trajects you maximally want in the final set.
    The plot parameter must be 'plotON' or 'plotOFF' depending on whether or not a plot should be generated.
    """

    critical_connections = map.critical_connections
    connections = map.all_connections

    # create a stack of the trajects database
    possible_trajects = list(trajects_database.values())
    stack = h.Stack(possible_trajects)

    # index for which traject in the set will be changed
    change_index = 0

    # keep track of K-values for plots
    K_distribution = {}
    iterations = 0

    while change_index < max_nr_of_trajects:

        random.shuffle(stack.array)

        # As all trajects will be tried as a change --> steepest ascent
        for i in range(len(possible_trajects)):

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
                K_distribution[iterations] = new_K

            # after all trajects where tried as a change, go try changing the next index
            change_index += 1
            iterations += 1

    if plot == 'plotON':
        # plot linechart of K values
        plt.plot(K_distribution.keys(), K_distribution.values())
        plt.xlabel('iterations')
        plt.ylabel('K_value')
        plt.title(f"K spread Steepest Ascent hillclimber - iterations {iterations}")
        plt.show()

    final_set = startset

    return(final_set)
