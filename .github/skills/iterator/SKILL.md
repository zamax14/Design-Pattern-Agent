---
name: iterator
description: 'Implementar el patrón Iterator en Python. Usar cuando necesitas recorrer elementos de una colección sin exponer su representación interna, soportar múltiples formas de recorrido, o unificar la interfaz de iteración sobre diferentes estructuras de datos.'
argument-hint: 'Describe la colección o estructura de datos que necesitas recorrer'
---

# Iterator — Patrón de Comportamiento

Permite recorrer elementos de una colección sin exponer su representación interna (lista, pila, árbol, etc.). En Python se implementa nativamente con los protocolos `__iter__()` y `__next__()` del módulo `collections.abc`.

## Cuándo Usar
- Tu colección tiene una estructura interna compleja pero quieres ocultar esa complejidad
- Quieres reducir duplicación de código de recorrido en tu aplicación
- Necesitas recorrer diferentes estructuras de datos con la misma interfaz
- Necesitas soportar múltiples formas de recorrido (directo, inverso, filtrado, etc.)
- Quieres recorridos paralelos o pausables (cada iterador mantiene su propio estado)

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica si tu colección necesita formas de recorrido no triviales
- Verifica si las colecciones nativas de Python ya cubren tu caso (`list`, `dict`, generators)
- Si la colección es simple, un iterador explícito puede ser excesivo
- Para iteraciones complejas, los generators de Python pueden ser más idiomáticos

### 2. Implementar el Patrón en Python
1. Crea la clase **Collection** que implemente `collections.abc.Iterable` con `__iter__()`
2. Crea la clase **ConcreteIterator** que implemente `collections.abc.Iterator` con `__next__()`
3. El iterator mantiene `_position` y otros campos de estado del recorrido
4. `__next__()` retorna el siguiente elemento o lanza `StopIteration`
5. La collection retorna nuevas instancias del iterator en `__iter__()`
6. Para recorrido inverso, crea un método separado que retorne otro tipo de iterator
7. Alternativa pythónica: usa `yield` en `__iter__()` para crear un generator iterator

### 3. Guía Educativa
- Explica los protocolos `Iterable` y `Iterator` de Python
- Muestra la diferencia entre iterador explícito y generator con `yield`
- Señala ventajas: SRP, Open/Closed, iteración paralela, iteración lazy
- Señala desventajas: excesivo para colecciones simples, puede ser menos eficiente

## Estructura

```
Iterable (ABC)                  # __iter__() -> Iterator
├── WordsCollection             # Colección concreta
│   __iter__() -> AlphabeticalOrderIterator
│   get_reverse_iterator()

Iterator (ABC)                  # __next__() -> Any
├── AlphabeticalOrderIterator   # Recorrido concreto
│   _collection, _position
│   __next__() -> Any           # Retorna siguiente o StopIteration
```

## Ejemplo de Referencia en Python

```python
from collections.abc import Iterable, Iterator
from typing import Any

class AlphabeticalOrderIterator(Iterator):
    def __init__(self, collection: "WordsCollection", reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = 0
        self._sorted = None

    def __next__(self) -> Any:
        if self._sorted is None:
            self._sorted = sorted(self._collection._items)
            if self._reverse:
                self._sorted = list(reversed(self._sorted))
        if self._position >= len(self._sorted):
            raise StopIteration()
        value = self._sorted[self._position]
        self._position += 1
        return value

class WordsCollection(Iterable):
    def __init__(self, collection: list[Any] | None = None) -> None:
        self._items = collection or []

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, reverse=True)

    def add_item(self, item: Any) -> None:
        self._items.append(item)

# Uso
collection = WordsCollection()
collection.add_item("C")
collection.add_item("A")
collection.add_item("B")

print("Directo:", list(collection))       # ['A', 'B', 'C']
print("Inverso:", list(collection.get_reverse_iterator()))  # ['C', 'B', 'A']
```

## Relaciones con Otros Patrones
- Se usa para recorrer árboles **Composite**
- **Factory Method** permite que subclases de colección retornen iteradores compatibles
- Se combina con **Memento** para capturar y reanudar estado de iteración
- Se combina con **Visitor** para ejecutar operaciones sobre elementos de una estructura compleja
