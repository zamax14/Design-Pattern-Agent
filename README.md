# Patrones de Diseño - Documentación

Documentación completa de los 22 patrones de diseño del catálogo GoF (Gang of Four), con descripciones en español y ejemplos de código en Python.

Fuente: [Refactoring Guru](https://refactoring.guru/es/design-patterns/catalog)

## Patrones Creacionales (5)

Proporcionan mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización de código.

| Patrón | Descripción |
|--------|-------------|
| [Factory Method](creacionales/factory-method.md) | Proporciona una interfaz para crear objetos en una superclase, permitiendo a las subclases alterar el tipo de objetos que se crearán. |
| [Abstract Factory](creacionales/abstract-factory.md) | Produce familias de objetos relacionados sin especificar sus clases concretas. |
| [Builder](creacionales/builder.md) | Construye objetos complejos paso a paso. |
| [Prototype](creacionales/prototype.md) | Copia objetos existentes sin que el código dependa de sus clases. |
| [Singleton](creacionales/singleton.md) | Garantiza que una clase tenga una única instancia con un punto de acceso global. |

## Patrones Estructurales (7)

Explican cómo ensamblar objetos y clases en estructuras más grandes, mientras se mantiene la flexibilidad y eficiencia.

| Patrón | Descripción |
|--------|-------------|
| [Adapter](estructurales/adapter.md) | Permite la colaboración entre objetos con interfaces incompatibles. |
| [Bridge](estructurales/bridge.md) | Divide una clase grande en dos jerarquías separadas (abstracción e implementación). |
| [Composite](estructurales/composite.md) | Compone objetos en estructuras de árbol para trabajar con ellos como objetos individuales. |
| [Decorator](estructurales/decorator.md) | Añade funcionalidades a objetos colocándolos dentro de objetos encapsuladores. |
| [Facade](estructurales/facade.md) | Proporciona una interfaz simplificada a un subsistema complejo. |
| [Flyweight](estructurales/flyweight.md) | Ahorra RAM compartiendo partes del estado entre varios objetos. |
| [Proxy](estructurales/proxy.md) | Proporciona un sustituto o marcador de posición para otro objeto. |

## Patrones de Comportamiento (10)

Se encargan de una comunicación efectiva y la asignación de responsabilidades entre objetos.

| Patrón | Descripción |
|--------|-------------|
| [Chain of Responsibility](comportamiento/chain-of-responsibility.md) | Pasa solicitudes a lo largo de una cadena de manejadores. |
| [Command](comportamiento/command.md) | Convierte una solicitud en un objeto independiente con toda la información sobre la solicitud. |
| [Iterator](comportamiento/iterator.md) | Recorre los elementos de una colección sin exponer su representación subyacente. |
| [Mediator](comportamiento/mediator.md) | Reduce las dependencias caóticas entre objetos restringiendo las comunicaciones directas. |
| [Memento](comportamiento/memento.md) | Guarda y restaura el estado previo de un objeto sin revelar los detalles de su implementación. |
| [Observer](comportamiento/observer.md) | Define un mecanismo de suscripción para notificar a varios objetos sobre eventos. |
| [State](comportamiento/state.md) | Permite a un objeto alterar su comportamiento cuando cambia su estado interno. |
| [Strategy](comportamiento/strategy.md) | Define una familia de algoritmos intercambiables. |
| [Template Method](comportamiento/template-method.md) | Define el esqueleto de un algoritmo en la superclase, permitiendo a las subclases sobrescribir pasos. |
| [Visitor](comportamiento/visitor.md) | Separa algoritmos de los objetos sobre los que operan. |
