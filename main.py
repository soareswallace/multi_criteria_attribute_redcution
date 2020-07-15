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

    number_of_attributes_used = 1
    optimum_number_of_attributes = 1
    optimum_E_a = E_at

    while number_of_attributes_used < number_of_attributes:
        print("Generating a new data instance info for " + str(number_of_attributes_used) + " attribute")
        instances_info = generate_instances_info(data, number_of_attributes_used, instances_info)

        print("Predicting classes based on new NEC...")
        instances_info, correct_predictions, incorrect_predictions = predict_classes_in_instances_info(
            instances_info,
            False
        )

        print("Correct predictions using new NEC: " + str((correct_predictions / data_size) * 100) + "%")

        print("Computing a, b, c and d for NDC...")

        a, b, c, d = compute_ndc_attributes(instances_info)
        sigma = (a * d - b * c) / sqrt((a + b) * (c + d) * (a + c) * (b + d))
        D_sigma = exp(-(1 - sigma))

        print("Computing harmonic mean...")

        current_harmonic_mean = 1/((1/2)*((1/(1-optimum_E_a))+(1/(D_sigma))))

        if current_harmonic_mean > maximum_harmonic_mean:
            maximum_harmonic_mean = current_harmonic_mean
            optimum_number_of_attributes = number_of_attributes_used
            print("Found a better result for harmonic mean. With " + str(optimum_number_of_attributes) + " attributes.")

        number_of_attributes_used += 1

    print("Algorithm finished! The optimum number of attributes is " + str(optimum_number_of_attributes) + " attributes.")


if __name__ == "__main__":
    main()
