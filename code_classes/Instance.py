class Instance:
    def __init__(self, instance_value, neighbours):
        self.instance_value = instance_value
        self.neighbours = neighbours

    def add_a_new_neighbours_to_instance_info(self, neighborhood):
        self.neighbours = neighborhood

    def set_instance_value(self, instance_value):
        self.instance_value = instance_value
