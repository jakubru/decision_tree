from sources.create_dataset import create_dataset
from sources.create_tree import *
from sources.evaluate_tree import evaluate_tree
from sources.prune_tree import prune_tree


sets = create_dataset("winequality-white.csv")
(tree,prob_Y) = create_tree(sets[0], 4,10)
print(tree_len(tree))
print(evaluate_tree(tree, sets[0], False))
prune_tree(tree,tree,prob_Y,sets[1])
print(tree_len(tree))
print(evaluate_tree(tree, sets[0], False))
