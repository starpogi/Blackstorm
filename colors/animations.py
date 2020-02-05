import dataclasses
import typing 

from colors import ColorSpace

@dataclasses.dataclass
class ColorAnimation:
    rate_s: float
    frames: typing.List[ColorSpace] = dataclasses.field(default_factory=list)
    repeat: bool = False
