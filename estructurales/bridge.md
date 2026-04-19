# Bridge

**Tipo:** Estructural
**También conocido como:** Puente

## Propósito

Bridge es un patrón de diseño estructural que te permite dividir una clase grande, o un grupo de clases estrechamente relacionadas, en dos jerarquías separadas (abstracción e implementación) que pueden desarrollarse independientemente la una de la otra.

## Problema

Digamos que tienes una clase geométrica `Forma` con un par de subclases: `Círculo` y `Cuadrado`. Deseas extender esta jerarquía de clase para que incorpore colores, por lo que planeas crear las subclases de forma `Rojo` y `Azul`. Sin embargo, como ya tienes dos subclases, tienes que crear cuatro combinaciones de clase, como `CírculoAzul` y `CuadradoRojo`.

El número de combinaciones de clase crece en progresión geométrica. Añadir nuevos tipos de forma y color a la jerarquía hará que ésta crezca exponencialmente.

## Solución

Este problema se presenta porque intentamos extender las clases de forma en dos dimensiones independientes: por forma y por color. El patrón Bridge intenta resolver este problema pasando de la herencia a la composición del objeto.

Esto quiere decir que se extrae una de las dimensiones a una jerarquía de clases separada, de modo que las clases originales referencian un objeto de la nueva jerarquía, en lugar de tener todo su estado y sus funcionalidades dentro de una clase.

Con esta solución, podemos extraer el código relacionado con el color y colocarlo dentro de su propia clase, con dos subclases: `Rojo` y `Azul`. La clase `Forma` obtiene entonces un campo de referencia que apunta a uno de los objetos de color. Esa referencia actuará como un puente entre las clases `Forma` y `Color`.

### Abstracción e Implementación

La **Abstracción** (también llamada interfaz) es una capa de control de alto nivel para una entidad. Esta capa no tiene que hacer ningún trabajo real por su cuenta, sino que debe delegar el trabajo a la capa de **implementación** (también llamada plataforma).

## Estructura

1. **Abstracción**: ofrece lógica de control de alto nivel. Depende de que el objeto de la implementación haga el trabajo de bajo nivel.
2. **Implementación**: declara la interfaz común a todas las implementaciones concretas. Una abstracción sólo se puede comunicar con un objeto de implementación a través de los métodos que se declaren aquí.
3. **Implementaciones Concretas**: contienen código específico de plataforma.
4. **Abstracciones Refinadas**: proporcionan variantes de lógica de control. Como sus padres, trabajan con distintas implementaciones a través de la interfaz general de implementación.
5. **Cliente**: sólo está interesado en trabajar con la abstracción, pero tiene que vincular el objeto de la abstracción con uno de los objetos de la implementación.

## Aplicabilidad

- Utiliza el patrón Bridge cuando quieras dividir y organizar una clase monolítica que tenga muchas variantes de una sola funcionalidad.
- Utiliza el patrón cuando necesites extender una clase en varias dimensiones ortogonales (independientes).
- Utiliza el patrón Bridge cuando necesites poder cambiar implementaciones durante el tiempo de ejecución.

## Pros y Contras

### Pros
- Puedes crear clases y aplicaciones independientes de plataforma.
- El código cliente funciona con abstracciones de alto nivel. No está expuesto a los detalles de la plataforma.
- Principio de abierto/cerrado. Puedes introducir nuevas abstracciones e implementaciones independientes entre sí.
- Principio de responsabilidad única. Puedes centrarte en la lógica de alto nivel en la abstracción y en detalles de la plataforma en la implementación.

### Contras
- Puede ser que el código se complique si aplicas el patrón a una clase muy cohesionada.

## Relaciones con otros patrones

- Bridge suele diseñarse por anticipado, lo que te permite desarrollar partes de una aplicación de forma independiente. Adapter se utiliza habitualmente con una aplicación existente.
- Bridge, State, Strategy (y, hasta cierto punto, Adapter) tienen estructuras muy similares, pero solucionan problemas diferentes.
- Puedes utilizar Abstract Factory junto a Bridge. Este emparejamiento resulta útil cuando algunas abstracciones definidas por Bridge sólo pueden funcionar con implementaciones específicas.
- Puedes combinar Builder con Bridge: la clase directora juega el papel de la abstracción, mientras que diferentes constructoras actúan como implementaciones.

## Ejemplo en Python

```python
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    """
    The Implementation defines the interface for all implementation classes. It
    doesn't have to match the Abstraction's interface. In fact, the two
    interfaces can be entirely different. Typically the Implementation interface
    provides only primitive operations, while the Abstraction defines higher-
    level operations based on those primitives.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Each Concrete Implementation corresponds to a specific platform and implements
the Implementation interface using that platform's API.
"""


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    """
    Except for the initialization phase, where an Abstraction object gets linked
    with a specific Implementation object, the client code should only depend on
    the Abstraction class. This way the client code can support any abstraction-
    implementation combination.
    """

    # ...

    print(abstraction.operation(), end="")

    # ...


if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
```

### Output

```
Abstraction: Base operation with:
ConcreteImplementationA: Here's the result on the platform A.

ExtendedAbstraction: Extended operation with:
ConcreteImplementationB: Here's the result on the platform B.
```

## Referencias

- [Refactoring Guru - Bridge](https://refactoring.guru/es/design-patterns/bridge)
- [Ejemplo en Python](https://refactoring.guru/es/design-patterns/bridge/python/example)
