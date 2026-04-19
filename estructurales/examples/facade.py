"""
Facade — Ejemplo

Proporciona una interfaz simplificada a un subsistema complejo,
ocultando la complejidad interna.
"""


class VideoFile:
    """Subsistema: archivo de video."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.codec_type = filename.split(".")[-1]


class CodecFactory:
    """Subsistema: fábrica de codecs."""

    @staticmethod
    def extract(file: VideoFile) -> str:
        return f"codec-{file.codec_type}"


class BitrateReader:
    """Subsistema: lector de bitrate."""

    @staticmethod
    def read(filename: str, codec: str) -> str:
        return f"buffer({filename},{codec})"

    @staticmethod
    def convert(buffer: str, codec: str) -> str:
        return f"converted({buffer}->{codec})"


class AudioMixer:
    """Subsistema: mezclador de audio."""

    @staticmethod
    def fix(result: str) -> str:
        return f"audio_fixed({result})"


class VideoConverter:
    """Facade: interfaz simplificada para conversión de video."""

    def convert(self, filename: str, target_format: str) -> str:
        """Convierte un video a otro formato.

        Args:
            filename: nombre del archivo de entrada
            target_format: formato de salida deseado

        Returns:
            resultado de la conversión
        """
        file = VideoFile(filename)
        source_codec = CodecFactory.extract(file)
        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, target_format)
        result = AudioMixer.fix(result)
        return f"Archivo convertido: {filename} -> output.{target_format} [{result}]"


if __name__ == "__main__":
    print("--- Video Converter Facade ---")
    converter = VideoConverter()

    print(converter.convert("video_vacaciones.ogg", "mp4"))
    print(converter.convert("presentacion.avi", "webm"))
