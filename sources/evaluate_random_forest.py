
from statistics import mode

def evaluate_random_forest(test_set, forest):
    hits = 0
    for element in test_set:
        results = list()
        for tree in forest:
            node = tree
            while (node.left and node.right):
                if (element[node.label] <= node.position):
                    node = node.left
                else:
                    node = node.right
            results.insert(0, node.position)
        result = mode(results)
        if(result == element[len(element)-1]):
            hits += 1
    return hits/len(test_set)
