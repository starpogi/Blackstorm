import dataclasses

from colors import ColorSpace
from lights import Light

@dataclasses.dataclass
class ColorFrame:
    color: ColorSpace = dataclasses.field(default_factory=ColorSpace)
    light: Light = dataclasses.field(default_factory=Light)
