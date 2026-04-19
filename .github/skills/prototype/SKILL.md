---
name: prototype
description: 'Implementar el patrón Prototype en Python. Usar cuando necesitas copiar/clonar objetos existentes sin depender de sus clases concretas, evitar código de inicialización repetido, o crear objetos complejos a partir de prototipos prefabricados.'
argument-hint: 'Describe el objeto que necesitas clonar o el problema de copia'
---

# Prototype — Patrón Creacional

Permite copiar objetos existentes sin que el código dependa de sus clases. Delega el proceso de clonación a los propios objetos mediante una interfaz común (`clone`). En Python se implementa con `copy.copy()` y `copy.deepcopy()`.

## Cuándo Usar
- Tu código no debe depender de las clases concretas de los objetos que necesitas copiar
- Quieres reducir subclases que solo difieren en su inicialización
- Necesitas clonar objetos complejos con muchos campos y configuraciones
- Quieres evitar código de inicialización repetido usando prototipos prefabricados
- Necesitas una alternativa a herencia para preajustes de configuración

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica si hay objetos que necesitan ser copiados frecuentemente
- Verifica si la copia manual campo por campo es problemática (campos privados, objetos anidados)
- Evalúa si hay referencias circulares que compliquen la clonación
- Si el problema es crear variantes, considera Factory Method o Builder

### 2. Implementar el Patrón en Python
1. En Python, usa el módulo `copy` — no necesitas una interfaz Prototype explícita
2. Implementa `__copy__()` para copia superficial (shallow copy)
3. Implementa `__deepcopy__(memo)` para copia profunda (deep copy)
4. En `__deepcopy__`, usa el parámetro `memo` para evitar recursión infinita con referencias circulares
5. Crea copias de objetos anidados antes de construir el clon
6. Añade type hints completos

### 3. Guía Educativa
- Explica la diferencia entre shallow copy y deep copy
- Muestra cómo `memo` previene recursión infinita con referencias circulares
- Señala ventajas: independencia de clases concretas, evita inicialización repetida
- Señala desventajas: clonar objetos con referencias circulares es complejo

## Estructura

```
Prototype (implícito en Python)
│  __copy__() -> Self
│  __deepcopy__(memo) -> Self
├── ConcretePrototypeA          # Implementa clonación personalizada
└── ConcretePrototypeB          # Otra implementación de clonación

# En Python: copy.copy(obj) → shallow, copy.deepcopy(obj) → deep
```

## Ejemplo de Referencia en Python

```python
import copy

class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

class SomeComponent:
    def __init__(self, some_int: int, some_list: list, some_ref: SelfReferencingEntity):
        self.some_int = some_int
        self.some_list = some_list
        self.some_ref = some_ref

    def __copy__(self):
        some_list = copy.copy(self.some_list)
        some_ref = copy.copy(self.some_ref)
        new = self.__class__(self.some_int, some_list, some_ref)
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        some_list = copy.deepcopy(self.some_list, memo)
        some_ref = copy.deepcopy(self.some_ref, memo)
        new = self.__class__(self.some_int, some_list, some_ref)
        new.__dict__.update(self.__dict__)
        return new

# Uso
original = SomeComponent(42, [1, 2, 3], SelfReferencingEntity())
shallow = copy.copy(original)      # Copia superficial
deep = copy.deepcopy(original)     # Copia profunda independiente
```

## Relaciones con Otros Patrones
- Evoluciona desde **Factory Method** como alternativa sin herencia
- **Abstract Factory** puede usar Prototype para implementar sus métodos de creación
- Útil para guardar copias de **Commands** en un historial
- **Composite** y **Decorator** se benefician de Prototype
- Alternativa más simple a **Memento** para objetos sencillos sin recursos externos
- Puede implementarse como **Singleton**
