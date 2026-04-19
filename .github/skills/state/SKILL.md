---
name: state
description: 'Implementar el patrón State en Python. Usar cuando necesitas que un objeto cambie su comportamiento según su estado interno, reemplazar condicionales masivos de máquina de estados, o organizar código específico de cada estado en clases separadas.'
argument-hint: 'Describe el objeto y los estados que modifican su comportamiento'
---

# State — Patrón de Comportamiento

Permite que un objeto altere su comportamiento cuando su estado interno cambia, como si el objeto cambiara de clase. Cada estado se encapsula en una clase independiente y el contexto delega el comportamiento al objeto de estado actual.

## Cuándo Usar
- Un objeto se comporta diferente según su estado actual y el número de estados es grande
- Tienes condicionales masivos (`if/elif/else`, `match`) que alteran el comportamiento según estado
- Hay mucho código duplicado entre estados y transiciones similares
- Necesitas que las transiciones de estado sean explícitas y manejables

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica los estados distintos del objeto y los comportamientos asociados
- Mapea las transiciones entre estados (qué eventos causan qué cambios)
- Si la máquina de estados tiene pocos estados y rara vez cambia, el patrón es excesivo
- Si necesitas intercambiar algoritmos sin transiciones entre ellos, usa Strategy

### 2. Implementar el Patrón en Python
1. Crea la clase **Context** con referencia a un State y método `transition_to(state)`
2. Define la interfaz **State** (ABC) con los métodos de comportamiento + backreference al Context
3. Crea **ConcreteStateA**, **ConcreteStateB** con implementaciones específicas
4. Los estados concretos pueden invocar `self.context.transition_to(OtroEstado())` para transicionar
5. El Context delega llamadas al State actual: `self._state.handle()`
6. Añade type hints completos

### 3. Guía Educativa
- Explica cómo cada estado encapsula su comportamiento y transiciones
- Muestra la diferencia con Strategy: State permite transiciones entre estados; Strategy no
- Señala ventajas: SRP (código por estado en clases separadas), Open/Closed, elimina condicionales
- Señala desventajas: excesivo si hay pocos estados o cambios infrecuentes

## Estructura

```
Context                         # Mantiene referencia al estado actual
│  _state: State
│  transition_to(state: State)
│  request1()                   # Delega a _state.handle1()
│  request2()                   # Delega a _state.handle2()

State (ABC)                     # Interfaz + backreference a Context
│  context: Context
│  handle1()
│  handle2()
├── ConcreteStateA              # Comportamiento del estado A
│   handle1() → puede transicionar a StateB
└── ConcreteStateB              # Comportamiento del estado B
    handle2() → puede transicionar a StateA
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class State(ABC):
    @property
    def context(self) -> "Context":
        return self._context

    @context.setter
    def context(self, context: "Context") -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

class Context:
    _state: State = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State) -> None:
        print(f"Context: Transición a {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self) -> None:
        self._state.handle1()

    def request2(self) -> None:
        self._state.handle2()

class ConcreteStateA(State):
    def handle1(self) -> None:
        print("StateA maneja request1")
        print("StateA quiere cambiar a StateB")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("StateA maneja request2")

class ConcreteStateB(State):
    def handle1(self) -> None:
        print("StateB maneja request1")

    def handle2(self) -> None:
        print("StateB maneja request2")
        self.context.transition_to(ConcreteStateA())

# Uso
context = Context(ConcreteStateA())
context.request1()  # StateA → transiciona a StateB
context.request2()  # StateB → transiciona a StateA
```

## Relaciones con Otros Patrones
- **Bridge**, **Strategy** y **Adapter** tienen estructura similar pero resuelven problemas diferentes
- **State** es una extensión de **Strategy**: ambos usan composición, pero State permite transiciones entre estados mientras Strategy hace objetos independientes
- **Template Method** usa herencia; **State** usa composición (más dinámico)
