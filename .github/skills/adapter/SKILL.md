---
name: adapter
description: 'Implementar el patrón Adapter en Python. Usar cuando necesitas que clases con interfaces incompatibles colaboren entre sí, integrar código legacy o de terceros, o reutilizar clases existentes que no comparten una interfaz común.'
argument-hint: 'Describe las interfaces incompatibles que necesitas conectar'
---

# Adapter — Patrón Estructural

Permite la colaboración entre objetos con interfaces incompatibles. Convierte la interfaz de un objeto para que otro objeto pueda entenderla, actuando como un envoltorio traductor entre dos interfaces.

## Cuándo Usar
- Quieres usar una clase existente cuya interfaz es incompatible con el resto del código
- Necesitas integrar código de terceros o librerías legacy sin modificarlas
- Quieres reutilizar varias subclases existentes que carecen de funcionalidad común
- Necesitas traducir entre dos interfaces sin modificar ninguna de las dos

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica las dos interfaces incompatibles: el servicio existente y la interfaz esperada por el cliente
- Verifica que no puedes simplemente modificar el servicio (es de terceros, legacy, etc.)
- Si necesitas una interfaz completamente nueva para un subsistema, usa Facade
- Si la interfaz es la misma pero quieres añadir funcionalidad, usa Decorator

### 2. Implementar el Patrón en Python
1. Define la interfaz **Target** que el cliente espera (puede ser una clase ABC o protocolo)
2. Identifica el **Adaptee** (servicio) con la interfaz incompatible
3. Crea la clase **Adapter** que hereda de Target y envuelve el Adaptee
4. El Adapter traduce las llamadas del Target a llamadas del Adaptee
5. En Python, puedes usar herencia múltiple: `class Adapter(Target, Adaptee)`
6. El cliente trabaja solo con la interfaz Target

### 3. Guía Educativa
- Explica las dos variantes: object adapter (composición) y class adapter (herencia múltiple)
- Muestra cómo el adapter desacopla el código cliente de la implementación del servicio
- Señala ventajas: SRP (separar conversión de lógica), Open/Closed (nuevos adapters sin romper)
- Señala desventajas: complejidad añadida — a veces es más simple cambiar el servicio

## Estructura

```
Target                          # Interfaz que el cliente espera
│  request() -> str
│
Adaptee                         # Servicio con interfaz incompatible
│  specific_request() -> str
│
Adapter(Target)                 # Traduce entre Target y Adaptee
│  adaptee: Adaptee
│  request() -> str             # Llama a adaptee.specific_request()
```

## Ejemplo de Referencia en Python

```python
class Target:
    """Interfaz que el cliente espera."""
    def request(self) -> str:
        return "Target: comportamiento por defecto"

class Adaptee:
    """Servicio con interfaz incompatible."""
    def specific_request(self) -> str:
        return ".eetpadA led otneimatropmoc laicepsE"

class Adapter(Target, Adaptee):
    """Traduce la interfaz del Adaptee a la del Target."""
    def request(self) -> str:
        return f"Adapter: (TRADUCIDO) {self.specific_request()[::-1]}"

# Código cliente — trabaja solo con la interfaz Target
def client_code(target: Target) -> None:
    print(target.request())

client_code(Target())     # Comportamiento normal
client_code(Adapter())    # Adaptee traducido transparentemente
```

## Relaciones con Otros Patrones
- **Bridge** se diseña por adelantado; **Adapter** se usa con aplicaciones existentes
- **Decorator** mantiene/expande la interfaz; **Adapter** la cambia completamente
- **Facade** define una interfaz nueva para un subsistema; **Adapter** hace usable la existente
- **Proxy** mantiene la misma interfaz; **Adapter** la transforma
