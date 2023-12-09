import re


def lines(day: str, delim: str = "\n") -> list[str]:
    with open(f"inputs/{day}") as f:
        return [line.strip() for line in f.read().strip().split(delim)]


def ints(s: str) -> list[int]:
    return [int(x) for x in re.findall(r"-*\d+", s)]
