import numpy as np


class Coords:
    def __init__(self, x, y, z, alpha = 0, betta = 0, gamma = 0):
        self.x = x
        self.y = y 
        self.z = z
        self.alpha = alpha
        self.betta = betta
        self.gamma = gamma

    def print_coords(self):
        print(self.x, self.y, self.z)

    def get_coords(self):
        return np.array([self.x, self.y, self.z])

    def distance_to(self, other) -> float:
        """Рассчитывает расстояние до другой точки"""
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

