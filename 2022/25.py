dec = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2,
}
enc = {
    0: "0",
    1: "1",
    2: "2",
    3: "=",
    4: "-",
}


def to_decimal(snafu):
    return sum(5**i * dec[c] for i, c in enumerate(reversed(snafu)))


def to_snafu(decimal):
    res = ""
    while decimal:
        res += enc[decimal % 5]
        if decimal > 2:  # offset
            decimal += 2
        decimal //= 5
    return "".join(list(reversed(res)))


lines = open("inputs/25.txt").read().splitlines()
print("ans1", to_snafu(sum(to_decimal(snafu) for snafu in lines)))
