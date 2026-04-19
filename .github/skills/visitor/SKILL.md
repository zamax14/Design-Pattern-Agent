---
name: visitor
description: 'Implementar el patrón Visitor en Python. Usar cuando necesitas ejecutar operaciones sobre todos los elementos de una estructura compleja de objetos, separar algoritmos de los objetos sobre los que operan, o añadir operaciones sin modificar las clases existentes.'
argument-hint: 'Describe la estructura de objetos y la operación que quieres ejecutar sobre ellos'
---

# Visitor — Patrón de Comportamiento

Permite separar algoritmos de los objetos sobre los que operan. Define operaciones en clases visitor separadas que pueden ejecutarse sobre elementos de diferentes clases sin modificarlas. Usa double dispatch: el elemento acepta al visitor y lo redirige al método correcto.

## Cuándo Usar
- Necesitas ejecutar una operación sobre todos los elementos de una estructura compleja (ej: árbol de objetos)
- Quieres limpiar la lógica de negocio de comportamientos auxiliares
- Un comportamiento solo tiene sentido en algunas clases de una jerarquía, no en todas
- Quieres añadir nuevas operaciones a una jerarquía sin modificar las clases existentes

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica la jerarquía de elementos sobre los que necesitas operar
- Verifica que la jerarquía de elementos es estable (añadir nuevos elementos fuerza cambios en todos los visitors)
- Si la estructura es un árbol, combina con Composite y/o Iterator
- Si los elementos cambian frecuentemente, el patrón generará mucho mantenimiento

### 2. Implementar el Patrón en Python
1. Define la interfaz **Visitor** (ABC) con un método `visit_*` por cada clase de elemento concreto
2. Crea **ConcreteVisitors** que implementen todos los métodos `visit_*`
3. Define la interfaz **Element** (ABC) con `accept(visitor: Visitor)`
4. Cada **ConcreteElement** implementa `accept()` llamando a `visitor.visit_concrete_element_x(self)`
5. Esto es double dispatch: el elemento conoce su tipo y redirige al método correcto del visitor
6. Los visitors pueden acumular estado mientras recorren la estructura

### 3. Guía Educativa
- Explica double dispatch: `element.accept(visitor)` → `visitor.visit_X(element)`
- Muestra cómo añadir nuevas operaciones creando nuevos visitors sin tocar los elementos
- Señala ventajas: Open/Closed para operaciones, SRP, acumular información al recorrer
- Señala desventajas: actualizar todos los visitors al añadir/quitar elementos, posible falta de acceso a campos privados

## Estructura

```
Visitor (ABC)                   # Un método visit por tipo de elemento
│  visit_concrete_component_a(element)
│  visit_concrete_component_b(element)
├── ConcreteVisitor1            # Implementa operación 1
└── ConcreteVisitor2            # Implementa operación 2

Element (ABC)                   # accept(visitor)
├── ConcreteComponentA          # accept → visitor.visit_concrete_component_a(self)
│   exclusive_method_a() -> str
└── ConcreteComponentB          # accept → visitor.visit_concrete_component_b(self)
    special_method_b() -> str
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_component_a(self, element: "ComponentA") -> None:
        pass

    @abstractmethod
    def visit_component_b(self, element: "ComponentB") -> None:
        pass

class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class ComponentA(Component):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_component_a(self)

    def exclusive_method_a(self) -> str:
        return "A"

class ComponentB(Component):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_component_b(self)

    def special_method_b(self) -> str:
        return "B"

class ConcreteVisitor1(Visitor):
    def visit_component_a(self, element: ComponentA) -> None:
        print(f"{element.exclusive_method_a()} + Visitor1")

    def visit_component_b(self, element: ComponentB) -> None:
        print(f"{element.special_method_b()} + Visitor1")

class ConcreteVisitor2(Visitor):
    def visit_component_a(self, element: ComponentA) -> None:
        print(f"{element.exclusive_method_a()} + Visitor2")

    def visit_component_b(self, element: ComponentB) -> None:
        print(f"{element.special_method_b()} + Visitor2")

# Uso
components = [ComponentA(), ComponentB()]

visitor1 = ConcreteVisitor1()
for component in components:
    component.accept(visitor1)

visitor2 = ConcreteVisitor2()
for component in components:
    component.accept(visitor2)
```

## Relaciones con Otros Patrones
- Es como una versión potente de **Command**: puede ejecutar operaciones sobre objetos de distintas clases
- Se usa para ejecutar operaciones sobre árboles **Composite**
- Se combina con **Iterator** para recorrer estructuras complejas
