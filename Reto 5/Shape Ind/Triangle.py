import Line
import Shape

# Definimos la subclase Triangle que hereda de Shape
class Triangle(Shape):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)

        # Validamos que se proporcionen los datos correctos para un rectángulo
        if len(self.vertices) != 3 and len(self.edges) != 3:
            print("Error: Parametros no validos para un Triangulo")
        
        # Si se proporcionan las aristas completamos los vertices
        if len(self.edges) != 0:
            self.vertices = [self.edges[0].start, self.edges[0].end,
                             self.edges[1].start, self.edges[1].end,
                             self.edges[2].start, self.edges[2].end]
        # Si se proporcionan los vertices completamos las aristas
        elif len(self.vertices) != 0:
            self.edges = [Line(start = self.vertices[0], end = self.vertices[1]),
                          Line(start = self.vertices[1], end = self.vertices[2]),
                          Line(start = self.vertices[2], end = self.vertices[0]),]
        # Si no se proporcionan los vertices ni las aristas, mostramos un error
        else:
            print("Error: Falta de datos para el triangulo")
        
    # Definimos un método para calcular el área del triángulo 
    # usando la fórmula de Herón
    def compute_area(self):
        a = self.edges[0].compute_length()
        b = self.edges[1].compute_length()
        c = self.edges[2].compute_length()
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
    # Definimos un método para calcular el perímetro del triángulo
    def compute_perimeter(self):
        return self.edges[0].compute_length() + \
               self.edges[1].compute_length() + \
               self.edges[2].compute_length()
    # Definimos un método para calcular los ángulos internos del triángulo
    def compute_inner_angle(self):
        self.inner_angle = [abs(self.edges[0].compute_slope() - \
                                self.edges[1].compute_slope()),
                            abs(self.edges[1].compute_slope() - \
                                self.edges[2].compute_slope()),
                            abs(self.edges[2].compute_slope() - \
                                self.edges[0].compute_slope())]
        for i in range(len(self.inner_angle)):
            if self.inner_angle[i] > 180:
                self.inner_angle[i] = 360 - self.inner_angle[i]
        return self.inner_angle

# Definimos la subclase Isosceles que hereda de Triangle
class Isosceles(Triangle):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = False

        # Validamos que se proporcionen los datos correctos 
        # para un triángulo isósceles
        if len(self.vertices) != 3 and len(self.edges) != 3:
            print("Error: Parametros no validos para un Triangulo Isosceles")
        if self.edges[0].compute_length() != self.edges[1].compute_length() and \
           self.edges[1].compute_length() != self.edges[2].compute_length() and \
           self.edges[2].compute_length() != self.edges[0].compute_length():
            print("Error: Lados no forman un Triangulo Isosceles")
    
    # Definimos un metodo para calcular el area, perímetro y
    # ángulos internos del triángulo isósceles
    def compute_area(self):
        return super().compute_area()
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_inner_angle(self):
        return super().compute_inner_angle()

# Definimos la subclase Equilateral que hereda de Triangle
class Equilateral(Triangle):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = True

        # Validamos que se proporcionen los datos correctos 
        # para un triángulo equilátero
        if len(self.vertices) != 3 and len(self.edges) != 3:
            print("Error: Parametros no validos para un Triangulo Equilatero")
        if self.edges[0].compute_length() != self.edges[1].compute_length() or \
           self.edges[1].compute_length() != self.edges[2].compute_length() or \
           self.edges[2].compute_length() != self.edges[0].compute_length():
            print("Error: Lados no forman un Triangulo Equilatero")
    
    # Definimos un método para calcular el área, perímetro y
    # ángulos internos del triángulo equilátero
    def compute_area(self):
        return super().compute_area()
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_inner_angle(self):
        return super().compute_inner_angle()

# Definimos la subclase Scalene que hereda de Triangle
class Scalene(Triangle):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = False

        # Validamos que se proporcionen los datos correctos 
        # para un triángulo escaleno
        if len(self.vertices) != 3 and len(self.edges) != 3:
            print("Error: Parametros no validos para un Triangulo Escaleno")
        if self.edges[0].compute_length() == self.edges[1].compute_length() or \
           self.edges[1].compute_length() == self.edges[2].compute_length() or \
           self.edges[2].compute_length() == self.edges[0].compute_length():
            print("Error: Lados no forman un Triangulo Escaleno")
    
    # Definimos un método para calcular el área, perímetro y
    # ángulos internos del triángulo escaleno
    def compute_area(self):
        return super().compute_area()
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_inner_angle(self):
        return super().compute_inner_angle()
    
# Definimos la subclase TriRectanble que hereda de Triangle
class TriRectanble(Triangle):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = False

        # Validamos que se proporcionen los datos correctos 
        # para un triángulo rectángulo
        if len(self.vertices) != 3 and len(self.edges) != 3:
            print("Error: Parametros no validos para un Triangulo Rectangulo")
        self.compute_inner_angle()
        if 90 not in self.inner_angle:
            print("Error: Lados no forman un Triangulo Rectangulo")
        
    # Definimos un método para calcular el área, perímetro y
    # ángulos internos del triángulo rectángulo
    def compute_area(self):
        return super().compute_area()
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_inner_angle(self):
        return super().compute_inner_angle()
