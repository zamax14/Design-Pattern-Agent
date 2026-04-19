"""
Memento — Ejemplo

Guarda y restaura estados anteriores de un objeto sin violar
su encapsulación. Implementa undo con snapshots.
"""

from datetime import datetime


class Memento:
    """Almacena snapshot del estado del Originator."""

    def __init__(self, state: str) -> None:
        self._state = state
        self._date = datetime.now().strftime("%H:%M:%S")

    def get_state(self) -> str:
        return self._state

    def get_date(self) -> str:
        return self._date

    def __str__(self) -> str:
        return f"Memento({self._date}: '{self._state[:20]}...')"


class Editor:
    """Originator: editor cuyo estado puede guardarse y restaurarse."""

    def __init__(self) -> None:
        self._content = ""

    @property
    def content(self) -> str:
        return self._content

    def type_text(self, text: str) -> None:
        """Escribe texto en el editor."""
        self._content += text
        print(f"  Editor: escribió '{text}' -> contenido: '{self._content}'")

    def save(self) -> Memento:
        """Crea memento del estado actual."""
        return Memento(self._content)

    def restore(self, memento: Memento) -> None:
        """Restaura estado desde memento."""
        self._content = memento.get_state()
        print(f"  Editor: restaurado a '{self._content}'")


class History:
    """Caretaker: gestiona la pila de mementos."""

    def __init__(self, editor: Editor) -> None:
        self._editor = editor
        self._mementos: list[Memento] = []

    def backup(self) -> None:
        """Guarda el estado actual."""
        memento = self._editor.save()
        self._mementos.append(memento)
        print(f"  History: guardado {memento}")

    def undo(self) -> None:
        """Restaura el último estado guardado."""
        if not self._mementos:
            print("  History: nada que deshacer")
            return
        memento = self._mementos.pop()
        self._editor.restore(memento)

    def show_history(self) -> None:
        """Muestra los mementos guardados."""
        print(f"  History: {len(self._mementos)} snapshots")
        for m in self._mementos:
            print(f"    - {m}")


if __name__ == "__main__":
    print("--- Memento: Editor con Undo ---\n")

    editor = Editor()
    history = History(editor)

    editor.type_text("Hola")
    history.backup()

    editor.type_text(" mundo")
    history.backup()

    editor.type_text(" cruel")
    print(f"\n  Estado actual: '{editor.content}'")

    print("\n--- Historial ---")
    history.show_history()

    print("\n--- Undo ---")
    history.undo()

    print("\n--- Undo ---")
    history.undo()

    print(f"\n  Estado final: '{editor.content}'")
