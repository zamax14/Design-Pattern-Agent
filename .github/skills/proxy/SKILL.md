---
name: proxy
description: 'Implementar el patrón Proxy en Python. Usar cuando necesitas controlar acceso a un objeto, implementar lazy loading, caching, logging de solicitudes, control de acceso, o manejar objetos remotos de forma transparente.'
argument-hint: 'Describe el objeto cuyo acceso quieres controlar y qué tipo de proxy necesitas'
---

# Proxy — Patrón Estructural

Proporciona un sustituto o placeholder para otro objeto. El proxy controla el acceso al objeto original, permitiendo ejecutar lógica antes o después de que la solicitud llegue al objeto real. Comparte la misma interfaz que el servicio.

## Cuándo Usar
- **Proxy virtual (lazy loading)**: Tienes un objeto pesado que consume recursos innecesariamente
- **Proxy de protección**: Quieres restringir acceso según credenciales del cliente
- **Proxy remoto**: El servicio está en un servidor remoto
- **Proxy de logging**: Quieres registrar el historial de solicitudes
- **Proxy de caché**: Necesitas cachear resultados de solicitudes recurrentes
- **Referencia inteligente**: Necesitas descartar un objeto pesado cuando no hay clientes activos

## Procedimiento

### 1. Analizar Aplicabilidad
- Identifica el tipo de proxy necesario (virtual, protección, remoto, logging, caché)
- Verifica que el proxy debe tener la misma interfaz que el servicio
- Si quieres añadir funcionalidad apilable, usa Decorator en su lugar
- Si quieres simplificar un subsistema, usa Facade

### 2. Implementar el Patrón en Python
1. Define la interfaz **Subject** (ABC) con los métodos del servicio
2. Crea **RealSubject** que implementa la lógica de negocio real
3. Crea la clase **Proxy** que mantiene referencia al RealSubject
4. El Proxy implementa la misma interfaz y añade su lógica (check access, log, cache, etc.)
5. Tras su lógica, el Proxy delega al RealSubject
6. El Proxy normalmente gestiona el ciclo de vida completo del RealSubject

### 3. Guía Educativa
- Explica los diferentes tipos de proxy y sus casos de uso específicos
- Muestra cómo el proxy es transparente para el cliente (misma interfaz)
- Señala ventajas: control sin conocimiento del cliente, gestión de ciclo de vida, Open/Closed
- Señala desventajas: complejidad por nuevas clases, posible latencia

## Estructura

```
Subject (ABC)                   # Interfaz común para servicio y proxy
│  request()
│
├── RealSubject                 # Servicio con lógica de negocio real
│   request()
│
└── Proxy                       # Controla acceso al RealSubject
    _real_subject: RealSubject
    request()                   # check_access() → delegate → log_access()
    check_access() -> bool
    log_access()
```

## Ejemplo de Referencia en Python

```python
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Procesando solicitud")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Verificando acceso")
        return True

    def log_access(self) -> None:
        print("Proxy: Registrando solicitud")

# Código cliente — trabaja con Subject sin saber si es proxy o real
def client_code(subject: Subject) -> None:
    subject.request()

real = RealSubject()
client_code(real)       # Directo

proxy = Proxy(real)
client_code(proxy)      # A través del proxy (con acceso + logging)
```

## Relaciones con Otros Patrones
- **Adapter** cambia la interfaz; **Proxy** la mantiene idéntica
- **Decorator** es similar en estructura pero controlado por el cliente; **Proxy** gestiona su propio ciclo de vida
- **Facade** también almacena e inicializa entidades complejas, pero con interfaz diferente
