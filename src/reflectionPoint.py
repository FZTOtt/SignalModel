from RLS import Antenna
from coordSystem import Coords


class ReflectivePoint:
    def __init__(self, position: Coords, reflectivity=1.0):
        self.position = position
            
    def reflectivity(self):
        """Возвращает коэффициент отражения, для простоты считаем его равным 1"""
        return 1
