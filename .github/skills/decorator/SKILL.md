---
name: decorator
description: 'Implementar el patrón Decorator en Python. Usar cuando necesitas añadir funcionalidades a objetos en tiempo de ejecución sin modificar su clase, componer comportamientos mediante envolturas apilables, o evitar explosión de subclases por combinaciones de funcionalidad.'
argument-hint: 'Describe el objeto al que quieres añadir funcionalidades dinámicamente'
---

# Decorator — Patrón Estructural

Permite añadir funcionalidades a objetos colocándolos dentro de objetos envolventes especiales (wrappers). Los decoradores se apilan recursivamente, cada uno añadiendo comportamiento antes o después de delegar al componente envuelto.

## Cuándo Usar
- Necesitas asignar funcionalidades adicionales a objetos en tiempo de ejecución sin romper el código existente
- Es incómodo o imposible extender comportamiento usando herencia
- Necesitas combinar varios comportamientos de forma flexible (composición sobre herencia)
- Quieres dividir una clase monolítica en varias clases pequeñas con responsabilidades únicas

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica la clase base cuyo comportamiento quieres extender dinámicamente
- Verifica que necesitas composición flexible (no una jerarquía fija de herencia)
- Si solo necesitas un nivel de envoltorio sin composición, considera Proxy
- Si quieres cambiar el algoritmo completo, usa Strategy

### 2. Implementar el Patrón en Python
1. Define la interfaz **Component** con el método principal (ej: `operation()`)
2. Crea **ConcreteComponent** con la implementación base
3. Crea la clase **Decorator** base que envuelve un Component y delega `operation()`
4. Crea **ConcreteDecoratorA**, **ConcreteDecoratorB** que sobreescriben `operation()` añadiendo comportamiento
5. Los decoradores llaman a `self.component.operation()` y añaden su propia lógica
6. El cliente apila decoradores: `Decorator2(Decorator1(ConcreteComponent()))`

### 3. Guía Educativa
- Explica composición recursiva: cada decorador envuelve al anterior
- Muestra cómo apilar decoradores para combinar funcionalidades
- Señala ventajas: composición flexible, SRP, extensión en runtime
- Señala desventajas: difícil quitar un decorador del stack, orden puede importar

## Estructura

```
Component                       # Interfaz común para componentes y decoradores
│  operation() -> str
│
├── ConcreteComponent           # Implementación base
│   operation() -> str
│
└── Decorator(Component)        # Base decorador — envuelve un Component
    _component: Component
    operation() -> str          # Delega a _component.operation()
    ├── ConcreteDecoratorA      # Añade comportamiento A
    └── ConcreteDecoratorB      # Añade comportamiento B
```

## Ejemplo de Referencia en Python

```python
class Component:
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"DecoratorA({self.component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"DecoratorB({self.component.operation()})"

# Uso — apilando decoradores
simple = ConcreteComponent()
decorated = ConcreteDecoratorA(simple)
double_decorated = ConcreteDecoratorB(decorated)
print(double_decorated.operation())
# DecoratorB(DecoratorA(ConcreteComponent))
```

## Relaciones con Otros Patrones
- **Adapter** cambia la interfaz; **Decorator** la mantiene o expande
- **Chain of Responsibility** tiene estructura similar (composición recursiva)
- **Composite** es similar pero con múltiples hijos; **Decorator** solo tiene uno
- **Decorator** cambia la "piel"; **Strategy** cambia las "entrañas"
- **Proxy** estructura similar pero propósito diferente (controla ciclo de vida)
