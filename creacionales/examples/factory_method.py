"""
Factory Method — Ejemplo

Define una interfaz para crear objetos, pero permite que las subclases
decidan qué clase instanciar.
"""

from abc import ABC, abstractmethod


class Transport(ABC):
    """Producto abstracto."""

    @abstractmethod
    def deliver(self) -> str:
        pass


class Truck(Transport):
    """Producto concreto: transporte terrestre."""

    def deliver(self) -> str:
        return "Entrega por tierra en camión"


class Ship(Transport):
    """Producto concreto: transporte marítimo."""

    def deliver(self) -> str:
        return "Entrega por mar en barco"


class Logistics(ABC):
    """Creador abstracto con Factory Method."""

    @abstractmethod
    def create_transport(self) -> Transport:
        """Factory Method — subclases deciden qué Transport instanciar."""
        pass

    def plan_delivery(self) -> str:
        """Lógica de negocio que usa el producto creado por el factory method."""
        transport = self.create_transport()
        return f"Logística planificada: {transport.deliver()}"


class RoadLogistics(Logistics):
    """Creador concreto: logística terrestre."""

    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    """Creador concreto: logística marítima."""

    def create_transport(self) -> Transport:
        return Ship()


if __name__ == "__main__":
    print("--- Road Logistics ---")
    road = RoadLogistics()
    print(road.plan_delivery())

    print("\n--- Sea Logistics ---")
    sea = SeaLogistics()
    print(sea.plan_delivery())
