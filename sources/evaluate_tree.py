def evaluate_tree(root, dataset, prin=False):
    hits = 0
    for element in dataset:
        node = root
        while(node.left and node.right):
            if(element[node.label] <= node.position):
                node = node.left
            else:
                node = node.right
        result = node.position
        if(prin):
            print(result, element[len(element)-1])
        if(result == element[len(element)-1]):
            hits += 1
    return hits/(len(dataset))
