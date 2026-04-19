# Decorator

**Tipo:** Estructural
**También conocido como:** Decorador, Envoltorio, Wrapper

## Propósito

Decorator es un patrón de diseño estructural que te permite añadir funcionalidades a objetos colocando estos objetos dentro de objetos encapsuladores especiales que contienen estas funcionalidades.

## Problema

Imagina que estás trabajando en una biblioteca de notificaciones que permite a otros programas notificar a sus usuarios acerca de eventos importantes. La versión inicial se basaba en la clase `Notificador` con un único método `send` que enviaba notificaciones por correo electrónico.

En cierto momento, los usuarios quieren más: SMS, Facebook, Slack. Extender la clase `Notificador` creando subclases funciona al principio, pero cuando los usuarios quieren usar varios canales al mismo tiempo, se produce una explosión combinatoria de subclases.

## Solución

Cuando tenemos que alterar la funcionalidad de un objeto, lo primero que se viene a la mente es extender una clase. No obstante, la herencia es estática y las subclases sólo pueden tener una clase padre.

Una alternativa es emplear la **Agregación** o la **Composición**: un objeto tiene una referencia a otro y le delega parte del trabajo.

"Wrapper" (envoltorio) es el sobrenombre alternativo del patrón Decorator. Un wrapper es un objeto que puede vincularse con un objeto objetivo. El wrapper contiene el mismo grupo de métodos que el objetivo y le delega todas las solicitudes que recibe, pero puede alterar el resultado haciendo algo antes o después de pasar la solicitud al objetivo.

Se puede envolver un objeto en varios wrappers, añadiéndole el comportamiento combinado de todos ellos.

## Estructura

1. **Componente**: declara la interfaz común tanto para wrappers como para objetos envueltos.
2. **Componente Concreto**: clase de objetos envueltos. Define el comportamiento básico, que los decoradores pueden alterar.
3. **Decoradora Base**: tiene un campo para referenciar un objeto envuelto. La clase decoradora base delega todas las operaciones al objeto envuelto.
4. **Decoradores Concretos**: definen funcionalidades adicionales que se pueden añadir dinámicamente a los componentes. Sobrescriben métodos de la clase decoradora base y ejecutan su comportamiento antes o después de invocar al método padre.
5. **Cliente**: puede envolver componentes en varias capas de decoradores.

## Aplicabilidad

- Utiliza el patrón Decorator cuando necesites asignar funcionalidades adicionales a objetos durante el tiempo de ejecución sin descomponer el código que utiliza esos objetos.
- Utiliza el patrón cuando resulte extraño o no sea posible extender el comportamiento de un objeto utilizando la herencia.

## Pros y Contras

### Pros
- Puedes extender el comportamiento de un objeto sin crear una nueva subclase.
- Puedes añadir o eliminar responsabilidades de un objeto durante el tiempo de ejecución.
- Puedes combinar varios comportamientos envolviendo un objeto con varios decoradores.
- Principio de responsabilidad única. Puedes dividir una clase monolítica que implementa muchas variantes posibles de comportamiento, en varias clases más pequeñas.

### Contras
- Resulta difícil eliminar un wrapper específico de la pila de wrappers.
- Es difícil implementar un decorador de tal forma que su comportamiento no dependa del orden en la pila de decoradores.
- El código de configuración inicial de las capas puede tener un aspecto desagradable.

## Relaciones con otros patrones

- Adapter proporciona una interfaz completamente diferente. Con Decorator la interfaz permanece igual o se amplía.
- Chain of Responsibility y Decorator tienen estructuras de clase muy similares. Ambos se basan en la composición recursiva.
- Composite y Decorator tienen diagramas de estructura similares. Un Decorator es como un Composite pero sólo tiene un componente hijo.
- Decorator te permite cambiar la piel de un objeto, mientras que Strategy te permite cambiar sus entrañas.
- Decorator y Proxy tienen estructuras similares, pero propósitos muy distintos.

## Ejemplo en Python

```python
class Component():
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def operation(self) -> str:
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """

    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...


if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)
```

### Output

```
Client: I've got a simple component:
RESULT: ConcreteComponent

Client: Now I've got a decorated component:
RESULT: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
```

## Referencias

- [Refactoring Guru - Decorator](https://refactoring.guru/es/design-patterns/decorator)
- [Ejemplo en Python](https://refactoring.guru/es/design-patterns/decorator/python/example)
