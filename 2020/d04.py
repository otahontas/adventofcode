import re

passports = [line.strip() for line in open("inputs/d04.txt").read().split("\n\n")]


def is_valid(fields):
    valid_count = 0
    check = {
        "byr": lambda val: 1920 <= int(val) <= 2002,
        "iyr": lambda val: 2010 <= int(val) <= 2020,
        "eyr": lambda val: 2020 <= int(val) <= 2030,
        "hgt": lambda val: (
            val[-2:] == "cm"
            and 150 <= int(val[:-2]) <= 193
            or val[-2:] == "in"
            and 59 <= int(val[:-2]) <= 76
        ),
        "hcl": lambda val: bool(re.fullmatch(r"^#[0-9a-f]{6}$", val)),
        "ecl": lambda val: val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda val: bool(re.fullmatch(r"^[0-9]{9}$", val)),
    }
    for id, val in fields:
        if id == "cid":
            continue
        if check[id](val):
            valid_count += 1
    return valid_count == 7


ans1 = 0
ans2 = 0
for passport in passports:
    fields = re.findall(r"(\w+):(\S+)", passport)
    valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(x in [y[0] for y in fields] for x in valid_fields):
        ans1 += 1
        if is_valid(fields):
            ans2 += 1
print(ans1)
print(ans2)
