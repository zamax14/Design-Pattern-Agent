---
name: observer
description: 'Implementar el patrón Observer en Python. Usar cuando necesitas un mecanismo de suscripción para notificar a múltiples objetos sobre eventos, implementar pub/sub, reaccionar a cambios de estado, o establecer relaciones dinámicas entre objetos.'
argument-hint: 'Describe el evento o cambio de estado al que otros objetos deben reaccionar'
---

# Observer — Patrón de Comportamiento

Define un mecanismo de suscripción para notificar a múltiples objetos sobre cualquier evento que le suceda al objeto observado. Los suscriptores se registran y desregistran dinámicamente.

## Cuándo Usar
- Cambios en el estado de un objeto deben reflejarse en otros objetos desconocidos de antemano
- Algunos objetos deben observar a otros, pero solo temporalmente o en casos específicos
- Necesitas comunicación uno-a-muchos con lista dinámica de receptores
- Quieres implementar un sistema de eventos/pub-sub

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica el objeto emisor de eventos (Subject/Notifier) y los receptores (Observers)
- Verifica que la lista de observadores debe ser dinámica (suscribirse/desuscribirse)
- Si necesitas comunicación bidireccional centralizada, usa Mediator
- Si solo necesitas un receptor, el patrón es excesivo — usa callback directo

### 2. Implementar el Patrón en Python
1. Define la interfaz **Subject** (ABC) con `attach(observer)`, `detach(observer)`, `notify()`
2. Crea **ConcreteSubject** con la lista de observers y el estado que emite eventos
3. Define la interfaz **Observer** (ABC) con `update(subject)`
4. Crea **ConcreteObservers** que reaccionan en `update()` según el estado del subject
5. `notify()` itera la lista de observers y llama a `update()` en cada uno
6. Pasa el subject como argumento de `update()` para que observers puedan obtener contexto

### 3. Guía Educativa
- Explica el modelo de suscripción dinámica (attach/detach en runtime)
- Muestra cómo los observers son independientes entre sí
- Señala ventajas: Open/Closed (nuevos observers sin cambiar subject), relaciones en runtime
- Señala desventajas: orden de notificación no garantizado

## Estructura

```
Subject (ABC)                   # Gestiona suscripciones
│  attach(observer)
│  detach(observer)
│  notify()
└── ConcreteSubject             # Emite eventos cuando cambia estado
    _state: int
    _observers: list[Observer]
    some_business_logic()       # Cambia estado → notify()

Observer (ABC)                  # update(subject)
├── ConcreteObserverA           # Reacciona según condición
└── ConcreteObserverB           # Reacciona según otra condición
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, subject: "Subject") -> None:
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class ConcreteSubject(Subject):
    _state: int = 0
    _observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        self._state = 42
        print(f"Subject: estado cambió a {self._state}")
        self.notify()

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 50:
            print("ObserverA: Reaccionó al evento")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state >= 10:
            print("ObserverB: Reaccionó al evento")

# Uso
subject = ConcreteSubject()
observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)
subject.some_business_logic()   # Notifica a ambos

subject.detach(observer_a)
subject.some_business_logic()   # Solo notifica a B
```

## Relaciones con Otros Patrones
- **Chain of Responsibility**, **Command** y **Mediator** también conectan emisores/receptores
- La diferencia con **Mediator** es sutil: Mediator elimina dependencias mutuas; Observer establece conexiones unidireccionales dinámicas
- Se puede implementar **Mediator** usando Observer: el mediador actúa como notifier
