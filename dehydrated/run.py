import re
import subprocess
from .error import catch_error
from .modules import HydraBaseSettings

HYDRA_EXECUTABLE = "hydra"
HYDRA_SUCESS_BRUTEFORCE_REGEX = re.compile(
    r"\[(?P<port>[^\]]+)\]\[(?P<module>[^\]]+)\] host: (?P<host>[^\s]+)\s+login: (?P<login>[^\s]+)\s+password: (?P<passwd>[^\n]+)",
    re.I,
)


def collect_data(process_output: str):
    output = process_output.split("\n")
    return list(
        map(
            lambda m: m.groupdict(),
            map(
                HYDRA_SUCESS_BRUTEFORCE_REGEX.search,
                filter(HYDRA_SUCESS_BRUTEFORCE_REGEX.match, output),
            ),
        )
    )


def run_hydra(settings: HydraBaseSettings):
    arguments = [HYDRA_EXECUTABLE]

    if issubclass(settings.__class__, HydraBaseSettings):
        arguments.extend(settings.args)
    else:
        raise ValueError("Incorrect settings, should be subclass of 'HydraBaseSettings'.")

    string_arguments = list(map(str, arguments))

    r = subprocess.run(string_arguments, capture_output=True)

    if error := catch_error(r.stderr.decode()):
        raise error[0](error[1])

    if data := collect_data(r.stdout.decode()):
        return data
