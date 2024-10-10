
import RLS
import coordSystem
from reflectionPoint import ReflectivePoint
from solver import Solver

def calculate_reflected_signal(antenna: RLS.Antenna, reflective_point: ReflectivePoint):
    return reflective_point.reflect_signal(antenna, antenna.get_cordinates())

def init_antenna():
    antenna_position = coordSystem.Coords(0, 0, 0)
    reflective_point_position = coordSystem.Coords(5, 5, 0)
    
    # Создаем объекты
    antenna = RLS.Antenna(antenna_position)
    reflective_point = ReflectivePoint(reflective_point_position, reflectivity=1)
    
    solver = Solver(antenna, [reflective_point])

    result = solver.calculate_received_signal()
    
    print(f"Мощность сигнала на приёмнике: {result:.4f}")

def main():
    init_antenna()

if __name__ == '__main__':
    main()