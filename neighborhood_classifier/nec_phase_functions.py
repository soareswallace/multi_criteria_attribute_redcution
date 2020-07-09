import numpy as np


MIN_DISTANCE = 0
MAX_DISTANCE = 1
MAX_NEIGHBORS = 5


def calculate_euclidean_distance(instance_a, instance_b):
    return np.linalg.norm(instance_b - instance_a)


def calculate_instances_neighbours(data, test_instance):
    distances = list()
    for data_instance in data:
        comparison = data_instance == test_instance
        equal_arrays = comparison.all()
        array_len = len(data_instance) - 1
        if not equal_arrays:
            distance_between_instances = calculate_euclidean_distance(test_instance[:array_len], data_instance[:array_len])
            distances.append((data_instance, distance_between_instances))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    # TODO Implement using neighborhood radius and change MAX_NEIGHBORS to radius
    for i in range(MAX_NEIGHBORS):
        neighbors.append(distances[i][0])
    return neighbors



