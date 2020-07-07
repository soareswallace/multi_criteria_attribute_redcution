from code_classes import Instance


def count_class_occurencies(array_of_instances):
    classes_count = {}
    for instance in array_of_instances:
        if instance[13] in classes_count:
            classes_count[instance[13]] += 1
        else:
            classes_count[instance[13]] = 1
    return classes_count


def predict_class_base_on_max_occurencies(occurencies):
    return max(occurencies, key=occurencies.get)


def predict_class(instance_to_predict: Instance):
    classes_occurencies = count_class_occurencies(instance_to_predict.get_instance_neighbors())
    return predict_class_base_on_max_occurencies(classes_occurencies)

