import numpy as np
from RLS import Antenna
from cylinder import Cylinder
from reflectionPoint import ReflectivePoint

class Solver:
    def __init__(self, active_antenna: Antenna, reflective_points: list[ReflectivePoint], attenuation_model = 'squared', recieve_antenna = Antenna | None):
        """Инициализация для рассчета принятого сигнала антенной, совмещенной с передатчиком, от блестящих точек"""
        self.active_antenna = active_antenna
        self.reflective_points = reflective_points
        self.attenuation_model = attenuation_model
        self.passive_antenna = recieve_antenna

    def attenuate(self, signal: float, distance: float) -> float:
        if self.attenuation_model == 'squared':
            return signal / (distance ** 2)

    def calculate_received_signal(self):
        """Рассчитывает сигнал, принятый антенной после отражения от точек"""
        total_signal = 0.0

        if self.passive_antenna == None:
            self.passive_antenna = self.active_antenna
        
        for point in self.reflective_points:

            active_antenna_point_distance = self.active_antenna.position.distance_to(point.position) # расстояние до точки 
            
            power = self.active_antenna.directivity(point.position) * self.active_antenna.power # мощность сигнала в направлении точки

            signal_at_point = self.attenuate(power, active_antenna_point_distance)
                        
            point_passive_antenna_distance = point.position.distance_to(self.passive_antenna.position) # расстояние от точки до антенны

            reflected_signal_to_passive_antenna = self.attenuate(signal_at_point * point.reflectivity(), point_passive_antenna_distance) # Сигнал, пришедший на антенну

            accepted_signal = self.passive_antenna.directivity(point.position) * reflected_signal_to_passive_antenna
            
            total_signal += accepted_signal
        
        return total_signal
    
    def __init__(self, antenna, objects: list[Cylinder]):
        self.antenna = antenna
        self.objects = objects

    def intersect_ray_triangle(ray_origin, ray_direction, v0, v1, v2):
        """Проверка пересечения луча с треугольником"""
        epsilon = 1e-8
        edge1 = v1 - v0
        edge2 = v2 - v0
        h = np.cross(ray_direction, edge2)
        a = np.dot(edge1, h)

        if -epsilon < a < epsilon:
            return False, None  # Луч параллелен треугольнику

        f = 1.0 / a
        s = ray_origin - v0
        u = f * np.dot(s, h)

        if u < 0.0 or u > 1.0:
            return False, None

        q = np.cross(s, edge1)
        v = f * np.dot(ray_direction, q)

        if v < 0.0 or u + v > 1.0:
            return False, None

        t = f * np.dot(edge2, q)
        if t > epsilon:  # Луч пересекает треугольник
            intersection_point = ray_origin + ray_direction * t
            return True, intersection_point
        else:
            return False, None
        
    def reflect_vector(direction, normal):
        """Отражает вектор относительно нормали"""
        return direction - 2 * np.dot(direction, normal) * normal

    def calculate_signal(self):
        total_signal = 0
        for obj in self.objects:
            for face in obj.get_mesh():
                v0, v1, v2 = face

                # Проверяем пересечение луча с треугольником
                intersects, intersection_point = self.intersect_ray_triangle(self.antenna.position.get_coords(),
                                                                        self.antenna.get_direction(), 
                                                                        v0, v1, v2)
                if intersects:
                    # Вычисляем нормаль треугольника
                    normal = np.cross(v1 - v0, v2 - v0)
                    normal = normal / np.linalg.norm(normal)

                    # Вычисляем отражённый сигнал
                    reflected_direction = self.reflect_vector(self.antenna.get_direction(), normal)

                    # Моделируем дальнейшее распространение сигнала и принимаем его
                    total_signal += self.antenna.receive_signal(reflected_direction)
        return total_signal