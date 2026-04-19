---
name: builder
description: 'Implementar el patrón Builder en Python. Usar cuando necesitas construir objetos complejos paso a paso, evitar constructores telescópicos con muchos parámetros, o crear distintas representaciones del mismo objeto.'
argument-hint: 'Describe el objeto complejo que necesitas construir'
---

# Builder — Patrón Creacional

Permite construir objetos complejos paso a paso. El patrón permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción. Opcionalmente usa un Director para definir el orden de los pasos.

## Cuándo Usar
- Tienes un constructor con muchos parámetros opcionales ("constructor telescópico")
- Necesitas crear distintas representaciones de un mismo objeto
- Quieres construir objetos Composite u otros objetos complejos paso a paso
- Necesitas controlar el proceso de construcción (orden, pasos opcionales)

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica objetos con muchos campos opcionales o configuraciones complejas
- Verifica si el mismo proceso de construcción debe crear diferentes representaciones
- Si los objetos son simples, el patrón es excesivo — usa un constructor directo
- Si necesitas familias de productos, usa Abstract Factory en su lugar

### 2. Implementar el Patrón en Python
1. Define la interfaz **Builder** (ABC) con métodos para cada paso de construcción
2. Crea **ConcreteBuilder** con `reset()`, métodos de pasos, y propiedad `product`
3. Define la clase **Product** que acumula las partes
4. Opcionalmente, crea un **Director** que defina secuencias predefinidas de pasos
5. El `product` getter debe resetear el builder tras retornar el producto
6. Añade type hints completos

### 3. Guía Educativa
- Explica cómo se elimina el constructor telescópico
- Muestra la diferencia entre usar Director vs. usar el builder directamente
- Señala ventajas: construcción paso a paso, reutilización, SRP
- Señala desventajas: complejidad por nuevas clases

## Estructura

```
Builder (ABC)                   # Interfaz con pasos de construcción
├── ConcreteBuilder1            # Implementa pasos, tiene reset() y product
└── ConcreteBuilder2            # Otra implementación (producto diferente)

Product                         # Objeto resultante con partes acumuladas
Director                        # Opcional: define secuencias de pasos
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
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

class Product:
    def __init__(self) -> None:
        self.parts: list[Any] = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes: {', '.join(self.parts)}")

class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA")

    def produce_part_b(self) -> None:
        self._product.add("PartB")

    def produce_part_c(self) -> None:
        self._product.add("PartC")

class Director:
    def __init__(self) -> None:
        self._builder: Builder | None = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal(self) -> None:
        self.builder.produce_part_a()

    def build_full(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

# Código cliente
director = Director()
builder = ConcreteBuilder()
director.builder = builder

director.build_full()
builder.product.list_parts()  # Partes: PartA, PartB, PartC
```

## Relaciones con Otros Patrones
- Evoluciona desde **Factory Method** cuando se necesita más control sobre la construcción
- **Abstract Factory** crea familias de una vez; **Builder** construye paso a paso
- Se usa para crear árboles **Composite** complejos
- Se combina con **Bridge**: Director = abstracción, Builders = implementaciones
- Puede implementarse como **Singleton**
