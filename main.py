from load_data.load_data import load_from_data
from neighborhood_classifier.radius_calculator import calculate_instances_neighbours
from code_classes.Instance import Instance
from neighborhood_classifier.prediction_compute import predict_class


def main():
    file_name = 'data/heart.csv'
    data = load_from_data(file_name).to_numpy()
    data_size = len(data)
    correct_predictions = 0
    incorrect_predictions = 0

    instances_info = list()

##NEC PHASE
    for instance in data:
        instance_neighborhood = calculate_instances_neighbours(data, instance)
        info = Instance(instance, instance_neighborhood)
        instances_info.append(info)

    for instance in instances_info:
        prediction_class = predict_class(instance)
        instance.set_prediction_class(prediction_class)
        if instance.get_prediction_class() == instance.get_instance_class():
            correct_predictions += 1
        else:
            incorrect_predictions += 1

    print("Predictions using KNN reach " + str(correct_predictions/len(data)*100) + "%")

##NDER PHASE
    E_at = incorrect_predictions/data_size


if __name__ == "__main__":
    main()
