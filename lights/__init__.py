import dataclasses

@dataclasses.dataclass
class LightState:
    on: bool = False
    reachable: bool = False

@dataclasses.dataclass
class Light:
    id: int
    name: str = ""
    state: LightState = dataclasses.field(default_factory=LightState)
    modelid: str = ""
    uniqueid: str = ""
