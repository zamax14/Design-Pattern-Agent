"""
Visitor — Ejemplo

Separa algoritmos de los objetos sobre los que operan.
Usa double dispatch para ejecutar la operación correcta según el tipo.
"""

from abc import ABC, abstractmethod


class Visitor(ABC):
    """Interfaz Visitor: un método visit por tipo de elemento."""

    @abstractmethod
    def visit_circle(self, circle: "Circle") -> str:
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: "Rectangle") -> str:
        pass

    @abstractmethod
    def visit_triangle(self, triangle: "Triangle") -> str:
        pass


class Shape(ABC):
    """Interfaz Element con accept."""

    @abstractmethod
    def accept(self, visitor: Visitor) -> str:
        pass


class Circle(Shape):
    """Elemento concreto: círculo."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def accept(self, visitor: Visitor) -> str:
        return visitor.visit_circle(self)


class Rectangle(Shape):
    """Elemento concreto: rectángulo."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def accept(self, visitor: Visitor) -> str:
        return visitor.visit_rectangle(self)


class Triangle(Shape):
    """Elemento concreto: triángulo."""

    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def accept(self, visitor: Visitor) -> str:
        return visitor.visit_triangle(self)


class AreaCalculator(Visitor):
    """Visitor concreto: calcula áreas."""

    def visit_circle(self, circle: Circle) -> str:
        area = 3.14159 * circle.radius ** 2
        return f"Área círculo (r={circle.radius}): {area:.2f}"

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        area = rectangle.width * rectangle.height
        return f"Área rectángulo ({rectangle.width}x{rectangle.height}): {area:.2f}"

    def visit_triangle(self, triangle: Triangle) -> str:
        area = 0.5 * triangle.base * triangle.height
        return f"Área triángulo (b={triangle.base}, h={triangle.height}): {area:.2f}"


class PerimeterCalculator(Visitor):
    """Visitor concreto: calcula perímetros."""

    def visit_circle(self, circle: Circle) -> str:
        perimeter = 2 * 3.14159 * circle.radius
        return f"Perímetro círculo (r={circle.radius}): {perimeter:.2f}"

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        perimeter = 2 * (rectangle.width + rectangle.height)
        return f"Perímetro rectángulo ({rectangle.width}x{rectangle.height}): {perimeter:.2f}"

    def visit_triangle(self, triangle: Triangle) -> str:
        # Aproximación para triángulo isósceles
        side = ((triangle.base / 2) ** 2 + triangle.height ** 2) ** 0.5
        perimeter = triangle.base + 2 * side
        return f"Perímetro triángulo (b={triangle.base}, h={triangle.height}): {perimeter:.2f}"


if __name__ == "__main__":
    shapes: list[Shape] = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4),
    ]

    print("--- Visitor: Cálculo de Áreas ---")
    area_calc = AreaCalculator()
    for shape in shapes:
        print(f"  {shape.accept(area_calc)}")

    print("\n--- Visitor: Cálculo de Perímetros ---")
    perim_calc = PerimeterCalculator()
    for shape in shapes:
        print(f"  {shape.accept(perim_calc)}")
