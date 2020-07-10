from load_data.load_data import load_from_data
from neighborhood_classifier.nec_phase_functions import generate_instances_info
from neighborhood_classifier.prediction_compute import predict_classes_in_instances_info


def main():
    print("Loading data from CSV")

    file_name = 'data/vehicle.csv'
    data = load_from_data(file_name).to_numpy()
    data_size = len(data)
    number_of_attributes = len(data[0]) - 1

    print("Initial phase using the whole attributes available.")
    print("Running NEC phase...")
    instances_info = generate_instances_info(data, number_of_attributes)

    print("Predicting classes based on NEC...")
    instances_info, correct_predictions, incorrect_predictions = predict_classes_in_instances_info(instances_info)

    print("Predictions using NEC reach " + str((correct_predictions/data_size)*100) + "%")

    print("Going to NDER phase...")
    E_at = incorrect_predictions/data_size

    number_of_attributes_used = 1

    while number_of_attributes_used < number_of_attributes:
        print("Generating a new data instance info for " + str(number_of_attributes_used) + " attribute")
        instances_info = generate_instances_info(data, number_of_attributes_used)

        print("Predicting classes based on new NEC...")
        instances_info, correct_predictions, incorrect_predictions = predict_classes_in_instances_info(instances_info)

        print("Correct predictions using new NEC: " + str((correct_predictions / data_size) * 100) + "%")

        better_E_a = incorrect_predictions/data_size

        if better_E_a < E_at:
            print("[ALERT] - Founded a better number of attributes: " + str(number_of_attributes_used))

        number_of_attributes_used += 1


if __name__ == "__main__":
    main()
