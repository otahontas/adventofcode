import re
from aocd import data
from typing import Callable

Validator = Callable[[str], bool]


def has_valid_fields(
    fields: list[tuple[str, str]], validators: dict[str, Validator]
) -> bool:
    valid_amount = sum(
        validators[field_id](value) for field_id, value in fields if field_id != "cid"
    )
    return valid_amount == len(validators)


def main() -> None:
    first, second = 0, 0
    validators: dict[str, Validator] = {
        "byr": lambda v: 1920 <= int(v) <= 2002,
        "iyr": lambda v: 2010 <= int(v) <= 2020,
        "eyr": lambda v: 2020 <= int(v) <= 2030,
        "hgt": lambda v: (
            "cm" in v
            and 150 <= int(v[:-2]) <= 193
            or "in" in v
            and 59 <= int(v[:-2]) <= 76
        ),
        "hcl": lambda v: bool(re.fullmatch(r"^#[0-9a-f]{6}$", v)),
        "ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda v: bool(re.fullmatch(r"^[0-9]{9}$", v)),
    }

    for passport in data.split("\n\n"):
        fields = re.findall(r"(\w+):(\S+)", passport)
        field_ids = {field_id for field_id, _ in fields}
        if all(field_id in field_ids for field_id in validators):
            first += 1
            if has_valid_fields(fields=fields, validators=validators):
                second += 1
    print("Part 1:", first)
    print("Part 2:", second)


if __name__ == "__main__":
    main()
