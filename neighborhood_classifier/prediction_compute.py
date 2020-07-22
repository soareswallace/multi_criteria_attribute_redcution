from code_classes import Instance


def count_class_occurencies(array_of_instances):
    classes_count = {}
    for instance in array_of_instances:
        last_index_position = len(instance) - 1
        if instance[last_index_position] in classes_count:
            classes_count[instance[last_index_position]] += 1
        else:
            classes_count[instance[last_index_position]] = 1
    return classes_count


def predict_class_base_on_max_occurencies(occurencies):
    return max(occurencies, key=occurencies.get)


def predict_class(instance_to_predict: Instance):
    classes_occurencies = count_class_occurencies(instance_to_predict.get_instance_neighbors())
    return predict_class_base_on_max_occurencies(classes_occurencies)


def predict_classes_in_instances_info(instances_info, using_whole_data_attributes=True):
    correct_predictions = 0
    incorrect_predictions = 0

    for instance in instances_info:
        if instance.get_instance_neighbors():
            prediction_class = predict_class(instance)
        else:
            #don't know how to handle
            prediction_class = -1
        if using_whole_data_attributes:
            instance.set_prediction_class_using_whole_attributes(prediction_class)
            if instance.get_prediction_class_using_whole_attributes() == instance.get_instance_class():
                correct_predictions += 1
            else:
                incorrect_predictions += 1
        else:
            instance.set_prediction_class_using_reduced_attributes(prediction_class)
            if instance.get_prediction_class_using_reduced_attributes() == instance.get_instance_class():
                correct_predictions += 1
            else:
                incorrect_predictions += 1

    return instances_info, correct_predictions, incorrect_predictions
