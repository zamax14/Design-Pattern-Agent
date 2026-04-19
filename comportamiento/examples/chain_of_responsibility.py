"""
Chain of Responsibility — Ejemplo

Pasa solicitudes a lo largo de una cadena de manejadores. Cada uno decide
si procesa la solicitud o la pasa al siguiente.
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    """Interfaz del manejador con encadenamiento."""

    def __init__(self) -> None:
        self._next_handler: "Handler | None" = None

    def set_next(self, handler: "Handler") -> "Handler":
        """Encadena el siguiente manejador. Retorna el handler para encadenar."""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> str | None:
        pass


class SpamFilter(Handler):
    """Manejador: filtra spam."""

    def handle(self, request: str) -> str | None:
        if "spam" in request.lower():
            return f"SpamFilter: bloqueado '{request}'"
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class AuthFilter(Handler):
    """Manejador: verifica autenticación."""

    VALID_USERS = ["admin", "user1"]

    def handle(self, request: str) -> str | None:
        user = request.split(":")[0] if ":" in request else ""
        if user not in self.VALID_USERS:
            return f"AuthFilter: usuario '{user}' no autorizado"
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class LoggingFilter(Handler):
    """Manejador: registra y deja pasar."""

    def handle(self, request: str) -> str | None:
        result = f"LoggingFilter: registrado '{request}'"
        if self._next_handler:
            next_result = self._next_handler.handle(request)
            return f"{result} -> {next_result}"
        return result


class FinalHandler(Handler):
    """Manejador final: procesa la solicitud."""

    def handle(self, request: str) -> str | None:
        return f"FinalHandler: solicitud procesada OK"


if __name__ == "__main__":
    # Construir cadena: Spam -> Auth -> Logging -> Final
    spam = SpamFilter()
    auth = AuthFilter()
    logging_h = LoggingFilter()
    final = FinalHandler()

    spam.set_next(auth).set_next(logging_h).set_next(final)

    print("--- Chain of Responsibility ---\n")

    requests = [
        "admin: obtener datos",
        "spam promoción gratis!!!",
        "hacker: acceder sistema",
        "user1: guardar archivo",
    ]

    for req in requests:
        result = spam.handle(req)
        print(f"  '{req}'\n    -> {result}\n")
