"""
Flyweight — Ejemplo

Optimiza consumo de memoria compartiendo estado común (intrínseco)
entre múltiples objetos, separándolo del estado único (extrínseco).
"""

import json


class TreeType:
    """Flyweight: estado intrínseco compartido entre árboles."""

    def __init__(self, name: str, color: str, texture: str) -> None:
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x: int, y: int) -> str:
        """Dibuja con estado extrínseco (posición) recibido como parámetro."""
        return f"  Árbol '{self.name}' [{self.color}, {self.texture}] en ({x}, {y})"


class TreeFactory:
    """Fábrica de Flyweights: gestiona y reutiliza instancias."""

    _tree_types: dict[str, TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        """Retorna flyweight existente o crea uno nuevo."""
        key = f"{name}_{color}_{texture}"
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
            print(f"  [Factory] Nuevo TreeType creado: {key}")
        return cls._tree_types[key]

    @classmethod
    def total_types(cls) -> int:
        return len(cls._tree_types)


class Tree:
    """Contexto: combina flyweight (tipo) con estado extrínseco (posición)."""

    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self) -> str:
        return self.tree_type.draw(self.x, self.y)


class Forest:
    """Colección de árboles que usa Flyweight para optimizar memoria."""

    def __init__(self) -> None:
        self._trees: list[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        self._trees.append(Tree(x, y, tree_type))

    def draw(self) -> None:
        for tree in self._trees:
            print(tree.draw())


if __name__ == "__main__":
    print("--- Plantando bosque (Flyweight) ---\n")
    forest = Forest()

    # Plantar muchos árboles — solo se crean 3 TreeTypes
    forest.plant_tree(1, 2, "Pino", "verde", "rugosa")
    forest.plant_tree(5, 3, "Pino", "verde", "rugosa")
    forest.plant_tree(8, 1, "Roble", "café", "lisa")
    forest.plant_tree(3, 7, "Roble", "café", "lisa")
    forest.plant_tree(9, 9, "Abedul", "blanco", "papel")
    forest.plant_tree(2, 4, "Pino", "verde", "rugosa")

    print(f"\n--- Dibujando bosque ({len(forest._trees)} árboles, {TreeFactory.total_types()} tipos) ---")
    forest.draw()
