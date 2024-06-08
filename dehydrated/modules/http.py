from pydantic import Field
from .base import HydraBaseSettings
from functools import partial


class HttpHeadBase(HydraBaseSettings):
    service: str = Field(default=None)
    path: str = Field(default=None)

    @property
    def args(self):
        return [*super().args, self.service, self.path]


HttpHead = partial(HttpHeadBase, service="http-head")
HttpsHead = partial(HttpHeadBase, service="https-head")


class HttpGetOrPost(HydraBaseSettings):
    service: str = Field(default=None)
    path: str = Field(default=None)
    auth: str = Field(default=None)
    header: str = Field(default=None)
    check: str = Field(default=None)

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


HttpGet = partial(HttpGetOrPost, service="http-get")
HttpPost = partial(HttpGetOrPost, service="http-post")

HttpsGet = partial(HttpGetOrPost, service="https-get")
HttpsPost = partial(HttpGetOrPost, service="https-post")
