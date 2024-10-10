import numpy as np
from coordSystem import Coords

def standart(direction: Coords):
    return 1.0

class Antenna:
    def __init__(self, coords: Coords, diahramm = standart, power = 1):
        self.position = coords
        self.diagramm = standart
        self.power = power

    def get_cordinates(self):
        return self.position
    
    def directivity(self, direction: Coords):
        """Возвращает диаграмму направленности антенны. Для упрощения считаем её всенаправленной."""
        # Здесь можно использовать реальные диаграммы направленности
        return self.diagramm(direction)

    def rotate_vector(self, vector):
        """Применяет вращение к вектору направления с учётом углов ориентации антенны"""
        alpha, beta, gamma = self.orientation.x, self.orientation.y, self.orientation.z

        # Матрицы вращения вокруг осей x, y, z
        R_x = np.array([[1, 0, 0],
                        [0, np.cos(alpha), -np.sin(alpha)],
                        [0, np.sin(alpha), np.cos(alpha)]])
        
        R_y = np.array([[np.cos(beta), 0, np.sin(beta)],
                        [0, 1, 0],
                        [-np.sin(beta), 0, np.cos(beta)]])
        
        R_z = np.array([[np.cos(gamma), -np.sin(gamma), 0],
                        [np.sin(gamma), np.cos(gamma), 0],
                        [0, 0, 1]])

        rotation_matrix = R_z @ R_y @ R_x
        
        return rotation_matrix @ vector