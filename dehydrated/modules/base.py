from pydantic import BaseModel, Field
from typing import List
from ..as_file import as_file


class HydraBaseSettings(BaseModel):
    target: str = Field(default=None)
    service_port: int = Field(default=None)
    logins: List[str] = Field(default_factory=list)
    passwords: List[str] = Field(default_factory=list)

    @property
    def args(self):
        args = [self.target, "-L", as_file(self.logins), "-P", as_file(self.passwords)]

        if self.service_port is not None:
            args.extend(["-s", str(self.service_port)])

        return args
