---
name: facade
description: 'Implementar el patrón Facade en Python. Usar cuando necesitas una interfaz simplificada para un subsistema complejo, ocultar la complejidad de librerías o frameworks, o estructurar un subsistema en capas.'
argument-hint: 'Describe el subsistema complejo que quieres simplificar'
---

# Facade — Patrón Estructural

Proporciona una interfaz simplificada a una librería, framework, o cualquier otro grupo complejo de clases. La fachada ofrece acceso conveniente a funcionalidad específica del subsistema, orquestando sus componentes internos.

## Cuándo Usar
- Necesitas una interfaz limitada pero directa a un subsistema complejo
- Quieres estructurar un subsistema en capas (cada capa tiene su fachada)
- Quieres desacoplar el código cliente de los detalles internos del subsistema
- Necesitas simplificar la inicialización y coordinación de múltiples objetos

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica el subsistema complejo con muchas clases interdependientes
- Verifica que los clientes necesitan solo una fracción de la funcionalidad
- Si necesitas traducir interfaces, usa Adapter
- Si necesitas esconder solo la creación de objetos, usa Abstract Factory
- Cuidado con crear un "god object" — divide en múltiples fachadas si es necesario

### 2. Implementar el Patrón en Python
1. Identifica las clases del **Subsistema** que la fachada va a orquestar
2. Crea la clase **Facade** que recibe las dependencias del subsistema por constructor
3. La Facade expone métodos simples que internamente coordinan múltiples objetos del subsistema
4. Los clientes usan la Facade en lugar de interactuar directamente con el subsistema
5. Las clases del subsistema no conocen la existencia de la Facade
6. Si es necesario, crea **Fachadas Adicionales** para agrupar funcionalidad no relacionada

### 3. Guía Educativa
- Explica cómo la fachada aísla al cliente de la complejidad del subsistema
- Muestra que el subsistema sigue siendo accesible directamente si se necesita
- Señala ventajas: aislamiento de complejidad, interfaz simple
- Señala desventajas: la fachada puede convertirse en god object acoplado a todo

## Estructura

```
Facade                          # Interfaz simplificada
│  _subsystem1: Subsystem1
│  _subsystem2: Subsystem2
│  operation() -> str           # Coordina subsistemas
│
Subsystem1                      # Clase del subsistema
│  operation1(), operation_n()
│
Subsystem2                      # Otra clase del subsistema
│  operation1(), operation_z()
```

## Ejemplo de Referencia en Python

```python
class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: Listo"

    def operation_n(self) -> str:
        return "Subsystem1: Ejecutando"

class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2: Preparado"

    def operation_z(self) -> str:
        return "Subsystem2: Disparando"

class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self) -> str:
        results = [
            "Facade inicializa subsistemas:",
            self._subsystem1.operation1(),
            self._subsystem2.operation1(),
            "Facade ordena acción:",
            self._subsystem1.operation_n(),
            self._subsystem2.operation_z(),
        ]
        return "\n".join(results)

# Código cliente — trabaja solo con la fachada
facade = Facade(Subsystem1(), Subsystem2())
print(facade.operation())
```

## Relaciones con Otros Patrones
- **Adapter** hace usable una interfaz existente; **Facade** define una nueva interfaz simplificada
- **Abstract Factory** puede servir como alternativa cuando solo necesitas esconder la creación
- **Flyweight** crea muchos objetos pequeños; **Facade** crea un único objeto para todo un subsistema
- **Mediator** organiza colaboración similar pero con comunicación bidireccional
- Puede transformarse en **Singleton** ya que normalmente basta un solo objeto fachada
- Similar a **Proxy** en que ambos almacenan y pueden inicializar una entidad compleja
