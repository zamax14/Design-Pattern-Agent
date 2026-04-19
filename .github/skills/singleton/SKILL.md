---
name: singleton
description: 'Implementar el patrón Singleton en Python. Usar cuando necesitas garantizar una única instancia de una clase, controlar acceso a recursos compartidos como bases de datos, o proveer un punto de acceso global thread-safe.'
argument-hint: 'Describe la clase o recurso que necesita ser singleton'
---

# Singleton — Patrón Creacional

Garantiza que una clase tenga una única instancia y proporciona un punto de acceso global a ella. En Python se implementa típicamente con una metaclase que controla la instanciación.

## Cuándo Usar
- Una clase solo debe tener una instancia disponible para todos los clientes
- Necesitas controlar acceso a un recurso compartido (BD, archivo, configuración)
- Necesitas un control más estricto que las variables globales
- Quieres inicialización lazy (solo cuando se requiere por primera vez)

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica si realmente necesitas una sola instancia (no abuses del patrón)
- Evalúa si el recurso compartido requiere thread-safety
- Considera si el Singleton dificultará las pruebas unitarias
- Si solo necesitas esconder creación de subsistemas, considera Facade

### 2. Implementar el Patrón en Python
1. Crea una **metaclase** `SingletonMeta(type)` con diccionario `_instances`
2. Sobreescribe `__call__` para controlar la instanciación
3. Para thread-safety, usa `threading.Lock` dentro de `__call__`
4. La clase Singleton usa `metaclass=SingletonMeta`
5. Añade type hints completos
6. Considera alternativas pythónicas: módulos como singletons, `__new__`

### 3. Guía Educativa
- Explica los dos problemas que resuelve: instancia única + acceso global
- Muestra la versión naïve vs. thread-safe con `Lock`
- Señala ventajas: instancia única garantizada, acceso global, lazy init
- Señala desventajas: viola SRP, enmascara mal diseño, dificulta testing, threading

## Estructura

```
SingletonMeta (type)            # Metaclase que controla instanciación
│  _instances: dict             # Cache de instancias
│  __call__() -> instance       # Retorna instancia existente o crea nueva
│
Singleton (metaclass=SingletonMeta)
│  some_business_logic()        # Lógica de negocio de la instancia
```

## Ejemplo de Referencia en Python

```python
from threading import Lock

class SingletonMeta(type):
    _instances: dict = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self) -> None:
        pass

# Uso — ambas variables apuntan a la misma instancia
s1 = Singleton("primera")
s2 = Singleton("segunda")
assert id(s1) == id(s2)  # True
print(s1.value)           # "primera" (la segunda llamada no reinicializa)
```

## Relaciones con Otros Patrones
- **Facade** a menudo puede transformarse en Singleton
- **Flyweight** podría asemejarse a Singleton si se reduce a un solo objeto compartido
- **Abstract Factory**, **Builder** y **Prototype** pueden implementarse como Singletons
