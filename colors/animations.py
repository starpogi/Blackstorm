import dataclasses
import typing 

from colors.frames import ColorFrame

@dataclasses.dataclass
class ColorAnimation:
    rate_s: float
    frames: typing.List[ColorFrame] = dataclasses.field(default_factory=list)
    repeat: bool = False
