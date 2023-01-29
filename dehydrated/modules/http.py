from dataclasses import dataclass, field
from .base import HydraShotSettings, HydraBurstSettings


@dataclass
class HttpHeadBase:
    service: str = field(init=False, default="http-head")
    path: str = field(default=None)

    @property
    def args(self):
        return [*super().args, self.service, self.path]


@dataclass
class HttpHeadShot(HttpHeadBase, HydraShotSettings):
    pass


@dataclass
class HttpHeadBurst(HttpHeadBase, HydraBurstSettings):
    pass


@dataclass
class HttpGetBase:
    service: str = field(init=False, default="http-get")
    path: str = field(default=None)
    auth: str = field(default=None)
    header: str = field(default=None)
    check: str = field(default=None)

    @property
    def args(self):
        args = []
        if self.auth is not None:
            args.append(f":A={self.auth}")
        if self.header is not None:
            args.append(f":H={self.header}")
        if self.check is not None:
            args.append(f":F={self.check}")

        args = "".join(args)
        return [*super().args, self.service, f"{self.path}{args}"]


@dataclass
class HttpGetShot(HttpGetBase, HydraShotSettings):
    pass


@dataclass
class HttpGetBurst(HttpGetBase, HydraBurstSettings):
    pass


@dataclass
class HttpPostBase:
    service: str = field(init=False, default="http-post")
    path: str = field(default=None)
    auth: str = field(default=None)
    header: str = field(default=None)
    check: str = field(default=None)

    @property
    def args(self):
        args = []
        if self.auth is not None:
            args.append(f":A={self.auth}")
        if self.header is not None:
            args.append(f":H={self.header}")
        if self.check is not None:
            args.append(f":F={self.check}")

        args = "".join(args)
        return [*super().args, self.service, f"{self.path}{args}"]


@dataclass
class HttpPostShot(HttpPostBase, HydraShotSettings):
    pass


@dataclass
class HttpPostBurst(HttpPostBase, HydraBurstSettings):
    pass
