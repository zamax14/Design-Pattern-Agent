---
name: abstract-factory
description: 'Implementar el patrón Abstract Factory en Python. Usar cuando necesitas crear familias de objetos relacionados sin especificar clases concretas, garantizar compatibilidad entre productos de una misma variante, o desacoplar código cliente de las clases de productos.'
argument-hint: 'Describe el problema o el código donde quieres aplicar Abstract Factory'
---

# Abstract Factory — Patrón Creacional

Proporciona una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas. Cada fábrica concreta produce una variante completa de productos que son compatibles entre sí.

## Cuándo Usar
- Tu código debe funcionar con varias familias de productos relacionados
- No quieres depender de las clases concretas de los productos
- Necesitas garantizar que los productos de una familia sean compatibles entre sí
- Tienes un grupo de Factory Methods que difuminan la responsabilidad principal de una clase
- Quieres permitir extensibilidad futura con nuevas variantes de productos

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica si existen familias de productos relacionados (ej: UI themes, DB drivers, parsers)
- Verifica que los productos de una familia deben usarse juntos (compatibilidad)
- Si solo hay un tipo de producto, usa Factory Method en su lugar
- Si la creación es paso a paso, considera Builder

### 2. Implementar el Patrón en Python
1. Define interfaces **AbstractProductA**, **AbstractProductB** (clases ABC con `@abstractmethod`)
2. Crea las implementaciones concretas por variante (ej: `ConcreteProductA1`, `ConcreteProductA2`)
3. Declara la interfaz **AbstractFactory** con métodos `create_product_a()`, `create_product_b()`
4. Implementa **ConcreteFactory1**, **ConcreteFactory2** que retornen productos de su variante
5. El código cliente recibe la fábrica por inyección y trabaja solo con interfaces abstractas
6. Añade type hints completos

### 3. Guía Educativa
- Explica cómo se garantiza compatibilidad entre productos de una misma variante
- Muestra cómo añadir nuevas variantes sin modificar código existente
- Señala ventajas: compatibilidad, desacoplamiento, Open/Closed, SRP
- Señala desventajas: complejidad por muchas interfaces y clases nuevas

## Estructura

```
AbstractProductA (ABC)          AbstractProductB (ABC)
├── ConcreteProductA1           ├── ConcreteProductB1
└── ConcreteProductA2           └── ConcreteProductB2

AbstractFactory (ABC)
│  create_product_a() -> AbstractProductA
│  create_product_b() -> AbstractProductB
├── ConcreteFactory1            # Crea A1 + B1
└── ConcreteFactory2            # Crea A2 + B2
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    @abstractmethod
    def function_a(self) -> str:
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def function_b(self) -> str:
        pass

    @abstractmethod
    def collaborate(self, product_a: AbstractProductA) -> str:
        pass

class ConcreteProductA1(AbstractProductA):
    def function_a(self) -> str:
        return "Producto A1"

class ConcreteProductA2(AbstractProductA):
    def function_a(self) -> str:
        return "Producto A2"

class ConcreteProductB1(AbstractProductB):
    def function_b(self) -> str:
        return "Producto B1"

    def collaborate(self, product_a: AbstractProductA) -> str:
        return f"B1 colabora con ({product_a.function_a()})"

class ConcreteProductB2(AbstractProductB):
    def function_b(self) -> str:
        return "Producto B2"

    def collaborate(self, product_a: AbstractProductA) -> str:
        return f"B2 colabora con ({product_a.function_a()})"

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

# Código cliente — trabaja solo con interfaces abstractas
def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(product_b.function_b())
    print(product_b.collaborate(product_a))
```

## Relaciones con Otros Patrones
- Evoluciona desde **Factory Method** cuando se necesitan familias de productos
- Se basa frecuentemente en un grupo de **Factory Methods**
- Puede usar **Prototype** para implementar los métodos de creación
- Puede servir como alternativa a **Facade** para esconder creación de subsistemas
- Se combina con **Bridge** cuando abstracciones requieren implementaciones específicas
- Puede implementarse como **Singleton**
