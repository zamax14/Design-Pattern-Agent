"""
Composite — Ejemplo

Compone objetos en estructuras de árbol para representar jerarquías
parte-todo. Los clientes tratan objetos individuales y compuestos uniformemente.
"""

from abc import ABC, abstractmethod


class Component(ABC):
    """Interfaz común para hojas y composites."""

    @property
    def parent(self) -> "Component | None":
        return self._parent

    @parent.setter
    def parent(self, parent: "Component | None") -> None:
        self._parent = parent

    def add(self, component: "Component") -> None:
        pass

    def remove(self, component: "Component") -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Leaf(Component):
    """Hoja: elemento sin hijos."""

    def __init__(self, name: str) -> None:
        self._parent = None
        self._name = name

    def operation(self) -> str:
        return self._name


class Composite(Component):
    """Composite: contiene hijos (hojas u otros composites)."""

    def __init__(self, name: str) -> None:
        self._parent = None
        self._name = name
        self._children: list[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = [child.operation() for child in self._children]
        return f"{self._name}({'+'.join(results)})"


if __name__ == "__main__":
    # Árbol de estructura organizacional
    print("--- Estructura de árbol ---")

    leaf1 = Leaf("Dev1")
    leaf2 = Leaf("Dev2")
    leaf3 = Leaf("Designer1")
    leaf4 = Leaf("Manager1")

    dev_team = Composite("DevTeam")
    dev_team.add(leaf1)
    dev_team.add(leaf2)

    design_team = Composite("DesignTeam")
    design_team.add(leaf3)

    company = Composite("Company")
    company.add(dev_team)
    company.add(design_team)
    company.add(leaf4)

    print(f"  Hoja simple: {leaf1.operation()}")
    print(f"  Subárbol: {dev_team.operation()}")
    print(f"  Árbol completo: {company.operation()}")
