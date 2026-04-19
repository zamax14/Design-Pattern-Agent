"""
Bridge — Ejemplo

Divide una clase monolítica en dos jerarquías separadas
(abstracción e implementación) que pueden evolucionar independientemente.
"""

from abc import ABC, abstractmethod


# --- Implementación ---

class Device(ABC):
    """Interfaz de implementación."""

    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, volume: int) -> None:
        pass


class TV(Device):
    """Implementación concreta: televisor."""

    def __init__(self) -> None:
        self._on = False
        self._volume = 30

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        self._on = True

    def disable(self) -> None:
        self._on = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume: int) -> None:
        self._volume = max(0, min(100, volume))


class Radio(Device):
    """Implementación concreta: radio."""

    def __init__(self) -> None:
        self._on = False
        self._volume = 50

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        self._on = True

    def disable(self) -> None:
        self._on = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume: int) -> None:
        self._volume = max(0, min(100, volume))


# --- Abstracción ---

class RemoteControl:
    """Abstracción: control remoto básico."""

    def __init__(self, device: Device) -> None:
        self._device = device

    def toggle_power(self) -> None:
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_up(self) -> None:
        self._device.set_volume(self._device.get_volume() + 10)

    def volume_down(self) -> None:
        self._device.set_volume(self._device.get_volume() - 10)

    def status(self) -> str:
        state = "ON" if self._device.is_enabled() else "OFF"
        return f"{self._device.__class__.__name__}: {state}, vol={self._device.get_volume()}"


class AdvancedRemote(RemoteControl):
    """Abstracción refinada: control con mute."""

    def mute(self) -> None:
        self._device.set_volume(0)


if __name__ == "__main__":
    print("--- Remote + TV ---")
    tv = TV()
    remote = RemoteControl(tv)
    remote.toggle_power()
    remote.volume_up()
    print(f"  {remote.status()}")

    print("\n--- Advanced Remote + Radio ---")
    radio = Radio()
    advanced = AdvancedRemote(radio)
    advanced.toggle_power()
    advanced.volume_up()
    print(f"  {advanced.status()}")
    advanced.mute()
    print(f"  Después de mute: {advanced.status()}")
