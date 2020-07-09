from load_data.load_data import load_from_data
from neighborhood_classifier.nec_phase_functions import calculate_instances_neighbours
from code_classes.Instance import Instance
from neighborhood_classifier.prediction_compute import predict_class


def main():
    print("Loading data from CSV")

    file_name = 'data/vehicle.csv'
    data = load_from_data(file_name).to_numpy()
    data_size = len(data)
    correct_predictions = 0
    incorrect_predictions = 0

    instances_info = list()

    print("Running NEC phase...")
    #TODO Bring this line of code to the nec_phase_functions file
    for instance in data:
        instance_neighborhood = calculate_instances_neighbours(data, instance)
        info = Instance(instance, instance_neighborhood)
        instances_info.append(info)

    print("Predicting classes based on NEC...")
    for instance in instances_info:
        prediction_class = predict_class(instance)
        instance.set_prediction_class(prediction_class)
        if instance.get_prediction_class() == instance.get_instance_class():
            correct_predictions += 1
        else:
            incorrect_predictions += 1

    print("Predictions using NEC reach " + str((correct_predictions/data_size)*100) + "%")

    print("Going to NDER phase...")
    E_at = incorrect_predictions/data_size


if __name__ == "__main__":
    main()
