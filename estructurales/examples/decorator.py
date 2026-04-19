"""
Decorator — Ejemplo

Añade funcionalidades a objetos en tiempo de ejecución mediante
envolturas apilables, sin modificar la clase original.
"""

from abc import ABC, abstractmethod


class DataSource(ABC):
    """Interfaz del componente."""

    @abstractmethod
    def write_data(self, data: str) -> str:
        pass

    @abstractmethod
    def read_data(self) -> str:
        pass


class FileDataSource(DataSource):
    """Componente concreto: lectura/escritura básica."""

    def __init__(self) -> None:
        self._data = ""

    def write_data(self, data: str) -> str:
        self._data = data
        return f"Escrito: {data}"

    def read_data(self) -> str:
        return self._data


class DataSourceDecorator(DataSource):
    """Decorator base: delega al componente envuelto."""

    def __init__(self, source: DataSource) -> None:
        self._wrappee = source

    def write_data(self, data: str) -> str:
        return self._wrappee.write_data(data)

    def read_data(self) -> str:
        return self._wrappee.read_data()


class EncryptionDecorator(DataSourceDecorator):
    """Decorator concreto: añade cifrado."""

    def write_data(self, data: str) -> str:
        encrypted = self._encrypt(data)
        return super().write_data(encrypted)

    def read_data(self) -> str:
        data = super().read_data()
        return self._decrypt(data)

    def _encrypt(self, data: str) -> str:
        # Cifrado simple: rot13
        import codecs
        return codecs.encode(data, "rot13")

    def _decrypt(self, data: str) -> str:
        import codecs
        return codecs.encode(data, "rot13")


class CompressionDecorator(DataSourceDecorator):
    """Decorator concreto: añade compresión simulada."""

    def write_data(self, data: str) -> str:
        compressed = f"[compressed:{len(data)}bytes]{data[:10]}..."
        return super().write_data(compressed)

    def read_data(self) -> str:
        return f"[decompressed]{super().read_data()}"


if __name__ == "__main__":
    print("--- Escritura sin decoradores ---")
    source = FileDataSource()
    print(f"  {source.write_data('Hello World')}")
    print(f"  Lectura: {source.read_data()}")

    print("\n--- Con EncryptionDecorator ---")
    encrypted_source = EncryptionDecorator(FileDataSource())
    print(f"  {encrypted_source.write_data('Secret Data')}")
    print(f"  Lectura (descifrada): {encrypted_source.read_data()}")

    print("\n--- Decoradores apilados: Compression + Encryption ---")
    stacked = CompressionDecorator(EncryptionDecorator(FileDataSource()))
    print(f"  {stacked.write_data('Datos importantes para guardar')}")
    print(f"  Lectura: {stacked.read_data()}")
