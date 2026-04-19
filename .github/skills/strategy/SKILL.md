---
name: strategy
description: 'Implementar el patrón Strategy en Python. Usar cuando necesitas definir una familia de algoritmos intercambiables, cambiar el algoritmo en tiempo de ejecución, reemplazar condicionales que seleccionan variantes de un algoritmo, o aislar lógica de negocio de detalles de implementación.'
argument-hint: 'Describe los algoritmos o comportamientos que quieres hacer intercambiables'
---

# Strategy — Patrón de Comportamiento

Define una familia de algoritmos, coloca cada uno en una clase separada y hace sus objetos intercambiables. El contexto delega el trabajo al objeto strategy actual, que puede cambiarse en runtime.

## Cuándo Usar
- Quieres usar diferentes variantes de un algoritmo y cambiar entre ellas en runtime
- Tienes muchas clases similares que solo difieren en cómo ejecutan cierto comportamiento
- Quieres aislar la lógica de negocio de los detalles de implementación del algoritmo
- Tienes un condicional masivo que selecciona variantes del mismo algoritmo
- Quieres reemplazar herencia por composición

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica los algoritmos o comportamientos que varían
- Verifica que el contexto necesita poder cambiar de algoritmo en runtime
- Si los algoritmos son simples, en Python puedes usar funciones/lambdas en lugar de clases
- Si necesitas transiciones entre variantes, considera State
- Si necesitas encapsular operaciones como objetos, considera Command

### 2. Implementar el Patrón en Python
1. Define la interfaz **Strategy** (ABC) con el método del algoritmo (ej: `do_algorithm(data)`)
2. Crea **ConcreteStrategyA**, **ConcreteStrategyB** con implementaciones diferentes
3. Crea **Context** que recibe Strategy por constructor y expone setter para cambiarla
4. Context delega la ejecución al strategy actual
5. El cliente crea el strategy concreto y lo inyecta al contexto
6. Alternativa pythónica: usa `Callable` o funciones en lugar de clases strategy

### 3. Guía Educativa
- Explica composición sobre herencia: cambiar comportamiento sin cambiar la clase
- Muestra cómo cambiar algoritmo en runtime con el setter
- Señala ventajas: intercambio en runtime, aislamiento de implementación, Open/Closed
- Señala desventajas: excesivo con pocos algoritmos, clientes deben conocer las diferencias

## Estructura

```
Strategy (ABC)                  # Interfaz del algoritmo
│  do_algorithm(data) -> result
├── ConcreteStrategyA           # Implementación A
└── ConcreteStrategyB           # Implementación B

Context                         # Usa Strategy via composición
│  _strategy: Strategy
│  strategy (setter)            # Permite cambiar en runtime
│  do_some_business_logic()     # Delega a _strategy.do_algorithm()
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: list) -> list:
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: list) -> list:
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: list) -> list:
        return list(reversed(sorted(data)))

class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        result = self._strategy.do_algorithm(["a", "c", "b", "d"])
        print(",".join(result))

# Uso — cambiar estrategia en runtime
context = Context(ConcreteStrategyA())
print("Ordenamiento normal:")
context.do_some_business_logic()  # a,b,c,d

print("Ordenamiento inverso:")
context.strategy = ConcreteStrategyB()
context.do_some_business_logic()  # d,c,b,a
```

## Relaciones con Otros Patrones
- **Bridge**, **State** y **Adapter** tienen estructura similar pero resuelven problemas diferentes
- **Command** convierte operaciones en objetos; **Strategy** describe formas de hacer lo mismo
- **Decorator** cambia la "piel"; **Strategy** cambia las "entrañas"
- **Template Method** usa herencia (estático, nivel de clase); **Strategy** usa composición (dinámico, nivel de objeto)
- **State** es una extensión: permite transiciones entre estados; Strategy hace objetos independientes
