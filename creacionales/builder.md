# Builder

**Tipo:** Creacional
**También conocido como:** Constructor

## Propósito

Builder es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. El patrón nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.

## Problema

Imagina un objeto complejo que requiere una inicialización laboriosa, paso a paso, de muchos campos y objetos anidados. Normalmente, este código de inicialización está sepultado dentro de un monstruoso constructor con una gran cantidad de parámetros. O, peor aún, disperso por todo el código del cliente.

Por ejemplo, piensa cómo crear un objeto `Casa`. Para construir una casa sencilla, debes construir cuatro paredes y un piso, instalar una puerta, encajar un par de ventanas y edificar un tejado. Pero ¿qué pasa si quieres una casa más grande y luminosa, con un patio y otros extras (como un sistema de calefacción, cableado y fontanería)?

La solución más sencilla es extender la clase base `Casa` y crear un grupo de subclases que cubran todas las combinaciones posibles de los parámetros. Pero, eventualmente, acabarás con un número considerable de subclases. Cualquier nuevo parámetro, como el estilo del porche, exigirá que crezcas aún más esta jerarquía.

## Solución

El patrón Builder sugiere que saques el código de construcción del objeto de su propia clase y lo coloques dentro de objetos independientes llamados constructores.

El patrón organiza la construcción de objetos en una serie de pasos (`construirParedes`, `construirPuerta`, etc.). Para crear un objeto, ejecutas una serie de pasos en un objeto constructor. Lo importante es que no necesitas invocar todos los pasos. Puedes invocar sólo aquellos que sean necesarios para producir una configuración particular de un objeto.

Puedes ir más lejos y extraer una serie de llamadas a los pasos del constructor que utilizas para construir un producto en una clase independiente llamada directora. La clase directora define el orden en el que se deben ejecutar los pasos de construcción, mientras que el constructor proporciona la implementación de esos pasos.

## Estructura

1. **Builder**: declara pasos de construcción de producto que todos los tipos de objetos constructores tienen en común.
2. **Constructores Concretos**: ofrecen distintas implementaciones de los pasos de construcción. Los constructores concretos pueden crear productos que no siguen la interfaz común.
3. **Productos**: son los objetos resultantes. Los productos construidos por distintos constructores no tienen que pertenecer a la misma jerarquía de clase o interfaz.
4. **Directora**: define el orden en el que se invocarán los pasos de construcción, por lo que puedes crear y reutilizar configuraciones específicas de los productos.
5. **Cliente**: debe asociar uno de los objetos constructores con la clase directora.

## Aplicabilidad

- Utiliza el patrón Builder para evitar un "constructor telescópico".
- Utiliza el patrón Builder cuando quieras que el código sea capaz de crear distintas representaciones de ciertos productos.
- Utiliza el patrón Builder para construir árboles Composite u otros objetos complejos.

## Pros y Contras

### Pros
- Puedes construir objetos paso a paso, aplazar pasos de la construcción o ejecutar pasos de forma recursiva.
- Puedes reutilizar el mismo código de construcción para varias representaciones de productos.
- Principio de responsabilidad única. Puedes aislar un código de construcción complejo de la lógica de negocio del producto.

### Contras
- La complejidad general del código aumenta, ya que el patrón exige la creación de varias clases nuevas.

## Relaciones con otros patrones

- Muchos diseños empiezan utilizando Factory Method y evolucionan hacia Abstract Factory, Prototype o Builder.
- Builder se enfoca en construir objetos complejos, paso a paso. Abstract Factory se especializa en crear familias de objetos relacionados.
- Puedes utilizar Builder para crear árboles Composite complejos, ya que puedes programar sus pasos de construcción para que funcionen de forma recursiva.
- Puedes combinar Builder con Bridge: la clase directora juega el papel de la abstracción, mientras que diferentes constructoras actúan como implementaciones.
- Los patrones Abstract Factory, Builder y Prototype pueden todos ellos implementarse como Singletons.

## Ejemplo en Python

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
```

### Output

```
Standard basic product: 
Product parts: PartA1

Standard full featured product: 
Product parts: PartA1, PartB1, PartC1

Custom product: 
Product parts: PartA1, PartB1
```

## Referencias

- [Refactoring Guru - Builder](https://refactoring.guru/es/design-patterns/builder)
- [Ejemplo en Python](https://refactoring.guru/es/design-patterns/builder/python/example)
