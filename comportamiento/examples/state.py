"""
State — Ejemplo

Permite que un objeto altere su comportamiento cuando su estado interno
cambia. Cada estado se encapsula en una clase separada.
"""

from abc import ABC, abstractmethod


class State(ABC):
    """Interfaz del estado con backreference al contexto."""

    @property
    def player(self) -> "AudioPlayer":
        return self._player

    @player.setter
    def player(self, player: "AudioPlayer") -> None:
        self._player = player

    @abstractmethod
    def press_play(self) -> None:
        pass

    @abstractmethod
    def press_stop(self) -> None:
        pass

    @abstractmethod
    def press_next(self) -> None:
        pass


class AudioPlayer:
    """Context: reproductor de audio cuyo comportamiento depende del estado."""

    def __init__(self) -> None:
        self._state: State | None = None
        self.current_track = "Track 1"
        self.transition_to(StoppedState())

    def transition_to(self, state: State) -> None:
        print(f"  [Player] Transición a {type(state).__name__}")
        self._state = state
        self._state.player = self

    def press_play(self) -> None:
        self._state.press_play()

    def press_stop(self) -> None:
        self._state.press_stop()

    def press_next(self) -> None:
        self._state.press_next()


class StoppedState(State):
    """Estado: detenido."""

    def press_play(self) -> None:
        print(f"  Reproduciendo '{self.player.current_track}'")
        self.player.transition_to(PlayingState())

    def press_stop(self) -> None:
        print("  Ya está detenido")

    def press_next(self) -> None:
        print("  Siguiente track (sin reproducir)")
        self.player.current_track = "Track 2"


class PlayingState(State):
    """Estado: reproduciendo."""

    def press_play(self) -> None:
        print("  Pausando...")
        self.player.transition_to(PausedState())

    def press_stop(self) -> None:
        print("  Deteniendo reproducción")
        self.player.transition_to(StoppedState())

    def press_next(self) -> None:
        self.player.current_track = "Track 2"
        print(f"  Siguiente: '{self.player.current_track}'")


class PausedState(State):
    """Estado: pausado."""

    def press_play(self) -> None:
        print(f"  Reanudando '{self.player.current_track}'")
        self.player.transition_to(PlayingState())

    def press_stop(self) -> None:
        print("  Deteniendo desde pausa")
        self.player.transition_to(StoppedState())

    def press_next(self) -> None:
        print("  No se puede avanzar en pausa")


if __name__ == "__main__":
    print("--- State: Audio Player ---\n")

    player = AudioPlayer()

    print("\n> play")
    player.press_play()

    print("\n> next")
    player.press_next()

    print("\n> play (pausa)")
    player.press_play()

    print("\n> play (reanudar)")
    player.press_play()

    print("\n> stop")
    player.press_stop()
