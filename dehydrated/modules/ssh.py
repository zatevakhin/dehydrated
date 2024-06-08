from pydantic import Field
from .base import HydraBaseSettings


class Ssh(HydraBaseSettings):
    service: str = Field(init=False, default="ssh")

    @property
    def args(self):
        return [*super().args, self.service]
