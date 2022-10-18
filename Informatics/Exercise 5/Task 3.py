from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
    ]

def reverse_index(dataset):
    index_dictionary = {}
    for i in range(len(dataset)):
        for j in dataset[i].split():
            if j.lower() not in index_dictionary:
                index_dictionary[j.lower()] = [i]
            else:
                index_dictionary[j.lower()].append(i)
                index_dictionary[j.lower()].sort()

    return  index_dictionary

# You can see the output of your function here
print(reverse_index(dataset))
