"""
Prototype — Ejemplo

Crea nuevos objetos clonando instancias existentes sin depender
de sus clases concretas.
"""

import copy


class Shape:
    """Prototipo base con capacidad de clonación."""

    def __init__(self, x: int = 0, y: int = 0, color: str = "negro") -> None:
        self.x = x
        self.y = y
        self.color = color

    def clone(self) -> "Shape":
        """Crea una copia profunda del objeto."""
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, color={self.color})"


class Circle(Shape):
    """Prototipo concreto: círculo."""

    def __init__(self, x: int = 0, y: int = 0, color: str = "negro", radius: int = 10) -> None:
        super().__init__(x, y, color)
        self.radius = radius

    def __str__(self) -> str:
        return f"Circle(x={self.x}, y={self.y}, color={self.color}, radius={self.radius})"


class Rectangle(Shape):
    """Prototipo concreto: rectángulo."""

    def __init__(self, x: int = 0, y: int = 0, color: str = "negro", width: int = 20, height: int = 10) -> None:
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(x={self.x}, y={self.y}, color={self.color}, w={self.width}, h={self.height})"


if __name__ == "__main__":
    # Crear prototipos originales
    circle = Circle(x=5, y=10, color="rojo", radius=25)
    rectangle = Rectangle(x=0, y=0, color="azul", width=100, height=50)

    # Clonar y modificar
    circle_clone = circle.clone()
    circle_clone.color = "verde"
    circle_clone.x = 50

    rect_clone = rectangle.clone()
    rect_clone.width = 200

    print("--- Originales ---")
    print(f"  {circle}")
    print(f"  {rectangle}")

    print("\n--- Clones modificados ---")
    print(f"  {circle_clone}")
    print(f"  {rect_clone}")

    print(f"\n--- Verificación: son objetos distintos ---")
    print(f"  circle is circle_clone: {circle is circle_clone}")
    print(f"  rectangle is rect_clone: {rectangle is rect_clone}")
