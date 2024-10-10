from RLS import Antenna
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