from sources import evaluate_tree
from sources.create_tree import tree_len

def prune(root,node, prob_Y, validation_dataset, acc1, epsilon):
    if(node.left.isLeaf and node.right.isLeaf):
        nodeLeft = node.left
        nodeRight = node.right
        nodeLabel = node.label
        nodePosition = node.position
        pos1 = node.left.position
        pos2 = node.right.position
        val1 = 0
        val2 = 0
        for element in prob_Y:
            if(element[0] == pos1):
                val1 = element[1]
            if(element[0] == pos2):
                val2 = element[1]
        if(val1 > val2):
            node.position = pos1
            node.label = val1
        else:
            node.position = pos2
            node.label = val2
        node.left = None
        node.right = None
        node.isLeaf = True
        acc2 = evaluate_tree.evaluate_tree(root, validation_dataset)
        if acc2 >= acc1 - epsilon:
            return True
        else:
            node.left = nodeLeft
            node.right = nodeRight
            node.position = nodePosition
            node.label = nodeLabel
            node.isLeaf = False
            return False
    else:
        return False


def prune_tree_internal(root,tree, prob_Y, validation_dataset, acc1, epsilon):
    pruned1 = False
    pruned2 = False
    if(not tree.left.isLeaf):
        pruned1 = prune_tree_internal(root,tree.left, prob_Y, validation_dataset,acc1, epsilon)
    if(not tree.right.isLeaf):
        pruned2 = prune_tree_internal(root,tree.right, prob_Y, validation_dataset,acc1, epsilon)
    return pruned1 or pruned2 or prune(root,tree, prob_Y, validation_dataset,acc1, epsilon)


def prune_tree(root,tree, prob_Y, validation_dataset, epsilon = 0):
    wasChanged = True
    acc1 = evaluate_tree.evaluate_tree(root, validation_dataset)
    while(wasChanged):
        wasChanged = prune_tree_internal(root, tree, prob_Y, validation_dataset,acc1, epsilon)