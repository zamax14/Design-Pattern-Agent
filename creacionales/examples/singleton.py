"""
Singleton — Ejemplo

Garantiza que una clase tenga una única instancia y proporciona
un punto de acceso global a ella. Implementación thread-safe.
"""

from threading import Lock, Thread


class SingletonMeta(type):
    """Metaclase Singleton thread-safe."""

    _instances: dict = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """Ejemplo: conexión a base de datos como Singleton."""

    def __init__(self, connection_string: str = "localhost:5432") -> None:
        self.connection_string = connection_string

    def query(self, sql: str) -> str:
        """Simula una consulta."""
        return f"Ejecutando '{sql}' en {self.connection_string}"


def test_singleton(name: str) -> None:
    """Función para verificar singleton desde distintos hilos."""
    db = Database()
    print(f"  Hilo {name}: id={id(db)}, conn={db.connection_string}")


if __name__ == "__main__":
    print("--- Singleton thread-safe ---")

    db1 = Database("prod-server:5432")
    db2 = Database("otro-server:3306")  # No crea nueva instancia

    print(f"  db1 is db2: {db1 is db2}")
    print(f"  db1.connection_string: {db1.connection_string}")
    print(f"  db2.connection_string: {db2.connection_string}")

    print("\n--- Verificación multihilo ---")
    threads = [Thread(target=test_singleton, args=(f"T{i}",)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
