from load_data.load_data import load_from_data
from neighborhood_classifier.nec_phase_functions import generate_instances_info
from neighborhood_classifier.prediction_compute import predict_classes_in_instances_info
from NDC_files.ndc_phase_functions import compute_ndc_attributes
from math import sqrt, exp
from processing_data.feature_reduction import best_features

a = 0
b = 0
c = 0
d = 0


def main():
    global a, d, b, c
    print("Loading data from CSV")

    file_name = 'data/heart.csv'
    data = load_from_data(file_name)
    data_size = len(data.to_numpy())
    number_of_attributes = len(data.to_numpy()[0]) - 1

    #NEC PHASE

    print("Initial phase using the whole attributes available.")
    print("Running NEC phase...")
    instances_info = list()
    instances_info = generate_instances_info(data.to_numpy(), number_of_attributes, instances_info)

    print("Predicting classes based on NEC...")
    instances_info, correct_predictions, incorrect_predictions = predict_classes_in_instances_info(instances_info)

    print("Predictions using NEC reach " + str((correct_predictions/data_size)*100) + "%")

    # NDER PHASE

    print("Going to NDER phase...")
    E_at = incorrect_predictions/data_size

    number_of_attributes_used = 1
    optimum_number_of_attributes = 1
    optimum_E_a = E_at

    top_features = best_features(data, number_of_attributes)

    print("Running NDER for each attribute to found the best one...")
    while number_of_attributes_used < number_of_attributes:
        # NDERR PHASE

        # print("Generating a new data instance info for " + str(number_of_attributes_used) + " attribute")
        instances_info = generate_instances_info(data.to_numpy(), number_of_attributes_used, instances_info)

        # print("Predicting classes based on new NEC...")
        instances_info, correct_predictions, incorrect_predictions = predict_classes_in_instances_info(
            instances_info,
            False
        )

        # print("Correct predictions using new NEC: " + str((correct_predictions / data_size) * 100) + "%")

        current_E_a = incorrect_predictions/data_size

        # COMPUTE NDC ATTRIBUTES BASED ON NEW NEC PARAMETERS, IF APPLICABLE

        if current_E_a < optimum_E_a:
            a, b, c, d = compute_ndc_attributes(instances_info)
            optimum_E_a = current_E_a
            optimum_number_of_attributes = number_of_attributes_used
            # print("[ALERT] - Founded a better number of attributes: " + str(number_of_attributes_used))

        number_of_attributes_used += 1

    print("[ALERT] - Optimum E_a: " + str(optimum_E_a * 100))
    print("[ALERT] - Using " + str(optimum_number_of_attributes) + " attributes.")

    print("Entering the NDC phase, using correlation coefficient")

    sigma = (a * d - b * c) / sqrt((a + b) * (c + d) * (a + c) * (b + d))
    D_sigma = exp(-(1 - sigma))

    print("Using a correlation coefficient of: " + str(sigma))

    harmonic_mean = 1/((1/2)*((1/(1-optimum_E_a))+(1/(D_sigma))))

    print("Harmonic mean of: " + str(harmonic_mean))


if __name__ == "__main__":
    main()
