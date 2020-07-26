import numpy as np
from code_classes.Instance import Instance

NEIGHBORHOOD_RADIUS = 0.23


def calculate_euclidean_distance(instance_a, instance_b):
    return np.linalg.norm(instance_b - instance_a)


def calculate_instances_neighbours(data, test_instance, number_of_attributes):
    distances = list()
    for data_instance in data:
        comparison = data_instance == test_instance
        equal_arrays = comparison.all()
        if not equal_arrays:
            distance_between_instances = calculate_euclidean_distance(
                test_instance[:number_of_attributes],
                data_instance[:number_of_attributes]
            )
            distances.append((data_instance, distance_between_instances))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    instance_index = 0
    while instance_index < len(distances) and distances[instance_index][1] < NEIGHBORHOOD_RADIUS:
        neighbors.append(distances[instance_index][0])
        instance_index += 1
    return neighbors


def generate_instances_info(data, number_of_attributes, instances_info):
    if not instances_info: #Checking if instances_info is empty
        for instance in data:
            instance_neighborhood = calculate_instances_neighbours(data, instance, number_of_attributes)
            info = Instance(instance, instance_neighborhood)
            instances_info.append(info)
    else:
        for instance in instances_info:
            instance_neighborhood = calculate_instances_neighbours(
                data,
                instance.get_instance_values(),
                number_of_attributes
            )
            instance.update_neighborhood(instance_neighborhood)

    return instances_info



