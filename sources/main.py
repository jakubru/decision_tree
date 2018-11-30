from sources.create_dataset import create_dataset
from sources.create_tree import *
from sources.evaluate_tree import evaluate_tree
from sources.prune_tree import prune_tree
from sources.create_random_forest import create_random_forest
from sources.evaluate_random_forest import evaluate_random_forest


sets = create_dataset("winequality-white.csv",5,1,1)
forest = create_random_forest(20, sets[0])
print(evaluate_random_forest(sets[2], forest))