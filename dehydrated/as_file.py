import uuid
import os


class TemporaryFile:
    def __init__(self) -> None:
        name = uuid.uuid4().hex
        self.file = open(f"/tmp/dehydrated_{name}", "w")

    @property
    def name(self):
        self.file.name

    def writelines(self, lines: list[str]):
        self.file.writelines(map(lambda l: f"{l}\n", lines))
        self.file.seek(0)

    def __repr__(self) -> str:
        return self.file.name

    def __str__(self) -> str:
        return self.file.name

    def __del__(self):
        path = self.file.name
        self.file.close()
        os.unlink(path)


def as_file(lines: list):
    fp = TemporaryFile()
    fp.writelines(lines)
    return fp
