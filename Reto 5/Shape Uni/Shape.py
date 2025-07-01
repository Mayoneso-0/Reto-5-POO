import math

# Creamos una clase para representar un punto con coordenadas x y
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

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

# Definimos la superclase Shape que representa una forma geométrica
class Shape():
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        self.vertices = vertices
        self.edges = edges
        self.inner_angle = inner_angle
        self.is_regular = is_regular

    # Métodos para computar el área, perímetro y ángulo interno de la forma
    # Estos métodos serán sobreescritos por las subclases
    def compute_area(self):
        return "Debe seleccionar una forma para computar su area"
    def compute_perimeter(self):
        return "Debe seleccionar una forma para computar su perimetro"
    def compute_inner_angle(self):
        return "Debe seleccionar una forma para computar sus angulos internos"
    
    # Definimos métodos para obtener y establecer los atributos de la forma
    def get_vertices(self):
        return self.vertices
    def get_edges(self):
        return self.edges
    def get_inner_angle(self):
        return self.inner_angle
    def get_is_regular(self):
        return self.is_regular
    def set_vertices(self, vertices):
        self.vertices = vertices
    def set_edges(self, edges):
        self.edges = edges 
    def set_inner_angle(self, inner_angle):
        self.inner_angle = inner_angle
    def set_is_regular(self, is_regular):
        self.is_regular = is_regular

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



# Ejemplo con un cuadrado 
punto1 = Point(0,0)
punto2 = Point(0,2)
punto3 = Point(2,2)
punto4 = Point(2,0)

listaPuntos1 = [punto1, punto2, punto3, punto4]

cuadrado1 = Square(vertices = listaPuntos1)

print("Area del cuadrado:", cuadrado1.compute_area())
print("Perimetro del cuadrado:", cuadrado1.compute_perimeter())
print("Angulos internos del cuadrado:", cuadrado1.compute_inner_angle())

print()
# Ejemplo con un triángulo rectángulo
punto5 = Point(0,0)
punto6 = Point(0,3)
punto7 = Point(4,0)

listaPuntos2 = [punto5, punto6, punto7]

trianguloRectangulo1 = TriRectanble(vertices = listaPuntos2)
print("Area del triangulo rectangulo:", trianguloRectangulo1.compute_area())
print("Perimetro del triangulo rectangulo:", trianguloRectangulo1.compute_perimeter())
print("Angulos internos del triangulo rectangulo:", trianguloRectangulo1.compute_inner_angle())

print()
# Ejemplo de set y get de is_regular
print("El triangulo rectangulo es regular?",trianguloRectangulo1.get_is_regular())
trianguloRectangulo1.set_is_regular(True)
print("El triangulo rectangulo es regular?",trianguloRectangulo1.get_is_regular())

