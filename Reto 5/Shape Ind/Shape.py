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
