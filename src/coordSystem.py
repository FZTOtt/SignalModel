import numpy as np


class Coords:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z

    def print_coords(self):
        print(self.x, self.y, self.z)

    def distance_to(self, other):
        """Рассчитывает расстояние до другой точки"""
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

