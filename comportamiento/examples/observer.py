"""
Observer — Ejemplo

Mecanismo de suscripción para notificar a múltiples objetos
sobre eventos que ocurren en el objeto observado.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """Interfaz del suscriptor."""

    @abstractmethod
    def update(self, event: str, data: str) -> None:
        pass


class EventManager:
    """Publisher: gestiona suscripciones y notificaciones."""

    def __init__(self) -> None:
        self._listeners: dict[str, list[Observer]] = {}

    def subscribe(self, event_type: str, listener: Observer) -> None:
        """Suscribe un observer a un tipo de evento."""
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener)

    def unsubscribe(self, event_type: str, listener: Observer) -> None:
        """Cancela suscripción."""
        if event_type in self._listeners:
            self._listeners[event_type].remove(listener)

    def notify(self, event_type: str, data: str) -> None:
        """Notifica a todos los listeners del evento."""
        for listener in self._listeners.get(event_type, []):
            listener.update(event_type, data)


class Store:
    """Subject concreto: tienda que emite eventos."""

    def __init__(self) -> None:
        self.events = EventManager()
        self._inventory: dict[str, int] = {}

    def add_product(self, product: str, quantity: int) -> None:
        self._inventory[product] = self._inventory.get(product, 0) + quantity
        self.events.notify("product_added", f"{product} (qty: {quantity})")

    def sell_product(self, product: str) -> None:
        if product in self._inventory and self._inventory[product] > 0:
            self._inventory[product] -= 1
            self.events.notify("product_sold", product)
            if self._inventory[product] == 0:
                self.events.notify("out_of_stock", product)


class EmailNotifier(Observer):
    """Observer concreto: envía notificaciones por email."""

    def __init__(self, email: str) -> None:
        self._email = email

    def update(self, event: str, data: str) -> None:
        print(f"  [Email -> {self._email}] {event}: {data}")


class InventoryLogger(Observer):
    """Observer concreto: registra cambios de inventario."""

    def update(self, event: str, data: str) -> None:
        print(f"  [InventoryLog] {event}: {data}")


if __name__ == "__main__":
    print("--- Observer: Store Events ---\n")

    store = Store()

    # Crear observers
    customer = EmailNotifier("cliente@mail.com")
    admin = EmailNotifier("admin@tienda.com")
    logger = InventoryLogger()

    # Suscribir
    store.events.subscribe("product_added", logger)
    store.events.subscribe("product_sold", logger)
    store.events.subscribe("out_of_stock", admin)
    store.events.subscribe("out_of_stock", customer)

    # Acciones
    print("Agregando productos:")
    store.add_product("Laptop", 2)
    store.add_product("Mouse", 1)

    print("\nVendiendo productos:")
    store.sell_product("Laptop")
    store.sell_product("Mouse")  # Dispara out_of_stock
