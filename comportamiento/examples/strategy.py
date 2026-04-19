"""
Strategy — Ejemplo

Define una familia de algoritmos intercambiables. El contexto delega
el trabajo al objeto strategy actual, que puede cambiarse en runtime.
"""

from abc import ABC, abstractmethod


class SortStrategy(ABC):
    """Interfaz de estrategia de ordenamiento."""

    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class BubbleSort(SortStrategy):
    """Estrategia: ordenamiento burbuja (listas pequeñas)."""

    def sort(self, data: list[int]) -> list[int]:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def name(self) -> str:
        return "BubbleSort"


class QuickSort(SortStrategy):
    """Estrategia: quicksort (listas grandes)."""

    def sort(self, data: list[int]) -> list[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

    def name(self) -> str:
        return "QuickSort"


class ReverseSort(SortStrategy):
    """Estrategia: ordenamiento inverso."""

    def sort(self, data: list[int]) -> list[int]:
        return sorted(data, reverse=True)

    def name(self) -> str:
        return "ReverseSort"


class Sorter:
    """Context: usa una estrategia de ordenamiento intercambiable."""

    def __init__(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> SortStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def sort(self, data: list[int]) -> list[int]:
        """Delega al strategy actual."""
        print(f"  Sorter usando: {self._strategy.name()}")
        return self._strategy.sort(data)


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"--- Strategy: Sorting ---\n")
    print(f"  Datos originales: {data}\n")

    sorter = Sorter(BubbleSort())
    print(f"  Resultado: {sorter.sort(data)}\n")

    # Cambiar estrategia en runtime
    sorter.strategy = QuickSort()
    print(f"  Resultado: {sorter.sort(data)}\n")

    sorter.strategy = ReverseSort()
    print(f"  Resultado: {sorter.sort(data)}")
