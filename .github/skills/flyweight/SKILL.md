---
name: flyweight
description: 'Implementar el patrón Flyweight en Python. Usar cuando necesitas optimizar consumo de RAM con gran cantidad de objetos similares, separar estado intrínseco (compartido) de extrínseco (único), o implementar cache de objetos inmutables.'
argument-hint: 'Describe los objetos que consumen mucha memoria y qué estado comparten'
---

# Flyweight — Patrón Estructural

Permite encajar más objetos en la RAM disponible compartiendo las partes comunes del estado entre varios objetos, en lugar de mantener toda la información en cada uno. Separa estado intrínseco (compartido, inmutable) de estado extrínseco (único, variable).

## Cuándo Usar
- Tu programa necesita soportar una gran cantidad de objetos que apenas caben en RAM
- La aplicación genera muchos objetos similares que consumen toda la memoria
- Los objetos contienen estado duplicado que puede extraerse y compartirse
- Muchos grupos de objetos pueden reemplazarse por pocos objetos compartidos + estado externo

## Procedimiento

### 1. Analizar Aplicabilidad
- Confirma que hay un problema real de consumo de RAM (no optimices prematuramente)
- Identifica qué campos son intrínsecos (compartidos entre muchos objetos, inmutables)
- Identifica qué campos son extrínsecos (únicos por instancia, pasados como parámetros)
- Si los objetos son pocos o todos son únicos, el patrón no aporta beneficio

### 2. Implementar el Patrón en Python
1. Divide los campos de la clase original en intrínsecos y extrínsecos
2. Crea la clase **Flyweight** que almacena solo el estado intrínseco (inmutable)
3. Los métodos del Flyweight reciben el estado extrínseco como parámetros
4. Crea una **FlyweightFactory** con un diccionario cache de flyweights existentes
5. La factory retorna flyweights existentes o crea nuevos según el estado intrínseco
6. El cliente calcula o almacena el estado extrínseco y lo pasa al flyweight

### 3. Guía Educativa
- Explica la separación intrínseco vs. extrínseco con ejemplos concretos
- Muestra cómo la factory garantiza que los flyweights se compartan correctamente
- Señala ventajas: ahorro significativo de RAM con muchos objetos similares
- Señala desventajas: trade-off RAM por CPU, código más complicado

## Estructura

```
Flyweight                       # Almacena estado intrínseco (compartido)
│  _shared_state: str
│  operation(unique_state)      # Recibe estado extrínseco por parámetro
│
FlyweightFactory                # Gestiona y reutiliza flyweights
│  _flyweights: dict[str, Flyweight]
│  get_flyweight(shared_state) -> Flyweight
│
Context                         # Almacena estado extrínseco + referencia a flyweight
```

## Ejemplo de Referencia en Python

```python
import json

class Flyweight:
    def __init__(self, shared_state: list[str]) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: list[str]) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: compartido ({s}) + único ({u})")

class FlyweightFactory:
    _flyweights: dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: list[list[str]]) -> None:
        for state in initial_flyweights:
            key = self._get_key(state)
            self._flyweights[key] = Flyweight(state)

    def _get_key(self, state: list[str]) -> str:
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: list[str]) -> Flyweight:
        key = self._get_key(shared_state)
        if key not in self._flyweights:
            print("Factory: Creando nuevo flyweight")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("Factory: Reutilizando flyweight existente")
        return self._flyweights[key]

# Uso
factory = FlyweightFactory([
    ["BMW", "M5", "rojo"],
    ["Mercedes", "C300", "negro"],
])

# Reutiliza flyweight existente
fw = factory.get_flyweight(["BMW", "M5", "rojo"])
fw.operation(["ABC-123", "Juan"])  # Estado extrínseco

# Crea nuevo flyweight
fw2 = factory.get_flyweight(["Toyota", "Corolla", "blanco"])
fw2.operation(["XYZ-789", "Maria"])
```

## Relaciones con Otros Patrones
- Los nodos hoja de **Composite** pueden implementarse como Flyweights
- **Facade** crea un único objeto para un subsistema; **Flyweight** crea muchos objetos pequeños
- Podría asemejarse a **Singleton** pero: Flyweight puede tener múltiples instancias con estados diferentes, y los flyweights son inmutables
