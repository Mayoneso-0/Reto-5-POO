import Line
import Shape

# Definimos la subclase Rectangle que hereda de Shape
class Rectangle(Shape):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None, 
                 ancho: float = None, alto: float = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = True
        self.ancho = ancho
        self.alto = alto

        # Validamos que se proporcionen los datos correctos para un rectángulo
        if len(self.vertices) != 4 and len(self.edges) != 4:
            print("Error: Parametros no validos para Rectangulo")

        # Se se propicionan las aristas completamos los vertices y el ancho y alto
        if len(self.edges) != 0:
            self.vertices = [self.edges[0].start,self.edges[0].end,
                             self.edges[2].start,self.edges[2].end]
            self.alto = self.edges[0].compute_length()
            self.ancho = self.edges[1].compute_length()
        # Si se proporcionan los vertices completamos las aristas y el ancho y alto
        elif len(self.vertices) != 0:
            self.edges = [Line(start = self.vertices[0], end = self.vertices[1]),
                          Line(start = self.vertices[1], end = self.vertices[2]),
                          Line(start = self.vertices[2], end = self.vertices[3]),
                          Line(start = self.vertices[3], end = self.vertices[0]),]
            self.alto = self.edges[0].compute_length()
            self.ancho = self.edges[1].compute_length()
        # Si no se proporcionan los vertices ni las aristas, mostramos un error
        else:
            print("Error: Falta de datos para el rectangulo")
    
    # Definimos un método para calcular el área del rectángulo
    def compute_area(self):
        return self.alto*self.ancho
    # Definimos un método para calcular el perímetro del rectángulo
    def compute_perimeter(self):
        return self.alto*2 + self.ancho*2
    # Definimos un método para calcular los ángulos internos del rectángulo
    def compute_inner_angle(self):
        self.inner_angle = [abs(self.edges[0].compute_slope() - \
                                self.edges[1].compute_slope()),
                            abs(self.edges[1].compute_slope() - \
                                self.edges[2].compute_slope()),
                            abs(self.edges[2].compute_slope() - \
                                self.edges[3].compute_slope()),
                            abs(self.edges[3].compute_slope() - \
                                self.edges[0].compute_slope())]
        for i in range(len(self.inner_angle)):
            if self.inner_angle[i] > 180:
                self.inner_angle[i] = 360 - self.inner_angle[i]
        return self.inner_angle

class Square(Rectangle):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = True

        # Validamos que se proporcionen los datos correctos para un cuadrado
        if len(self.vertices) != 4 and len(self.edges) != 4:
            print("Error: Parametros no validos para Cuadrado")
        if len(self.edges) != 0:
            if self.edges[0].compute_length() != self.edges[1].compute_length() or \
               self.edges[1].compute_length() != self.edges[2].compute_length() or \
               self.edges[2].compute_length() != self.edges[3].compute_length() or \
               self.edges[3].compute_length() != self.edges[0].compute_length():
                print("Error: Lados no forman un cuadrado")
        elif len(self.vertices) != 0:
            if self.vertices[0].x != self.vertices[1].x or \
               self.vertices[1].y != self.vertices[2].y or \
               self.vertices[2].x != self.vertices[3].x or \
               self.vertices[3].y != self.vertices[0].y:
                print("Error: Vertices no forman un cuadrado")

    # Definimos un método para calcular el área del cuadrado
    def compute_area(self):
        return super().compute_area()
    # Definimos un método para calcular el perímetro del cuadrado
    def compute_perimeter(self):
        return super().compute_perimeter()
    # Definimos un método para calcular los ángulos internos del cuadrado
    def compute_inner_angle(self):
        return super().compute_inner_angle()
