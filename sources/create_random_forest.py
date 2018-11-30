from sources.create_tree import *


def create_random_forest(amount_of_trees, training_set):
    forest = list()
    for i in range(0, amount_of_trees):
        forest.insert(0,create_tree(training_set,5, len(training_set))[0])
    print('skonczono')
    return forest