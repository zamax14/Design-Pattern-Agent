---
name: mediator
description: 'Implementar el patrón Mediator en Python. Usar cuando necesitas reducir dependencias caóticas entre objetos, centralizar la comunicación entre componentes, desacoplar componentes para reutilizarlos, o evitar subclases solo para reusar comportamiento.'
argument-hint: 'Describe los componentes que necesitan comunicarse y sus interacciones'
---

# Mediator — Patrón de Comportamiento

Reduce dependencias caóticas entre objetos restringiendo las comunicaciones directas y forzándolos a colaborar solo a través de un objeto mediador. Los componentes no se conocen entre sí — solo conocen al mediador.

## Cuándo Usar
- Es difícil cambiar clases porque están fuertemente acopladas entre sí
- No puedes reutilizar un componente porque depende demasiado de otros
- Te encuentras creando muchas subclases solo para reusar comportamiento en distintos contextos
- Quieres centralizar la lógica de comunicación entre componentes

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica los componentes con dependencias cruzadas
- Verifica que la comunicación es lo suficientemente compleja como para justificar el mediador
- Si solo necesitas simplificar una interfaz, usa Facade (unidireccional)
- Cuidado: el mediador puede convertirse en un God Object

### 2. Implementar el Patrón en Python
1. Define la interfaz **Mediator** (ABC o clase base) con método `notify(sender, event)`
2. Crea **BaseComponent** con referencia al mediator (property getter/setter)
3. Los componentes no se comunican directamente — llaman a `self.mediator.notify(self, event)`
4. Crea **ConcreteMediator** que recibe todos los componentes y reacciona a eventos
5. En `notify()`, el mediator decide qué componentes activar según sender + event
6. Los componentes desconocen la existencia de otros componentes

### 3. Guía Educativa
- Explica cómo el mediador centraliza la comunicación (estrella vs. malla)
- Muestra la diferencia con Facade: el mediador es bidireccional, los componentes lo conocen
- Señala ventajas: SRP, Open/Closed, menor acoplamiento, reutilización
- Señala desventajas: puede evolucionar a God Object

## Estructura

```
Mediator (ABC)                  # notify(sender, event)
└── ConcreteMediator            # Reacciona a eventos, coordina componentes
    _component1: Component1
    _component2: Component2

BaseComponent                   # Referencia al mediator
│  mediator: Mediator
├── Component1                  # Notifica eventos, no conoce a Component2
│   do_a() → mediator.notify(self, "A")
└── Component2
    do_c() → mediator.notify(self, "C")
```

## Ejemplo de Referencia en Python

```python
from abc import ABC

class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass

class BaseComponent:
    def __init__(self, mediator: Mediator | None = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component1 hace A")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component1 hace B")

class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component2 hace C")

    def do_d(self) -> None:
        print("Component2 hace D")
        self.mediator.notify(self, "D")

class ConcreteMediator(Mediator):
    def __init__(self, c1: Component1, c2: Component2) -> None:
        self._c1 = c1
        self._c1.mediator = self
        self._c2 = c2
        self._c2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacciona a A y activa C")
            self._c2.do_c()
        elif event == "D":
            print("Mediator reacciona a D y activa B + C")
            self._c1.do_b()
            self._c2.do_c()

# Uso
c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)
c1.do_a()  # Activa c2.do_c() a través del mediator
```

## Relaciones con Otros Patrones
- **Chain of Responsibility**, **Command** y **Observer** también conectan emisores/receptores
- **Facade** simplifica sin añadir funcionalidad; **Mediator** centraliza comunicación bidireccional
- La diferencia con **Observer** es sutil: a menudo se puede implementar Mediator usando Observer
