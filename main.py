from load_data.load_data import load_from_data
from neighborhood_classifier.radius_calculator import calculate_instances_neighbours


def main():
    file_name = 'data/heart.csv'
    data = load_from_data(file_name).to_numpy()
    for instance in data:
        calculate_instances_neighbours(data, instance)



if __name__ == "__main__":
    main()