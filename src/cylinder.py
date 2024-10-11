import numpy as np

from coordSystem import Coords

class Cylinder:
    def __init__(self, base_center:Coords, height, radius, orientation, num_segments):
        self.base_center = base_center  # Центр основания цилиндра
        self.height = height
        self.radius = radius
        self.orientation = orientation
        self.num_segments = num_segments  # Количество сегментов для триангуляции боковой поверхности

        self.mesh = self.generate_mesh()

    def generate_mesh(self):
        """Генерация треугольной сетки для цилиндра"""
        vertices = []
        faces = []

        # Генерация боковой поверхности
        for i in range(self.num_segments):
            theta = 2 * np.pi * i / self.num_segments
            next_theta = 2 * np.pi * (i + 1) / self.num_segments

            # Верхняя точка
            top1 = np.array([self.base_center[0] + self.radius * np.cos(theta),
                             self.base_center[1] + self.height,
                             self.base_center[2] + self.radius * np.sin(theta)])

            # Нижняя точка
            bottom1 = np.array([self.base_center[0] + self.radius * np.cos(theta),
                                self.base_center[1],
                                self.base_center[2] + self.radius * np.sin(theta)])

            # Следующие точки для боковой поверхности
            top2 = np.array([self.base_center[0] + self.radius * np.cos(next_theta),
                             self.base_center[1] + self.height,
                             self.base_center[2] + self.radius * np.sin(next_theta)])

            bottom2 = np.array([self.base_center[0] + self.radius * np.cos(next_theta),
                                self.base_center[1],
                                self.base_center[2] + self.radius * np.sin(next_theta)])

            # Добавляем треугольники
            vertices.extend([top1, bottom1, top2, bottom2])
            faces.append([top1, bottom1, bottom2])  # Треугольник 1
            faces.append([top1, bottom2, top2])     # Треугольник 2

        return faces

    def get_mesh(self):
        return self.mesh
    