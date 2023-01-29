from dataclasses import dataclass, field
from ..as_file import as_file


@dataclass
class HydraBaseSettings:
    target: str = field(default=None)
    service_port: int = field(default=None)

    @property
    def args(self):
        args = [self.target]

        if self.service_port is not None:
            args.extend(["-s", str(self.service_port)])
        return args


@dataclass
class HydraShotSettings(HydraBaseSettings):
    login: str = field(default=None)
    password: str = field(default=None)

    @property
    def args(self):
        return [*super().args, "-l", self.login, "-p", self.password]


@dataclass
class HydraBurstSettings(HydraBaseSettings):
    logins: list[str] = field(default=None)
    passwords: list[str] = field(default=None)

    @property
    def args(self):
        return [*super().args, "-L", as_file(self.logins), "-P", as_file(self.passwords)]
