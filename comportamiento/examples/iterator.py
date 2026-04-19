"""
Iterator — Ejemplo

Recorre elementos de una colección sin exponer su representación interna.
Implementa el protocolo de iteración de Python (__iter__, __next__).
"""

from collections.abc import Iterator, Iterable


class AlphabeticalOrderIterator(Iterator):
    """Iterador concreto: recorre colección en orden alfabético."""

    def __init__(self, collection: list[str], reverse: bool = False) -> None:
        self._collection = sorted(collection, reverse=reverse)
        self._position = 0

    def __next__(self) -> str:
        if self._position >= len(self._collection):
            raise StopIteration
        value = self._collection[self._position]
        self._position += 1
        return value


class WordsCollection(Iterable):
    """Colección concreta que expone iteradores."""

    def __init__(self) -> None:
        self._items: list[str] = []

    def add_item(self, item: str) -> None:
        self._items.append(item)

    def __iter__(self) -> AlphabeticalOrderIterator:
        """Iterador en orden alfabético normal."""
        return AlphabeticalOrderIterator(self._items)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        """Iterador en orden alfabético inverso."""
        return AlphabeticalOrderIterator(self._items, reverse=True)

    def __len__(self) -> int:
        return len(self._items)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("Python")
    collection.add_item("Java")
    collection.add_item("TypeScript")
    collection.add_item("Go")
    collection.add_item("Rust")

    print("--- Iteración normal (A-Z) ---")
    for item in collection:
        print(f"  {item}")

    print("\n--- Iteración inversa (Z-A) ---")
    for item in collection.get_reverse_iterator():
        print(f"  {item}")
