class Instance:
    def __init__(self, instance_value, neighbours):
        self.instance_value = instance_value
        self.neighbours = neighbours
        self.prediction_class = ''

    def set_instance_value(self, instance_value):
        self.instance_value = instance_value

    def add_a_new_neighbours_to_instance_info(self, neighborhood):
        self.neighbours = neighborhood

    def get_instance_neighbors(self):
        return self.neighbours

    def set_prediction_class(self, prediction):
        self.prediction_class = prediction

    def get_prediction_class(self):
        return self.prediction_class

    def get_instance_class(self):
        last_index_position = len(self.instance_value) - 1
        return self.instance_value[last_index_position]
