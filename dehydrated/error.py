import re

HYDRA_ERROR_REGEX = re.compile(r"(\[ERROR\])", re.I)


def catch_error(process_output: str):
    output = process_output.split("\n")

    for error in filter(HYDRA_ERROR_REGEX.match, output):
        return (RuntimeError, error)
