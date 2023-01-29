from dataclasses import dataclass, field
from .base import HydraShotSettings, HydraBurstSettings


@dataclass
class SshBase:
    service: str = field(init=False, default="ssh")

    @property
    def args(self):
        return [*super().args, self.service]


@dataclass
class SshShot(SshBase, HydraShotSettings):
    pass


@dataclass
class SshBurst(SshBase, HydraBurstSettings):
    pass
