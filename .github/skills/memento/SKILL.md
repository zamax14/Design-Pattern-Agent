---
name: memento
description: 'Implementar el patrón Memento en Python. Usar cuando necesitas guardar y restaurar estados anteriores de un objeto sin violar su encapsulación, implementar undo/redo, o crear snapshots del estado para recuperación.'
argument-hint: 'Describe el objeto cuyo estado necesitas guardar y restaurar'
---

# Memento — Patrón de Comportamiento

Permite guardar y restaurar el estado anterior de un objeto sin revelar los detalles de su implementación. El originador crea snapshots (mementos) de su estado que un cuidador almacena sin acceder a su contenido.

## Cuándo Usar
- Necesitas producir snapshots del estado de un objeto para poder restaurarlo después
- El acceso directo a campos/getters/setters del objeto violaría su encapsulación
- Necesitas implementar undo/redo
- Quieres crear puntos de restauración o checkpoints

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica el objeto cuyo estado necesitas capturar (Originator)
- Verifica que el estado puede serializarse como snapshot
- Si el objeto es simple sin recursos externos, Prototype puede ser más simple
- Se combina naturalmente con Command para undo/redo

### 2. Implementar el Patrón en Python
1. Crea la clase **Originator** con métodos `save()` -> Memento y `restore(memento)`
2. Define la interfaz **Memento** (ABC) con metadata: `get_name()`, `get_date()`
3. Crea **ConcreteMemento** que almacena el estado internamente (inmutable)
4. Solo el Originator accede al estado del Memento via `get_state()`
5. Crea el **Caretaker** que mantiene una pila de mementos (`backup()`, `undo()`)
6. El Caretaker no accede al estado — solo almacena y retorna mementos

### 3. Guía Educativa
- Explica los tres roles: Originator (crea snapshots), Memento (almacena), Caretaker (gestiona)
- Muestra cómo se preserva la encapsulación del originador
- Señala ventajas: snapshots sin violar encapsulación, simplifica código del originador
- Señala desventajas: consumo de RAM si se crean muchos mementos, no garantiza inmutabilidad en Python

## Estructura

```
Originator                      # Crea y restaura snapshots de su estado
│  _state: str
│  save() -> Memento
│  restore(memento)

Memento (ABC)                   # Interfaz: metadata sin exponer estado
│  get_name() -> str
│  get_date() -> str
└── ConcreteMemento             # Almacena estado inmutable
    _state: str
    get_state() -> str          # Solo accesible por Originator

Caretaker                       # Gestiona historial de mementos
│  _mementos: list[Memento]
│  backup()
│  undo()
│  show_history()
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod
from datetime import datetime

class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[:9]}...)"

    def get_date(self) -> str:
        return self._date

class Originator:
    def __init__(self, state: str) -> None:
        self._state = state

    def do_something(self) -> None:
        print(f"Originator: Cambiando estado")
        self._state = "nuevo_estado"

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: Estado restaurado a: {self._state}")

class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos: list[Memento] = []
        self._originator = originator

    def backup(self) -> None:
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not self._mementos:
            return
        memento = self._mementos.pop()
        self._originator.restore(memento)

# Uso
originator = Originator("estado_inicial")
caretaker = Caretaker(originator)

caretaker.backup()              # Guardar estado
originator.do_something()       # Cambiar estado
caretaker.backup()              # Guardar nuevo estado
caretaker.undo()                # Restaurar al anterior
```

## Relaciones con Otros Patrones
- Se combina con **Command** para undo/redo: Command ejecuta, Memento guarda estado previo
- Se combina con **Iterator** para capturar y reanudar estado de iteración
- **Prototype** puede ser alternativa más simple para objetos sencillos sin recursos externos
