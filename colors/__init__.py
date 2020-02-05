import dataclasses
import typing

Increment = typing.TypeVar('Increment', int, float)

class ColorSpace:
    pass

@dataclasses.dataclass
class CIE(ColorSpace):
    x: float
    y: float
    colormode: str = "xy"

@dataclasses.dataclass
class HueSaturation(ColorSpace):
    hue: int
    saturation: int
    colormode: str = "hs"

@dataclasses.dataclass
class ColorTemperature(ColorSpace):
    temperature: int
    colormode: str = "ct"
