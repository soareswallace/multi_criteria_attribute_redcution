import pandas as pd


def load_from_data(file_name):
    return pd.read_csv(file_name, header=None)
