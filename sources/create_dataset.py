from random import randint

def create_dataset(filename, training = 5, validation = 1, test = 1):
    f = open("./files/" + filename, "r")
    content = f.read()
    tuples = content.split("\n")
    tuples.pop(0)
    for i in range (len(tuples)):
        tuples[i] = tuple(tuples[i].split(";"))

    training_set = list()
    validation_set = list()
    test_set = list()

    tuples.pop(len(tuples) -1)

    for i in range (len(tuples)):
        tuples[i] = tuple(map(float, tuples[i]))

    while(len(tuples) >= training + validation + test):
        for i in range(training):
            rand = randint(0, len(tuples) - 1)
            training_set.insert(0, tuples[rand])
            tuples.pop(rand)
        for i in range(validation):
            rand = randint(0, len(tuples) - 1)
            validation_set.insert(0, tuples[rand])
            tuples.pop(rand)
        for i in range(test):
            rand = randint(0, len(tuples) - 1)
            test_set.insert(0, tuples[rand])
            tuples.pop(rand)


    return [training_set, validation_set, test_set]
