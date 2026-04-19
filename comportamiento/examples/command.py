"""
Command — Ejemplo

Convierte solicitudes en objetos independientes que contienen toda
la información sobre la operación. Soporta undo y cola de operaciones.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    """Interfaz Command."""

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class Editor:
    """Receptor: editor de texto."""

    def __init__(self) -> None:
        self.text = ""

    def insert(self, text: str) -> None:
        self.text += text

    def delete(self, count: int) -> str:
        deleted = self.text[-count:]
        self.text = self.text[:-count]
        return deleted

    def __str__(self) -> str:
        return f"Editor: '{self.text}'"


class InsertCommand(Command):
    """Comando concreto: insertar texto."""

    def __init__(self, editor: Editor, text: str) -> None:
        self._editor = editor
        self._text = text

    def execute(self) -> None:
        self._editor.insert(self._text)

    def undo(self) -> None:
        self._editor.delete(len(self._text))


class DeleteCommand(Command):
    """Comando concreto: borrar caracteres."""

    def __init__(self, editor: Editor, count: int) -> None:
        self._editor = editor
        self._count = count
        self._deleted = ""

    def execute(self) -> None:
        self._deleted = self._editor.delete(self._count)

    def undo(self) -> None:
        self._editor.insert(self._deleted)


class CommandHistory:
    """Invocador: ejecuta comandos y mantiene historial para undo."""

    def __init__(self) -> None:
        self._history: list[Command] = []

    def execute(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo(self) -> None:
        if self._history:
            command = self._history.pop()
            command.undo()


if __name__ == "__main__":
    editor = Editor()
    history = CommandHistory()

    print("--- Command con Undo ---\n")

    history.execute(InsertCommand(editor, "Hola"))
    print(f"  Después de insertar 'Hola': {editor}")

    history.execute(InsertCommand(editor, " Mundo"))
    print(f"  Después de insertar ' Mundo': {editor}")

    history.execute(DeleteCommand(editor, 5))
    print(f"  Después de borrar 5 chars: {editor}")

    print("\n  --- Undo ---")
    history.undo()
    print(f"  Undo delete: {editor}")

    history.undo()
    print(f"  Undo insert: {editor}")

    history.undo()
    print(f"  Undo insert: {editor}")
