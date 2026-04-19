"""
Template Method — Ejemplo

Define el esqueleto de un algoritmo en la superclase, permitiendo que
las subclases sobreescriban pasos específicos sin cambiar la estructura.
"""

from abc import ABC, abstractmethod


class DataMiner(ABC):
    """Clase abstracta con template method para minería de datos."""

    def mine(self, path: str) -> None:
        """Template method: esqueleto fijo del algoritmo."""
        raw_data = self.extract(path)
        data = self.parse(raw_data)
        analysis = self.analyze(data)
        self.hook_before_report(analysis)
        self.report(analysis)

    @abstractmethod
    def extract(self, path: str) -> str:
        """Paso abstracto: extraer datos del archivo."""
        pass

    @abstractmethod
    def parse(self, raw_data: str) -> list[str]:
        """Paso abstracto: parsear datos crudos."""
        pass

    def analyze(self, data: list[str]) -> dict:
        """Paso con implementación base: analizar datos."""
        return {
            "total_records": len(data),
            "sample": data[:3] if data else [],
        }

    def hook_before_report(self, analysis: dict) -> None:
        """Hook opcional: subclases pueden sobreescribir."""
        pass

    def report(self, analysis: dict) -> None:
        """Paso con implementación base: generar reporte."""
        print(f"    Reporte: {analysis['total_records']} registros")
        print(f"    Muestra: {analysis['sample']}")


class CSVDataMiner(DataMiner):
    """Subclase: mina datos de archivos CSV."""

    def extract(self, path: str) -> str:
        print(f"  [CSV] Extrayendo de '{path}'")
        return "nombre,edad,ciudad\nAna,30,CDMX\nLuis,25,GDL\nMaria,28,MTY"

    def parse(self, raw_data: str) -> list[str]:
        lines = raw_data.strip().split("\n")
        print(f"  [CSV] Parseando {len(lines)} líneas")
        return lines[1:]  # Saltar header


class JSONDataMiner(DataMiner):
    """Subclase: mina datos de archivos JSON."""

    def extract(self, path: str) -> str:
        print(f"  [JSON] Extrayendo de '{path}'")
        return '[{"name":"Ana"},{"name":"Luis"},{"name":"Maria"},{"name":"Pedro"}]'

    def parse(self, raw_data: str) -> list[str]:
        # Simulación simple de parse
        items = raw_data.strip("[]").split("},")
        print(f"  [JSON] Parseando {len(items)} objetos")
        return [item.strip() for item in items]

    def hook_before_report(self, analysis: dict) -> None:
        """Hook sobreescrito: validación extra para JSON."""
        print("  [JSON] Hook: validando estructura de datos...")


if __name__ == "__main__":
    print("--- Template Method: DataMiner ---\n")

    print("= CSV Mining =")
    csv_miner = CSVDataMiner()
    csv_miner.mine("datos.csv")

    print("\n= JSON Mining =")
    json_miner = JSONDataMiner()
    json_miner.mine("datos.json")
