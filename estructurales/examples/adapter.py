"""
Adapter — Ejemplo

Permite que clases con interfaces incompatibles colaboren entre sí
mediante un objeto intermediario que traduce la interfaz.
"""


class Target:
    """Interfaz que el cliente espera."""

    def request(self) -> str:
        return "Target: comportamiento por defecto"


class Adaptee:
    """Clase existente con interfaz incompatible."""

    def specific_request(self) -> str:
        return ".eetpadA led laicepse otneimaipmoc"


class Adapter(Target):
    """Adapta la interfaz de Adaptee a la interfaz Target."""

    def __init__(self, adaptee: Adaptee) -> None:
        self._adaptee = adaptee

    def request(self) -> str:
        """Traduce la llamada al formato compatible."""
        result = self._adaptee.specific_request()[::-1]
        return f"Adapter: (TRADUCIDO) {result}"


if __name__ == "__main__":
    print("--- Cliente con Target directo ---")
    target = Target()
    print(f"  {target.request()}")

    print("\n--- Adaptee (interfaz incompatible) ---")
    adaptee = Adaptee()
    print(f"  {adaptee.specific_request()}")

    print("\n--- Cliente con Adapter ---")
    adapter = Adapter(adaptee)
    print(f"  {adapter.request()}")
