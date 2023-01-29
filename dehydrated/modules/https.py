from dataclasses import dataclass, field
from .base import HydraShotSettings, HydraBurstSettings


@dataclass
class HttpsHeadBase:
    service: str = field(init=False, default="https-head")
    path: str = field(default=None)

    @property
    def args(self):
        return [*super().args, self.service, self.path]


@dataclass
class HttpsHeadShot(HttpsHeadBase, HydraShotSettings):
    pass


@dataclass
class HttpsHeadBurst(HttpsHeadBase, HydraBurstSettings):
    pass


@dataclass
class HttpsGetBase:
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
class HttpsGetShot(HttpsGetBase, HydraShotSettings):
    pass


@dataclass
class HttpsGetBurst(HttpsGetBase, HydraBurstSettings):
    pass


@dataclass
class HttpsPostBase:
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
class HttpsPostShot(HttpsPostBase, HydraShotSettings):
    pass


@dataclass
class HttpsPostBurst(HttpsGetBase, HydraBurstSettings):
    pass
