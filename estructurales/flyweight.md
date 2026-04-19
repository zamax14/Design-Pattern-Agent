# Flyweight

**Tipo:** Estructural
**También conocido como:** Peso mosca, Peso ligero, Cache

## Propósito

Flyweight es un patrón de diseño estructural que te permite mantener más objetos dentro de la cantidad disponible de RAM compartiendo las partes comunes del estado entre varios objetos en lugar de mantener toda la información en cada objeto.

## Problema

Para divertirte un poco después de largas horas de trabajo, decides crear un sencillo videojuego en el que los jugadores se tienen que mover por un mapa disparándose entre sí. Decides implementar un sistema de partículas realistas que lo distinga de otros juegos. Grandes cantidades de balas, misiles y metralla de las explosiones volarán por todo el mapa, ofreciendo una apasionante experiencia al jugador.

Al terminarlo, subes el último cambio, compilas el juego y se lo envías a un amigo para una partida de prueba. Aunque el juego funcionaba sin problemas en tu máquina, tu amigo no logró jugar durante mucho tiempo. En su computadora el juego se paraba a los pocos minutos de empezar. Tras dedicar varias horas a revisar los registros de depuración, descubres que el juego se paraba debido a una cantidad insuficiente de RAM. Resulta que el equipo de tu amigo es mucho menos potente que tu computadora, y esa es la razón por la que el problema surgió tan rápido en su máquina.

El problema estaba relacionado con tu sistema de partículas. Cada partícula, como una bala, un misil o un trozo de metralla, estaba representada por un objeto separado que contenía gran cantidad de datos. En cierto momento, cuando la masacre alcanzaba su punto culminante en la pantalla del jugador, las partículas recién creadas ya no cabían en el resto de RAM, provocando que el programa fallara.

## Solución

Observando más atentamente la clase `Partícula`, puede ser que te hayas dado cuenta de que los campos de color y sprite consumen mucha más memoria que otros campos. Lo que es peor, esos dos campos almacenan información casi idéntica de todas las partículas. Por ejemplo, todas las balas tienen el mismo color y sprite.

Otras partes del estado de una partícula, como las coordenadas, vector de movimiento y velocidad, son únicas en cada partícula. Después de todo, los valores de estos campos cambian a lo largo del tiempo. Estos datos representan el contexto siempre cambiante en el que existe la partícula, mientras que el color y el sprite se mantienen constantes.

Esta información constante de un objeto suele denominarse su **estado intrínseco**. Existe dentro del objeto y otros objetos únicamente pueden leerla, no cambiarla. El resto del estado del objeto, a menudo alterado "desde el exterior" por otros objetos, se denomina el **estado extrínseco**.

El patrón Flyweight sugiere que dejemos de almacenar el estado extrínseco dentro del objeto. En lugar de eso, debes pasar este estado a métodos específicos que dependen de él. Tan solo el estado intrínseco se mantiene dentro del objeto, permitiendo que lo reutilices en distintos contextos. Como resultado, necesitarás menos de estos objetos, ya que sólo se diferencian en el estado intrínseco, que cuenta con muchas menos variaciones que el extrínseco.

### Flyweight y la inmutabilidad

Debido a que el mismo objeto flyweight puede utilizarse en distintos contextos, debes asegurarte de que su estado no se pueda modificar. Un objeto flyweight debe inicializar su estado una sola vez a través de parámetros del constructor. No debe exponer ningún método set (modificador) o campo público a otros objetos.

### Fábrica flyweight

Para un acceso más cómodo a varios objetos flyweight, puedes crear un método fábrica que gestione un grupo de objetos flyweight existentes. El método acepta el estado intrínseco del flyweight deseado por un cliente, busca un objeto flyweight existente que coincida con este estado y lo devuelve si lo encuentra. Si no, crea un nuevo objeto flyweight y lo añade al grupo.

## Estructura

1. El patrón Flyweight es simplemente una optimización. Antes de aplicarlo, asegúrate de que tu programa tenga un problema de consumo de RAM provocado por tener una gran cantidad de objetos similares en la memoria al mismo tiempo.
2. La clase **Flyweight** contiene la parte del estado del objeto original que pueden compartir varios objetos. El mismo objeto flyweight puede utilizarse en muchos contextos diferentes. El estado almacenado dentro de un objeto flyweight se denomina intrínseco, mientras que al que se pasa a sus métodos se le llama extrínseco.
3. La clase **Contexto** contiene el estado extrínseco, único en todos los objetos originales. Cuando un contexto se empareja con uno de los objetos flyweight, representa el estado completo del objeto original.
4. Normalmente, el comportamiento del objeto original permanece en la clase flyweight. En este caso, quien invoque un método del objeto flyweight debe también pasar las partes adecuadas del estado extrínseco dentro de los parámetros del método. Por otra parte, el comportamiento se puede mover a la clase de contexto, que utilizará el objeto flyweight vinculado como mero objeto de datos.
5. El **Cliente** calcula o almacena el estado extrínseco de los objetos flyweight. Desde la perspectiva del cliente, un flyweight es un objeto plantilla que puede configurarse durante el tiempo de ejecución pasando información contextual dentro de los parámetros de sus métodos.
6. La **Fábrica flyweight** gestiona un grupo de objetos flyweight existentes. Con la fábrica, los clientes no crean objetos flyweight directamente. En lugar de eso, invocan a la fábrica, pasándole partes del estado intrínseco del objeto flyweight deseado. La fábrica revisa objetos flyweight creados previamente y devuelve uno existente que coincida con los criterios de búsqueda, o bien crea uno nuevo si no encuentra nada.

## Aplicabilidad

- Utiliza el patrón Flyweight únicamente cuando tu programa deba soportar una enorme cantidad de objetos que apenas quepan en la RAM disponible.
- La ventaja de aplicar el patrón depende en gran medida de cómo y dónde se utiliza. Resulta más útil cuando:
  - La aplicación necesita generar una cantidad enorme de objetos similares.
  - Esto consume toda la RAM disponible de un dispositivo objetivo.
  - Los objetos contienen estados duplicados que se pueden extraer y compartir entre varios objetos.

## Pros y Contras

### Pros
- Puedes ahorrar mucha RAM, siempre que tu programa tenga toneladas de objetos similares.

### Contras
- Puede que estés cambiando RAM por ciclos CPU cuando deba calcularse de nuevo parte de la información de contexto cada vez que alguien invoque un método flyweight.
- El código se complica mucho. Los nuevos miembros del equipo siempre estarán preguntándose por qué el estado de una entidad se separó de tal manera.

## Relaciones con otros patrones

- Puedes implementar nodos de hoja compartidos del árbol Composite como Flyweights para ahorrar memoria RAM.
- Flyweight muestra cómo crear muchos pequeños objetos, mientras que Facade muestra cómo crear un único objeto que represente un subsistema completo.
- Flyweight podría asemejarse a Singleton si de algún modo pudieras reducir todos los estados compartidos de los objetos a un único objeto flyweight. Pero existen dos diferencias fundamentales entre estos patrones:
  1. Solo debe haber una instancia Singleton, mientras que una clase Flyweight puede tener varias instancias con distintos estados intrínsecos.
  2. El objeto Singleton puede ser mutable. Los objetos flyweight son inmutables.

## Ejemplo en Python

```python
import json
from typing import Dict


class Flyweight():
    """
    The Flyweight stores a common portion of the state (also called intrinsic
    state) that belongs to multiple real business entities. The Flyweight
    accepts the rest of the state (extrinsic state, unique for each entity) via
    its method parameters.
    """

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory():
    """
    The Flyweight Factory creates and manages the Flyweight objects. It ensures
    that flyweights are shared correctly. When the client requests a flyweight,
    the factory either returns an existing instance or creates a new one, if it
    doesn't exist yet.
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
        Returns a Flyweight's string hash for a given state.
        """
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
        Returns an existing Flyweight with a given state or creates a new one.
        """
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    # The client code either stores or calculates extrinsic state and passes it
    # to the flyweight's methods.
    flyweight.operation([plates, owner])


if __name__ == "__main__":
    """
    The client code usually creates a bunch of pre-populated flyweights in the
    initialization stage of the application.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()
```

### Output

```
FlyweightFactory: I have 5 flyweights:
Camaro2018_Chevrolet_pink
C300_Mercedes Benz_black
C500_Mercedes Benz_red
BMW_M5_red
BMW_X6_white

Client: Adding a car to database.
FlyweightFactory: Reusing existing flyweight.
Flyweight: Displaying shared (["BMW", "M5", "red"]) and unique (["CL234IR", "James Doe"]) state.

Client: Adding a car to database.
FlyweightFactory: Can't find a flyweight, creating new one.
Flyweight: Displaying shared (["BMW", "X1", "red"]) and unique (["CL234IR", "James Doe"]) state.

FlyweightFactory: I have 6 flyweights:
Camaro2018_Chevrolet_pink
C300_Mercedes Benz_black
C500_Mercedes Benz_red
BMW_M5_red
BMW_X6_white
BMW_X1_red
```

## Referencias

- [Refactoring Guru - Flyweight](https://refactoring.guru/es/design-patterns/flyweight)
- [Ejemplo en Python](https://refactoring.guru/es/design-patterns/flyweight/python/example)
