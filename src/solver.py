from RLS import Antenna
from reflectionPoint import ReflectivePoint


class Solver:
    def __init__(self, antenna: Antenna, reflective_points: list[ReflectivePoint], attenuation_model = 'squared'):
        """Инициализация для рассчета принятого сигнала антенной, совмещенной с передатчиком, от блестящих точек"""
        self.antenna = antenna
        self.reflective_points = reflective_points
        self.attenuation_model = attenuation_model

    def attenuate(self, signal, distance):
        if self.attenuation_model == 'squared':
            return signal / (distance ** 2)

    def calculate_received_signal(self):
        """Рассчитывает сигнал, принятый антенной после отражения от точек"""
        total_signal = 0.0
        
        for point in self.reflective_points:

            distance_to_point = self.antenna.position.distance_to(point.position) # расстояние до точки 
            
            power = self.antenna.directivity(point.position) * self.antenna.power # мощность сигнала в направлении точки 
            signal_at_point = self.attenuate(power, distance_to_point)
                        
            distance_to_antenna = point.position.distance_to(self.antenna.position) # расстояние от точки до антенны

            reflected_signal_to_antenna = self.attenuate(signal_at_point * point.reflectivity(), distance_to_antenna) # Сигнал, пришедший на антенну

            accepted_signal = self.antenna.directivity(distance_to_antenna) * reflected_signal_to_antenna
            
            total_signal += accepted_signal
        
        return total_signal