"""
Abstract Factory — Ejemplo

Crea familias de objetos relacionados sin especificar sus clases concretas.
"""

from abc import ABC, abstractmethod


# --- Productos abstractos ---

class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


# --- Productos concretos: Windows ---

class WindowsButton(Button):
    def render(self) -> str:
        return "[Windows Button]"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "[Windows Checkbox]"


# --- Productos concretos: Mac ---

class MacButton(Button):
    def render(self) -> str:
        return "[Mac Button]"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "[Mac Checkbox]"


# --- Abstract Factory ---

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# --- Cliente ---

def render_ui(factory: GUIFactory) -> None:
    """Renderiza UI usando la factory proporcionada."""
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(f"  Button: {button.render()}")
    print(f"  Checkbox: {checkbox.render()}")


if __name__ == "__main__":
    print("--- Windows UI ---")
    render_ui(WindowsFactory())

    print("\n--- Mac UI ---")
    render_ui(MacFactory())
