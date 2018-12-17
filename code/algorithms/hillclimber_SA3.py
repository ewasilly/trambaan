import helpers as h
import random
import copy
import matplotlib.pyplot as plt


def hillclimber_SA3(map, strtset, trajects_database, max_nr_of_trajects, rounds, plot):
    """
    This steepest ascent hillclimber takes as arguments a startset of trajects,
    as well as the trajects database.
    Systematically each traject from the database will be added in the startset and the effect on K-value will be evaluated.
    The max_nr_of_trajects parameter specifies how much trajects you maximally want in the final set.
    The plot parameter must be 'plotON' depending on whether or not a plot should be generated.
    This hillclimber
    Round must be preferably in the range of 100-1000
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
    startset = strtset

    print(f"startset: {startset}")

    while change_index < rounds:

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
            tempset[change_index%max_nr_of_trajects] = new_traject
            # calculate new K
            new_K = h.K_calculator(tempset, critical_connections, connections)

            # if the change results in higher K update startset
            if new_K > old_K:
                startset = tempset
                stack.remove(new_traject)
                # make sure that the traject will not be used in the set twice
                K_distribution[iterations] = new_K


            iterations += 1
        # after all trajects where tried as a change, go try changing the next index
        change_index += 1

        if change_index%50 == 0:
            remove_index = change_index%max_nr_of_trajects
            try:
                startset.pop(remove_index)
            except:
                pass



    if plot == 'plotON':
        # plot linechart of K values
        plt.plot(K_distribution.keys(), K_distribution.values())
        plt.xlabel('iterations')
        plt.ylabel('K_value')
        plt.title(f"K spread Steepest Ascent hillclimber - iterations {iterations}")
        plt.show()

    final_set = startset
    print(f"finalset : {final_set}")


    return(final_set)
