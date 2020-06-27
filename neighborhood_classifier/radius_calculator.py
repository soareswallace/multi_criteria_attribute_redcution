import numpy as np


MIN_DISTANCE = 0
MAX_DISTANCE = 1


def calculate_euclidean_distance(instance_a, instance_b):
    return np.linalg.norm(instance_b - instance_a)


def calculate_instances_neighbours(data, test_instance):
    for data_instance in data:
        comparison = data_instance == test_instance
        equal_arrays = comparison.all()
        if not equal_arrays:
            distance_between_instances = calculate_euclidean_distance(test_instance, data_instance)
            if distance_between_instances <= MAX_DISTANCE:
                print(distance_between_instances)
