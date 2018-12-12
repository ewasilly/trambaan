
"""""
Steepest ascent!

This hillclimber takes a startset with an arbitrary amount of trajects, aswell as a trajects database.
It takes a traject from the database and evaluates the effect of adding it into a temporary copy of the startset.
You can specify how much trajects you maximally want in the final set.
If adding an extra traject to your startset results in a higher K value. This change will be accepted aswell.

"""""
import helpers as h
import random
import copy


def hillclimber(startset, max_nr_of_trajects, trajects_database, iterations, critical_connections, connections):

    # create a stack of the trajects database
    possible_trajects = list(trajects_database.values())
    stack = h.Stack(possible_trajects)
    random.shuffle(stack.array)

    i = 0

    while i < iterations:

        random.shuffle(indices)
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

        i += 1

    final_set = startset

    return(final_set)




"""""
Vanaf hier moet het naar main om te runnen
"""""
# #  Create a trajects database
# trajects_db = traject_generator_Greedy_new(all_connections, 100, 60)
# # print(trajects_db)
#
# #  create a starting set of 3 trajects to use for the hillclimber
# start_set = {}
# for i in range(3):
#     traject = list(trajects_db.values())[i]
#     start_set[i] = traject
#
#
#
# final = hillclimber(start_set, trajects_db, 7, 1000)
#
# print(f"finalset = {final}")
# print(K_calculator(final))
# print(f"start_set = {start_set}")
# print(K_calculator(start_set))
