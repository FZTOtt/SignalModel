
import RLS
import coordSystem
from reflectionPoint import ReflectivePoint
from solver import Solver

def calculate_reflected_signal(antenna: RLS.Antenna, reflective_point: ReflectivePoint):
    return reflective_point.reflect_signal(antenna, antenna.get_cordinates())

def init_antenna():
    active_antenna_position = coordSystem.Coords(0, 0, 0)
    passive_antenna_position = coordSystem.Coords(-10, -1, -1)
    reflective_point_position = coordSystem.Coords(5, 5, 0)
    
    # Создаем объекты
    active_antenna = RLS.Antenna(active_antenna_position)
    passive_antenna = RLS.Antenna(passive_antenna_position)
    reflective_point = ReflectivePoint(reflective_point_position, reflectivity=1)   
    
    solver = Solver(active_antenna, [reflective_point], recieve_antenna=passive_antenna)

    result = solver.calculate_received_signal()
    
    print(f"Мощность сигнала на приёмнике: {result:.4f}")

def main():
    init_antenna()

if __name__ == '__main__':
    main()