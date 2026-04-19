---
name: factory-method
description: 'Implementar el patrón Factory Method en Python. Usar cuando necesitas crear objetos sin especificar la clase exacta, delegar la creación a subclases, desacoplar código cliente de la creación de objetos, o reemplazar condicionales de instanciación.'
argument-hint: 'Describe el problema o el código donde quieres aplicar Factory Method'
---

# Factory Method — Patrón Creacional

Proporciona una interfaz para crear objetos en una superclase, mientras permite a las subclases alterar el tipo de objetos que se crearán. En lugar de llamar a `new`/instanciar directamente, se invoca un método fábrica que las subclases pueden sobreescribir.

## Cuándo Usar
- No conoces de antemano los tipos exactos de objetos que tu código necesita
- Quieres ofrecer a usuarios de tu biblioteca una forma de extender componentes internos
- Hay condicionales (`if/elif/else`) que instancian diferentes clases según un parámetro
- Quieres cumplir el Principio Abierto/Cerrado en la creación de objetos
- Quieres reutilizar objetos existentes en lugar de reconstruirlos cada vez

## Procedimiento

### 1. Analizar Aplicabilidad
- Examina el código o problema descrito por el usuario
- Identifica lógica de creación de objetos acoplada al código cliente
- Busca condicionales que instancian diferentes clases según algún parámetro
- Si el patrón no aplica, sugiere alternativas: Abstract Factory, Builder o Prototype

### 2. Implementar el Patrón en Python
1. Define la interfaz **Product** (clase abstracta con `ABC` y `@abstractmethod`)
2. Crea las clases **ConcreteProduct** que implementen la interfaz
3. Declara la clase **Creator** base con el factory method abstracto que retorna `Product`
4. Implementa **ConcreteCreator** que sobreescriba el factory method
5. Añade type hints completos
6. Genera código cliente que use los creadores de forma polimórfica

### 3. Guía Educativa
- Explica cómo el patrón separa la construcción de objetos de su uso
- Muestra cómo agregar nuevos tipos sin modificar código existente (Open/Closed)
- Señala ventajas: desacoplamiento, extensibilidad, responsabilidad única
- Señala desventajas: puede complicar el código con muchas subclases

## Estructura

```
Product (ABC)                   # Interfaz común de los objetos creados
├── ConcreteProductA            # Implementación A
└── ConcreteProductB            # Implementación B

Creator (ABC)                   # Declara factory_method() abstracto
├── ConcreteCreatorA            # Retorna ConcreteProductA
└── ConcreteCreatorB            # Retorna ConcreteProductB
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Resultado de ProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Resultado de ProductB"

class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator trabajó con {product.operation()}"

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Código cliente — trabaja con Creator sin conocer la clase concreta
def client_code(creator: Creator) -> None:
    print(creator.some_operation())
```

## Relaciones con Otros Patrones
- Evoluciona hacia **Abstract Factory**, **Prototype** o **Builder** según la complejidad
- Se combina con **Iterator** para que subclases de colección devuelvan iteradores compatibles
- Es una especialización de **Template Method**
- **Prototype** no requiere herencia pero necesita inicialización complicada
