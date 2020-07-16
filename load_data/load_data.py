import pandas as pd
from sklearn import preprocessing


def load_from_data(file_name):
    dataFrame = pd.read_csv(file_name, header=None)
    number_of_attributes = len(dataFrame[:0].columns) - 1
    index = 0
    while index < number_of_attributes:
        dataFrame[index] = dataFrame[index] / dataFrame[index].max()
        index+=1

    return dataFrame

