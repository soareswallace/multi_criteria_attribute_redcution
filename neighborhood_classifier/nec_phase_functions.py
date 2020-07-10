import numpy as np
from code_classes.Instance import Instance

MIN_DISTANCE = 0
MAX_DISTANCE = 1
MAX_NEIGHBORS = 5


def calculate_euclidean_distance(instance_a, instance_b):
    return np.linalg.norm(instance_b - instance_a)


def calculate_instances_neighbours(data, test_instance, number_of_attributes):
    distances = list()
    for data_instance in data:
        comparison = data_instance == test_instance
        equal_arrays = comparison.all()
        if not equal_arrays:
            distance_between_instances = calculate_euclidean_distance(test_instance[:number_of_attributes], data_instance[:number_of_attributes])
            distances.append((data_instance, distance_between_instances))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    # TODO Implement using neighborhood radius and change MAX_NEIGHBORS to radius
    for i in range(MAX_NEIGHBORS):
        neighbors.append(distances[i][0])
    return neighbors


def generate_instances_info(data, number_of_attributes):
    instances_info = list()

    for instance in data:
        instance_neighborhood = calculate_instances_neighbours(data, instance, number_of_attributes)
        info = Instance(instance, instance_neighborhood)
        instances_info.append(info)

    return instances_info



