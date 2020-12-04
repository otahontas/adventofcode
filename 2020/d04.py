import collections
import math
import re

inp = open("inputs/d04.txt").read().split('\n\n')

def is_valid(fields):
    for id, val in fields:
        if id == "byr":
            if int(val) < 1920 or int(val) > 2002:
                return False
        elif id == "iyr":
            if int(val) < 2010 or int(val) > 2020:
                return False
        elif id == "eyr":
            if int(val) < 2020 or int(val) > 2030:
                return False
        elif id == "hgt":
            if "cm" in val:
                num, *_ = val.split("cm")
                num = int(num)
                if num < 150 or num > 193:
                    return False
            elif "in" in val:
                num, *_ = val.split("in")
                num = int(num)
                if num < 59 or num > 76:
                    return False
        elif id == "hcl":
            if not bool(re.fullmatch(r'#[0-9a-f]{6}', val)):
                return False
        elif id == "ecl":
            if val not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        elif id == "pid":
            if not bool(re.fullmatch(r'[0-9]{9}', val)):
                return False
    return True

ans_1 = 0
ans_2 = 0
for line in inp:
    fields = re.findall(r'(\w+):(\S+)', line)
    valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(x in [y[0] for y in fields] for x in valid_fields):
        ans_1 += 1
        if is_valid(fields):
            ans_2 += 1
print(ans_1)
print(ans_2)
