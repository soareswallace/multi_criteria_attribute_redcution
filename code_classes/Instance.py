class Instance:
    def __init__(self, array, neighbours):
        self.array = array
        self.neighbours = []

    def add_a_new_neighbour(self, neighbour):
        self.neighbours.append(neighbour)