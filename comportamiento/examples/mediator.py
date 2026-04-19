"""
Mediator — Ejemplo

Reduce dependencias caóticas entre objetos centralizando la comunicación
en un objeto mediador. Los componentes no se conocen entre sí.
"""

from abc import ABC, abstractmethod


class Mediator(ABC):
    """Interfaz del mediador."""

    @abstractmethod
    def notify(self, sender: "Component", event: str) -> None:
        pass


class Component:
    """Componente base con referencia al mediador."""

    def __init__(self, mediator: Mediator | None = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator | None:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Button(Component):
    """Componente concreto: botón."""

    def click(self) -> None:
        print("  Button: click")
        if self._mediator:
            self._mediator.notify(self, "click")


class TextBox(Component):
    """Componente concreto: campo de texto."""

    def __init__(self, mediator: Mediator | None = None) -> None:
        super().__init__(mediator)
        self.text = ""

    def set_text(self, text: str) -> None:
        self.text = text
        print(f"  TextBox: texto = '{text}'")
        if self._mediator:
            self._mediator.notify(self, "text_changed")


class Checkbox(Component):
    """Componente concreto: checkbox."""

    def __init__(self, mediator: Mediator | None = None) -> None:
        super().__init__(mediator)
        self.checked = False

    def toggle(self) -> None:
        self.checked = not self.checked
        print(f"  Checkbox: {'marcado' if self.checked else 'desmarcado'}")
        if self._mediator:
            self._mediator.notify(self, "toggle")


class Dialog(Mediator):
    """Mediador concreto: coordina componentes de un diálogo."""

    def __init__(self) -> None:
        self.button = Button()
        self.textbox = TextBox()
        self.checkbox = Checkbox()

        self.button.mediator = self
        self.textbox.mediator = self
        self.checkbox.mediator = self

    def notify(self, sender: Component, event: str) -> None:
        """Lógica de coordinación centralizada."""
        if sender == self.textbox and event == "text_changed":
            # Habilitar botón solo si hay texto
            has_text = bool(self.textbox.text)
            print(f"    [Mediator] Botón {'habilitado' if has_text else 'deshabilitado'}")

        elif sender == self.checkbox and event == "toggle":
            if self.checkbox.checked:
                print("    [Mediator] Modo avanzado activado")
            else:
                print("    [Mediator] Modo simple activado")

        elif sender == self.button and event == "click":
            print(f"    [Mediator] Enviando formulario: '{self.textbox.text}'")


if __name__ == "__main__":
    print("--- Mediator: Dialog ---\n")

    dialog = Dialog()

    dialog.textbox.set_text("Hola mundo")
    print()

    dialog.checkbox.toggle()
    print()

    dialog.button.click()
    print()

    dialog.textbox.set_text("")
