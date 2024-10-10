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
