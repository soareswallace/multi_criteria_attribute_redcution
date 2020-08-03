def best_features(data, number_of_attributes):
    X = data.iloc[:, 0:number_of_attributes]
    y = data.iloc[:, -1]
    top_corr_features = data.corr().index
    correlation_values = data[top_corr_features].corr()[number_of_attributes][:number_of_attributes]
    return correlation_values.sort_values(ascending=False)