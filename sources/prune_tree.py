from sources import evaluate_tree
from sources.create_tree import tree_len

def prune(root,node, prob_Y, validation_dataset, epsilon):
    if(node.left.isLeaf and node.right.isLeaf):
        acc1 = evaluate_tree.evaluate_tree(root, validation_dataset)
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
            None
        else:
            node.left = nodeLeft
            node.right = nodeRight
            node.position = nodePosition
            node.label = nodeLabel
            node.isLeaf = False



def prune_tree(root,tree, prob_Y, validation_dataset,acc1, epsilon = 0):
    if(not tree.left.isLeaf):
        prune_tree(root,tree.left, prob_Y, validation_dataset, epsilon)
    if(not tree.right.isLeaf):
        prune_tree(root,tree.right, prob_Y, validation_dataset, epsilon)
    prune(root,tree, prob_Y, validation_dataset, epsilon)

