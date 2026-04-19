# Facade

**Tipo:** Estructural
**También conocido como:** Fachada

## Propósito

Facade es un patrón de diseño estructural que proporciona una interfaz simplificada a una biblioteca, un framework o cualquier otro grupo complejo de clases.

## Problema

Imagina que debes lograr que tu código trabaje con un amplio grupo de objetos que pertenecen a una sofisticada biblioteca o framework. Normalmente, debes inicializar todos esos objetos, llevar un registro de las dependencias, ejecutar los métodos en el orden correcto y así sucesivamente.

Como resultado, la lógica de negocio de tus clases se vería estrechamente acoplada a los detalles de implementación de las clases de terceros, haciéndola difícil de comprender y mantener.

## Solución

Una fachada es una clase que proporciona una interfaz simple a un subsistema complejo que contiene muchas partes móviles. Una fachada puede proporcionar una funcionalidad limitada en comparación con trabajar directamente con el subsistema. Sin embargo, tan solo incluye las funciones realmente importantes para los clientes.

Tener una fachada resulta útil cuando tienes que integrar tu aplicación con una biblioteca sofisticada con decenas de funciones, de la cual sólo necesitas una pequeña parte.

## Estructura

1. **Facade**: proporciona un práctico acceso a una parte específica de la funcionalidad del subsistema. Sabe a dónde dirigir la petición del cliente y cómo operar todas las partes móviles.
2. **Fachada Adicional**: puede crearse para evitar contaminar una única fachada con funciones no relacionadas que podrían convertirla en otra estructura compleja.
3. **Subsistema Complejo**: consiste en decenas de objetos diversos. Las clases del subsistema no conocen la existencia de la fachada.
4. **Cliente**: utiliza la fachada en lugar de invocar directamente los objetos del subsistema.

## Aplicabilidad

- Utiliza el patrón Facade cuando necesites una interfaz limitada pero directa a un subsistema complejo.
- Utiliza el patrón Facade cuando quieras estructurar un subsistema en capas.

## Pros y Contras

### Pros
- Puedes aislar tu código de la complejidad de un subsistema.

### Contras
- Una fachada puede convertirse en un objeto todopoderoso acoplado a todas las clases de una aplicación.

## Relaciones con otros patrones

- Facade define una nueva interfaz para objetos existentes, mientras que Adapter intenta hacer que la interfaz existente sea utilizable. Normalmente Adapter sólo envuelve un objeto, mientras que Facade trabaja con todo un subsistema.
- Abstract Factory puede servir como alternativa a Facade cuando tan solo deseas esconder la forma en que se crean los objetos del subsistema.
- Flyweight muestra cómo crear muchos pequeños objetos, mientras que Facade muestra cómo crear un único objeto que represente un subsistema completo.
- Facade y Mediator tienen trabajos similares: ambos intentan organizar la colaboración entre muchas clases estrechamente acopladas.
- Una clase fachada a menudo puede transformarse en una Singleton, ya que un único objeto fachada es suficiente en la mayoría de los casos.
- Facade es similar a Proxy en el sentido de que ambos pueden almacenar temporalmente una entidad compleja e inicializarla por su cuenta.

## Ejemplo en Python

```python
from __future__ import annotations


class Facade:
    """
    The Facade class provides a simple interface to the complex logic of one or
    several subsystems. The Facade delegates the client requests to the
    appropriate objects within the subsystem. The Facade is also responsible for
    managing their lifecycle. All of this shields the client from the undesired
    complexity of the subsystem.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        Depending on your application's needs, you can provide the Facade with
        existing subsystem objects or force the Facade to create them on its
        own.
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        The Facade's methods are convenient shortcuts to the sophisticated
        functionality of the subsystems. However, clients get only to a fraction
        of a subsystem's capabilities.
        """

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    """
    The Subsystem can accept requests either from the facade or client directly.
    In any case, to the Subsystem, the Facade is yet another client, and it's
    not a part of the Subsystem.
    """

    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    # ...

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    """
    Some facades can work with multiple subsystems at the same time.
    """

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def client_code(facade: Facade) -> None:
    """
    The client code works with complex subsystems through a simple interface
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
```

### Output

```
Facade initializes subsystems:
Subsystem1: Ready!
Subsystem2: Get ready!
Facade orders subsystems to perform the action:
Subsystem1: Go!
Subsystem2: Fire!
```

## Referencias

- [Refactoring Guru - Facade](https://refactoring.guru/es/design-patterns/facade)
- [Ejemplo en Python](https://refactoring.guru/es/design-patterns/facade/python/example)
