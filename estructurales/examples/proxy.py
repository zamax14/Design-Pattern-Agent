"""
Proxy — Ejemplo

Controla el acceso a un objeto mediante un sustituto que intercepta
las operaciones. Implementa lazy loading y caching.
"""

from abc import ABC, abstractmethod


class Subject(ABC):
    """Interfaz común para RealSubject y Proxy."""

    @abstractmethod
    def request(self) -> str:
        pass


class RealSubject(Subject):
    """Objeto real que hace el trabajo pesado."""

    def __init__(self) -> None:
        # Simula inicialización costosa
        self._data = "datos cargados de la base de datos"
        print("  [RealSubject] Inicialización costosa completada")

    def request(self) -> str:
        return f"RealSubject: {self._data}"


class CachingProxy(Subject):
    """Proxy con lazy loading y caching."""

    def __init__(self) -> None:
        self._real_subject: RealSubject | None = None
        self._cache: str | None = None
        self._access_count = 0

    def request(self) -> str:
        if self._cache is not None:
            self._access_count += 1
            return f"Proxy (cache hit #{self._access_count}): {self._cache}"

        # Lazy loading
        if self._real_subject is None:
            print("  [Proxy] Lazy loading del RealSubject...")
            self._real_subject = RealSubject()

        result = self._real_subject.request()
        self._cache = result
        self._access_count += 1
        return f"Proxy (acceso #{self._access_count}): {result}"

    def clear_cache(self) -> None:
        """Limpia el cache para forzar recarga."""
        self._cache = None


if __name__ == "__main__":
    print("--- Proxy con lazy loading y caching ---\n")

    proxy = CachingProxy()
    print("Proxy creado. RealSubject NO inicializado aún.\n")

    # Primera llamada: lazy loading + guarda en cache
    print(f"  {proxy.request()}")

    # Segunda llamada: usa cache
    print(f"\n  {proxy.request()}")

    # Tercera llamada: usa cache
    print(f"  {proxy.request()}")

    # Limpiar cache y acceder de nuevo
    print("\n  [Cliente] Limpiando cache...")
    proxy.clear_cache()
    print(f"  {proxy.request()}")
