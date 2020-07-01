from load_data.load_data import load_from_data
from neighborhood_classifier.radius_calculator import calculate_instances_neighbours
from code_classes.Instance import Instance
from neighborhood_classifier.prediction_compute import predict_class


def main():
    file_name = 'data/heart.csv'
    data = load_from_data(file_name).to_numpy()

    instances_info = list()

    for instance in data:
        instance_neighborhood = calculate_instances_neighbours(data, instance)
        info = Instance(instance, instance_neighborhood)
        instances_info.append(info)

    for instance in instances_info:
        prediction_class = predict_class(instance)
        instance.set_prediction_class(prediction_class)


if __name__ == "__main__":
    main()
