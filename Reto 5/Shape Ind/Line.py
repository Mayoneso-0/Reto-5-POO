import math

import Point

# Creamos una clase para representar una línea con un punto de inicio y un punto de fin
class Line:
    def __init__(self, start: "Point" = None, end: "Point" = None
                 , length: float = 0, slope: float = 0):
        self.start = start
        self.end = end
        self.length = length
        self.slope = slope
    
    # Definimos un método para calcular la longitud de la línea 
    # usando la fórmula de distancia
    def compute_length(self):
        length = ((self.start.x - self.end.x)**2 
                  + (self.start.y - self.end.y)**2)**0.5
        return length
    
    # Definimos un método para calcular la pendiente de la línea 
    # usando la fórmula de la tangente
    def compute_slope(self):
        slope = math.atan2((self.end.y - self.start.y),
                           (self.end.x - self.start.x)) * 180 / math.pi
        return slope
