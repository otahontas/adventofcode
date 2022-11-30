# boiler
import itertools, functools
import math
import re
from collections import Counter, defaultdict, deque

# re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)") regex example


lines = list(open("inputs/d01.txt").readlines())
# nums = [int(x) for x in open("inputs/d13.txt").read().split(",")] # splitted by ,
# lines = list(open("inputs/d01.txt").read().split("\n\n")) # doubleline split


def neighbours(point: complex):
    # dirs = [complex(1,0), complex(-1,0), complex(0,1), complex(0, -1)] # 4, simple
    dirs = [
        complex(x, y)
        for x, y in itertools.product((-1, 0, 1), repeat=2)
        if (x, y) != (0, 0)
    ]
    return [point + d for d in dirs]
