"""
Builder — Ejemplo

Construye objetos complejos paso a paso, permitiendo distintas
representaciones del mismo proceso de construcción.
"""

from abc import ABC, abstractmethod


class House:
    """Producto complejo."""

    def __init__(self) -> None:
        self.walls: str = ""
        self.roof: str = ""
        self.garage: bool = False
        self.pool: bool = False

    def __str__(self) -> str:
        parts = [f"Paredes: {self.walls}", f"Techo: {self.roof}"]
        if self.garage:
            parts.append("Con garaje")
        if self.pool:
            parts.append("Con piscina")
        return " | ".join(parts)


class HouseBuilder(ABC):
    """Builder abstracto."""

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def build_walls(self) -> None:
        pass

    @abstractmethod
    def build_roof(self) -> None:
        pass

    @abstractmethod
    def build_garage(self) -> None:
        pass

    @abstractmethod
    def build_pool(self) -> None:
        pass


class ConcreteHouseBuilder(HouseBuilder):
    """Builder concreto que construye House."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._house = House()

    def build_walls(self) -> None:
        self._house.walls = "Ladrillo"

    def build_roof(self) -> None:
        self._house.roof = "Teja"

    def build_garage(self) -> None:
        self._house.garage = True

    def build_pool(self) -> None:
        self._house.pool = True

    @property
    def result(self) -> House:
        house = self._house
        self.reset()
        return house


class Director:
    """Director que orquesta los pasos de construcción."""

    def __init__(self, builder: HouseBuilder) -> None:
        self._builder = builder

    def build_minimal_house(self) -> None:
        """Construye casa mínima."""
        self._builder.build_walls()
        self._builder.build_roof()

    def build_full_house(self) -> None:
        """Construye casa completa con todas las opciones."""
        self._builder.build_walls()
        self._builder.build_roof()
        self._builder.build_garage()
        self._builder.build_pool()


if __name__ == "__main__":
    builder = ConcreteHouseBuilder()
    director = Director(builder)

    print("--- Casa mínima ---")
    director.build_minimal_house()
    print(builder.result)

    print("\n--- Casa completa ---")
    director.build_full_house()
    print(builder.result)

    print("\n--- Casa personalizada (sin director) ---")
    builder.build_walls()
    builder.build_roof()
    builder.build_pool()
    print(builder.result)
