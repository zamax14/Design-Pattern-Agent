---
name: bridge
description: 'Implementar el patrón Bridge en Python. Usar cuando necesitas dividir una clase monolítica en jerarquías de abstracción e implementación independientes, extender en múltiples dimensiones ortogonales, o cambiar implementaciones en tiempo de ejecución.'
argument-hint: 'Describe la clase o funcionalidad que quieres separar en abstracción e implementación'
---

# Bridge — Patrón Estructural

Permite dividir una clase grande o un grupo de clases estrechamente relacionadas en dos jerarquías separadas — abstracción e implementación — que pueden desarrollarse independientemente. La abstracción delega el trabajo a un objeto de implementación.

## Cuándo Usar
- Tienes una clase monolítica con muchas variantes de una sola funcionalidad
- Necesitas extender una clase en varias dimensiones ortogonales (independientes)
- Necesitas cambiar implementaciones en tiempo de ejecución
- Quieres evitar una explosión combinatoria de subclases (N abstracciones × M implementaciones)

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica las dos dimensiones independientes (ej: forma + color, GUI + API, dispositivo + plataforma)
- Verifica que hay una explosión combinatoria de subclases si usas herencia simple
- Si solo necesitas hacer compatible una interfaz existente, usa Adapter
- Si quieres simplificar un subsistema, usa Facade

### 2. Implementar el Patrón en Python
1. Define la interfaz **Implementation** (ABC) con métodos primitivos de bajo nivel
2. Crea **ConcreteImplementationA**, **ConcreteImplementationB** por plataforma/variante
3. Define la clase **Abstraction** que mantiene referencia a Implementation y delega
4. Crea **RefinedAbstraction** con variantes de lógica de alto nivel
5. El cliente enlaza la abstracción con la implementación concreta en la inicialización
6. Añade type hints completos

### 3. Guía Educativa
- Explica la separación entre lógica de alto nivel (abstracción) y trabajo de bajo nivel (implementación)
- Muestra cómo añadir nuevas abstracciones o implementaciones independientemente
- Señala ventajas: independencia de plataforma, Open/Closed, SRP
- Señala desventajas: complejidad si se aplica a una clase muy cohesiva

## Estructura

```
Implementation (ABC)            # Interfaz de bajo nivel
├── ConcreteImplA               # Implementación plataforma A
└── ConcreteImplB               # Implementación plataforma B

Abstraction                     # Lógica de alto nivel, delega a Implementation
│  implementation: Implementation
├── RefinedAbstraction          # Variante de lógica de alto nivel
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "Resultado en plataforma A"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "Resultado en plataforma B"

class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return f"Abstraction: {self.implementation.operation_implementation()}"

class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return f"Extended: {self.implementation.operation_implementation()}"

# Código cliente — enlaza abstracción con implementación
impl_a = ConcreteImplementationA()
abstraction = Abstraction(impl_a)
print(abstraction.operation())

impl_b = ConcreteImplementationB()
extended = ExtendedAbstraction(impl_b)
print(extended.operation())
```

## Relaciones con Otros Patrones
- Se diseña **por adelantado** (a diferencia de **Adapter** que se usa con código existente)
- **State**, **Strategy** y **Adapter** tienen estructuras similares pero resuelven problemas diferentes
- Se combina con **Abstract Factory** cuando abstracciones requieren implementaciones específicas
- Se combina con **Builder**: Director = abstracción, Builders = implementaciones
