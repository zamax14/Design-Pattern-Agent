---
name: command
description: 'Implementar el patrón Command en Python. Usar cuando necesitas convertir solicitudes en objetos independientes, implementar undo/redo, encolar o diferir ejecución de operaciones, o desacoplar invocador del receptor.'
argument-hint: 'Describe la operación que quieres encapsular como objeto command'
---

# Command — Patrón de Comportamiento

Convierte una solicitud en un objeto independiente que contiene toda la información sobre la solicitud. Permite parametrizar métodos con diferentes requests, diferir o encolar la ejecución, y soportar operaciones reversibles (undo/redo).

## Cuándo Usar
- Quieres parametrizar objetos con operaciones
- Necesitas encolar operaciones, programar su ejecución, o ejecutarlas remotamente
- Quieres implementar operaciones reversibles (undo/redo)
- Necesitas ensamblar comandos simples en comandos complejos (macros)
- Quieres desacoplar el objeto que invoca la operación del que la ejecuta

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica las operaciones que necesitas encapsular
- Verifica si necesitas undo/redo, encolamiento, o ejecución diferida
- Si solo necesitas intercambiar algoritmos, usa Strategy
- Si necesitas parametrizar con variantes del mismo comportamiento, Strategy es más simple

### 2. Implementar el Patrón en Python
1. Define la interfaz **Command** (ABC) con método `execute()`
2. Crea **SimpleCommand** para operaciones autocontenidas
3. Crea **ComplexCommand** que recibe un **Receiver** y le delega el trabajo real
4. El ComplexCommand almacena los parámetros necesarios como campos
5. Crea el **Invoker** que almacena y ejecuta commands sin conocer su tipo concreto
6. El **Receiver** contiene la lógica de negocio real
7. Para undo: añade método `undo()` que revierte `execute()`

### 3. Guía Educativa
- Explica la separación Invoker → Command → Receiver
- Muestra cómo los commands encapsulan toda la información necesaria
- Señala ventajas: SRP, Open/Closed, undo/redo, ejecución diferida, composición
- Señala desventajas: nueva capa de complejidad entre emisor y receptor

## Estructura

```
Command (ABC)                   # Interfaz con execute()
├── SimpleCommand               # Operación autocontenida
│   _payload: str
└── ComplexCommand              # Delega a Receiver
    _receiver: Receiver
    _params: ...

Receiver                        # Lógica de negocio real
│  do_something(a)
│  do_something_else(b)

Invoker                         # Almacena y ejecuta Commands
│  _on_start: Command
│  _on_finish: Command
│  do_something_important()
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: {self._payload}")

class Receiver:
    def do_something(self, a: str) -> None:
        print(f"Receiver: Trabajando en ({a})")

    def do_something_else(self, b: str) -> None:
        print(f"Receiver: También en ({b})")

class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Invoker:
    _on_start: Command | None = None
    _on_finish: Command | None = None

    def set_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        self._on_finish = command

    def do_something_important(self) -> None:
        if self._on_start:
            self._on_start.execute()
        print("Invoker: ...haciendo algo importante...")
        if self._on_finish:
            self._on_finish.execute()

# Uso
invoker = Invoker()
invoker.set_on_start(SimpleCommand("Hola"))
invoker.set_on_finish(ComplexCommand(Receiver(), "enviar email", "guardar log"))
invoker.do_something_important()
```

## Relaciones con Otros Patrones
- **Chain of Responsibility**, **Mediator** y **Observer** conectan emisores/receptores diferente
- Los handlers de **Chain of Responsibility** pueden implementarse como Commands
- Se combina con **Memento** para undo: Memento guarda estado antes de ejecutar Command
- **Strategy** describe formas de hacer lo mismo; **Command** convierte cualquier operación en objeto
- **Prototype** ayuda a guardar copias de Commands en un historial
- **Visitor** es como una versión potente de Command
