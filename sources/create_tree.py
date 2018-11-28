from math import log2
import random


class Node:

    def __init__(self, label, position, isLeaf):
        self.left = None
        self.right = None
        self.label = label
        self.position = position
        self.isLeaf = isLeaf

    def insertLeft(self, child):
        self.left = child

    def insertRight(self, child):
        self.right = child



def create_tree(training_set,feature_bagging, div= 1):
    decision_tree = None
    node_queue = list()
    dataset_queue = list()
    dataset_queue.insert(0, training_set)
    while(len(dataset_queue) > 0):
        dataset = dataset_queue.pop(0)
        transposed_dataset = list(map(list, zip(*dataset)))
        prob_arr = list()
        for i in range(len(transposed_dataset)):
            prob_arr.insert(len(prob_arr), (i, compute_probabilites(transposed_dataset[i])))
        prob_arr_len = len(prob_arr) - 1
        H_Y = compute_entropy(prob_arr[prob_arr_len][1])
        mutual_inf = 0
        label = None
        position = None
        internal = 1
        if (H_Y > 0):
            feature_sample = random.sample(range(0, prob_arr_len), feature_bagging)
            for i in feature_sample:
                 prob_var = prob_arr[i][1]
                 pos = prob_arr[i][0]
                 conditional_entropies = list()
                 prob_var_len = len(prob_var)
                 for j in range(prob_var_len):
                    conditional_entropies.insert(j,compute_conditional_entropy(prob_arr[prob_arr_len], dataset, lambda el: el[pos] == prob_var[j][0]))
                 x = (prob_var_len - 1) // div + (prob_var_len - 1) % div
                 sample = random.sample(range(0, prob_var_len - 1), x)
                 for j in sample:
                    prob_X_less_eq = prob_var[:j+1]
                    prob_X_greater = prob_var[j+1:]
                    sum_x_less_eq = sum([x[1] for x in prob_X_less_eq])
                    sum_x_qreater = sum([x[1] for x in prob_X_greater])
                    prob_X_less_eq = list(map(lambda el: el[1]/sum_x_less_eq, prob_X_less_eq))
                    prob_X_greater = list(map(lambda el: el[1]/sum_x_qreater, prob_X_greater))
                    H_Y_X_less_eq = 0
                    H_Y_X_greater = 0
                    for k in range(len(prob_X_less_eq)):
                        H_Y_X_less_eq += conditional_entropies[k]*prob_X_less_eq[k]
                    tmp = len(prob_X_less_eq)
                    for k in range(len(prob_X_greater)):
                        H_Y_X_greater += conditional_entropies[tmp+k]*prob_X_greater[k]
                    H_Y_Xt = sum_x_less_eq*H_Y_X_less_eq + sum_x_qreater*H_Y_X_greater
                    tmp_mutual_inf = compute_mutual_inf(H_Y, H_Y_Xt)
                    if(tmp_mutual_inf > mutual_inf):
                        mutual_inf = tmp_mutual_inf
                        label = i
                        position = prob_var[j][0]
            new_node = Node(label, position, False)
            if(decision_tree == None):
                decision_tree = new_node
            split = split_dataset(label, position, dataset)
            dataset_queue.insert(len(dataset_queue), split[0])
            dataset_queue.insert(len(dataset_queue), split[1])
        else:
            new_node = Node(prob_arr_len, dataset[0][prob_arr_len], True)
            internal = 0
        if (len(node_queue) > 0):
            node = node_queue.pop(0)
            if (node.left):
                node.insertRight(new_node)
            else:
                node.insertLeft(new_node)
                node_queue.insert(0, node)
        if(internal == 1):
            node_queue.insert(len(node_queue), new_node)
    transposed_training_set = list(map(list, zip(*training_set)))
    prob_Y = compute_probabilites(transposed_training_set[len(transposed_training_set) - 1])
    return (decision_tree, prob_Y)

def compute_probabilites(array):
    probabilites = list()
    sum = len(array)
    while(len(array) > 0):
        label = array.pop(0)
        k = array.count(label) + 1
        probabilites.insert(0,(label, k/sum))
        array = list(filter(lambda a: a != label, array))
    probabilites.sort(key=lambda tup: tup[0])
    return probabilites


def compute_mutual_inf(H_Y, H_Y_X):
    return H_Y - H_Y_X


def compute_entropy(Y):
    entropy = 0
    for tuple in Y:
        entropy -= tuple[1]*log2(tuple[1])
    return entropy


def compute_conditional_entropy(Y, training_set, condition):
    entropy = 0
    y_pos = Y[0]
    Y = Y[1]
    X_t = list(filter(condition, training_set))
    len_X_t = len(X_t)
    for el_Y in Y:
        fixed_Y = list(filter(lambda el: el[y_pos] == el_Y[0], X_t))
        len_Y = len(fixed_Y)
        prob = len_Y/len_X_t
        if(prob > 0):
            entropy -= prob*log2(prob)
    return entropy


def split_dataset(position, value, dataset):
    set_1 = list(filter(lambda x: x[position] <= value, dataset))
    set_2 = list(filter(lambda x: x[position] > value, dataset))
    return (set_1, set_2)

def tree_len(node):
    if(node == None):
        return 0
    else:
        return tree_len(node.left) + tree_len(node.right) + 1

def tree_bagging(training_set, b):
    n = len(training_set)
    bagged = list()


