---
name: composite
description: 'Implementar el patrón Composite en Python. Usar cuando necesitas representar jerarquías parte-todo como estructuras de árbol, tratar objetos individuales y compuestos de forma uniforme, o construir árboles recursivos.'
argument-hint: 'Describe la estructura de árbol o jerarquía que necesitas modelar'
---

# Composite — Patrón Estructural

Permite componer objetos en estructuras de árbol y trabajar con ellas como si fueran objetos individuales. Los clientes tratan hojas y contenedores de forma uniforme a través de una interfaz común.

## Cuándo Usar
- Necesitas implementar una estructura de objetos en forma de árbol
- Quieres que el código cliente trate elementos simples y compuestos de la misma manera
- Tienes una jerarquía parte-todo (archivos/carpetas, widgets UI, organización, etc.)
- Necesitas aplicar operaciones recursivas sobre una estructura

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica si el modelo del dominio puede representarse como árbol (contenedores + hojas)
- Verifica que hojas y contenedores comparten operaciones comunes
- Si los elementos no tienen relación jerárquica, el patrón no aplica
- Si necesitas recorrer el árbol sistemáticamente, combina con Iterator

### 2. Implementar el Patrón en Python
1. Define la interfaz **Component** (ABC) con `operation()` y opcionalmente `add()`, `remove()`, `is_composite()`
2. Crea la clase **Leaf** que implementa `operation()` con comportamiento real
3. Crea la clase **Composite** que almacena hijos en una lista y delega `operation()` recursivamente
4. El Composite propaga `operation()` a todos sus hijos y agrega los resultados
5. Opcionalmente, mantén referencia al padre con propiedad `parent`
6. Añade type hints completos

### 3. Guía Educativa
- Explica la diferencia entre Leaf (hace el trabajo real) y Composite (delega y agrega)
- Muestra cómo la recursión permite tratar árboles de cualquier profundidad
- Señala ventajas: polimorfismo, recursión, Open/Closed
- Señala desventajas: difícil proveer interfaz común si la funcionalidad varía mucho

## Estructura

```
Component (ABC)                 # Interfaz común para hojas y contenedores
│  operation() -> str
│  add(component)               # Opcional — vacío en Leaf
│  remove(component)            # Opcional — vacío en Leaf
│
├── Leaf                        # Elemento final sin hijos
│   operation() -> str          # Hace el trabajo real
│
└── Composite                   # Contenedor con hijos
    _children: list[Component]
    add(component)              # Agrega hijo
    remove(component)           # Quita hijo
    operation() -> str          # Delega a hijos recursivamente
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

    def add(self, component: "Component") -> None:
        pass

    def remove(self, component: "Component") -> None:
        pass

    def is_composite(self) -> bool:
        return False

class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"

class Composite(Component):
    def __init__(self) -> None:
        self._children: list[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = [child.operation() for child in self._children]
        return f"Branch({'+'.join(results)})"

# Uso
tree = Composite()
branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())
tree.add(branch1)
tree.add(Leaf())
print(tree.operation())  # Branch(Branch(Leaf+Leaf)+Leaf)
```

## Relaciones con Otros Patrones
- **Builder** se usa para crear árboles Composite complejos
- **Chain of Responsibility** se usa frecuentemente junto con Composite
- **Iterator** permite recorrer árboles Composite
- **Visitor** ejecuta operaciones sobre todo el árbol
- Los nodos hoja compartidos pueden implementarse como **Flyweight**
- **Decorator** es como un Composite con un solo hijo
