from load_data.load_data import load_from_data
from neighborhood_classifier.nec_phase_functions import generate_instances_info
from neighborhood_classifier.prediction_compute import predict_classes_in_instances_info
from NDC_files.ndc_phase_functions import compute_ndc_attributes
from math import sqrt, exp

a = 0
b = 0
c = 0
d = 0
maximum_harmonic_mean = 0.0


def main():
    global a, d, b, c, maximum_harmonic_mean
    print("Loading data from CSV")

    file_name = 'data/vehicle.csv'
    data = load_from_data(file_name).to_numpy()
    data_size = len(data)
    number_of_attributes = len(data[0]) - 1

    print("Initial phase using the whole attributes available.")
    print("Running NEC phase...")
    instances_info = list()
    instances_info = generate_instances_info(data, number_of_attributes, instances_info)

    print("Predicting classes based on NEC...")
    instances_info, correct_predictions, incorrect_predictions = predict_classes_in_instances_info(instances_info)

    print("Predictions using NEC reach " + str((correct_predictions/data_size)*100) + "%")

    print("Going to NDER phase...")
    E_at = incorrect_predictions/data_size
    optimum_E_a = E_at

    index_of_attribute_used = 0
    index_of_best_attribute = 0

    while index_of_attribute_used < number_of_attributes:
        print("Generating a new data instance info for attribute number " + str(index_of_attribute_used))
        instances_info = generate_instances_info(data, index_of_attribute_used, instances_info)

        print("Predicting classes based on new NEC...")
        instances_info, correct_predictions, incorrect_predictions = predict_classes_in_instances_info(
            instances_info,
            False
        )

        print("Correct predictions using new NEC: " + str((correct_predictions / data_size) * 100) + "%")

        current_E_a = incorrect_predictions/data_size

        if current_E_a < optimum_E_a:
            index_of_best_attribute = index_of_attribute_used
            optimum_E_a = current_E_a

        index_of_attribute_used += 1

    print("Finished NDERR. Optimum number of attributes is " + str(index_of_best_attribute) + " attributes.")



if __name__ == "__main__":
    main()
