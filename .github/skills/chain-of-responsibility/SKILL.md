---
name: chain-of-responsibility
description: 'Implementar el patrón Chain of Responsibility en Python. Usar cuando necesitas procesar solicitudes por una cadena de manejadores, cada uno decide si procesarla o pasarla al siguiente, desacoplar emisor del receptor, o manejar diferentes tipos de requests dinámicamente.'
argument-hint: 'Describe los tipos de solicitudes y manejadores que necesitas encadenar'
---

# Chain of Responsibility — Patrón de Comportamiento

Permite pasar solicitudes a lo largo de una cadena de manejadores. Al recibir una solicitud, cada manejador decide si procesarla o pasarla al siguiente manejador de la cadena. Los manejadores se enlazan dinámicamente.

## Cuándo Usar
- Tu programa debe procesar diferentes tipos de solicitudes pero no conoces los tipos ni su orden de antemano
- Necesitas ejecutar varios manejadores en un orden específico
- El grupo de manejadores y su orden debe poder cambiar en tiempo de ejecución
- Quieres desacoplar el emisor de la solicitud de sus receptores

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica los diferentes tipos de solicitudes y sus manejadores
- Verifica que cada manejador puede decidir independientemente si procesar o pasar
- Si todos los manejadores deben procesar la solicitud, usa Decorator u Observer
- Si necesitas mediación centralizada, usa Mediator

### 2. Implementar el Patrón en Python
1. Define la interfaz **Handler** (ABC) con `set_next(handler)` y `handle(request)`
2. Crea **AbstractHandler** base que implementa `set_next()` retornando el handler (encadenamiento fluido)
3. En `handle()` del AbstractHandler, delega al siguiente handler si existe
4. Crea **ConcreteHandlers** que sobreescriben `handle()`: procesan si aplica, o llaman a `super().handle()`
5. `set_next()` debe retornar el handler para permitir: `h1.set_next(h2).set_next(h3)`
6. El cliente puede enviar solicitudes a cualquier handler de la cadena

### 3. Guía Educativa
- Explica cómo cada handler decide independientemente si procesar o delegar
- Muestra cómo construir cadenas dinámicas en tiempo de ejecución
- Señala ventajas: control de orden, SRP, Open/Closed
- Señala desventajas: algunas solicitudes pueden quedar sin manejar

## Estructura

```
Handler (ABC)                   # Interfaz con set_next() y handle()
│
├── AbstractHandler             # Implementa encadenamiento base
│   _next_handler: Handler
│   set_next(handler) -> Handler
│   handle(request) -> Optional[str]
│
├── ConcreteHandlerA            # Procesa si aplica, sino delega
├── ConcreteHandlerB
└── ConcreteHandlerC
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod
from typing import Optional, Any

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        pass

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Banana":
            return f"Mono: Yo como la {request}"
        return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Hueso":
            return f"Perro: Yo como el {request}"
        return super().handle(request)

# Construir cadena dinámicamente
monkey = MonkeyHandler()
dog = DogHandler()
monkey.set_next(dog)

# Enviar solicitudes
for food in ["Banana", "Hueso", "Café"]:
    result = monkey.handle(food)
    print(result or f"{food} quedó sin manejar")
```

## Relaciones con Otros Patrones
- **Command**, **Mediator** y **Observer** también conectan emisores con receptores
- Se usa frecuentemente con **Composite** (propagar request por el árbol de padres)
- Los handlers pueden implementarse como **Commands**
- **Decorator** tiene estructura similar pero los decoradores no pueden detener la cadena
