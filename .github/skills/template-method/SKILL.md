---
name: template-method
description: 'Implementar el patrón Template Method en Python. Usar cuando necesitas definir el esqueleto de un algoritmo en una superclase permitiendo que subclases sobreescriban pasos específicos, reducir código duplicado entre clases con algoritmos similares, o usar hooks para extensión.'
argument-hint: 'Describe el algoritmo cuya estructura quieres fijar pero cuyos pasos deben ser extensibles'
---

# Template Method — Patrón de Comportamiento

Define el esqueleto de un algoritmo en la superclase pero permite que las subclases sobreescriban pasos específicos sin cambiar la estructura general. Usa herencia para variar partes del algoritmo.

## Cuándo Usar
- Quieres que los clientes extiendan solo pasos particulares de un algoritmo, no su estructura
- Tienes muchas clases con algoritmos casi idénticos con diferencias menores
- Quieres evitar duplicación de código entre algoritmos similares
- Necesitas puntos de extensión (hooks) en lugares específicos del algoritmo

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica el algoritmo que tiene una estructura fija con pasos variables
- Verifica que las variaciones son solo en pasos específicos, no en la estructura
- Si necesitas cambiar el algoritmo en runtime, usa Strategy (composición > herencia)
- Si el algoritmo puede variar completamente, Strategy es mejor opción

### 2. Implementar el Patrón en Python
1. Crea la **AbstractClass** (ABC) con el `template_method()` que define la estructura
2. El template_method llama en orden: operaciones base, operaciones abstractas, y hooks
3. **Operaciones base**: métodos con implementación por defecto en la clase abstracta
4. **Operaciones abstractas** (`@abstractmethod`): deben ser implementadas por subclases
5. **Hooks**: métodos vacíos opcionales que subclases pueden sobreescribir opcionalmente
6. Crea **ConcreteClasses** que implementan las operaciones abstractas y opcionalmente los hooks
7. El template_method NO debe ser sobreescrito (es el esqueleto fijo)

### 3. Guía Educativa
- Explica los tres tipos de métodos: base (fijos), abstractos (obligatorios), hooks (opcionales)
- Muestra cómo el template method define el orden invariante
- Señala ventajas: reutilización de código duplicado, clientes solo extienden partes específicas
- Señala desventajas: clientes limitados por el esqueleto, puede violar LSP, difícil de mantener con muchos pasos

## Estructura

```
AbstractClass (ABC)
│  template_method()            # Esqueleto fijo del algoritmo (NO sobreescribir)
│  base_operation1()            # Implementación por defecto
│  base_operation2()            # Implementación por defecto
│  required_operation1()        # @abstractmethod — obligatorio
│  required_operation2()        # @abstractmethod — obligatorio
│  hook1()                      # Vacío — opcional para subclases
│  hook2()                      # Vacío — opcional para subclases
│
├── ConcreteClass1              # Implementa required_*, opcionalmente hooks
└── ConcreteClass2              # Otra implementación
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self) -> None:
        """Esqueleto del algoritmo — no sobreescribir."""
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook1()
        self.required_operation2()
        self.hook2()

    def base_operation1(self) -> None:
        print("AbstractClass: operación base 1")

    def base_operation2(self) -> None:
        print("AbstractClass: operación base 2")

    @abstractmethod
    def required_operation1(self) -> None:
        pass

    @abstractmethod
    def required_operation2(self) -> None:
        pass

    def hook1(self) -> None:
        """Hook opcional — subclases pueden sobreescribir."""
        pass

    def hook2(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    def required_operation1(self) -> None:
        print("ConcreteClass1: operación requerida 1")

    def required_operation2(self) -> None:
        print("ConcreteClass1: operación requerida 2")

class ConcreteClass2(AbstractClass):
    def required_operation1(self) -> None:
        print("ConcreteClass2: operación requerida 1")

    def required_operation2(self) -> None:
        print("ConcreteClass2: operación requerida 2")

    def hook1(self) -> None:
        print("ConcreteClass2: hook1 sobreescrito")

# Código cliente
def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()

client_code(ConcreteClass1())
client_code(ConcreteClass2())  # Incluye hook1 personalizado
```

## Relaciones con Otros Patrones
- **Factory Method** es una especialización de Template Method; puede servir como un paso del template
- **Template Method** usa herencia (estático, nivel de clase); **Strategy** usa composición (dinámico, nivel de objeto)
