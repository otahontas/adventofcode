import re

instructions = re.findall(r"(\D{1})(\d+)", open("inputs/d12.txt").read())

directions = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}


def multiply_by_scalar(point, scalar):
    return tuple(axis * scalar for axis in point)


def move_by_vector(point, vector):
    return tuple(map(sum, zip(point, vector)))


def first():
    point = (0, 0)
    facing_to = "E"
    for action, value in instructions:
        value = int(value)
        if action in "NESW":
            point = move_by_vector(point, multiply_by_scalar(directions[action], value))
        elif action in "LR":
            direction_list = list(directions.keys())
            turn = value // 90 if action == "R" else -value // 90
            facing_to = direction_list[(direction_list.index(facing_to) + turn) % 4]
        else:
            point = move_by_vector(
                point, multiply_by_scalar(directions[facing_to], value)
            )
    print(sum(abs(axis) for axis in point))


def second():
    waypoint = (10, 1)
    point = (0, 0)
    turns = {
        1: lambda x, y: (y, -x),
        2: lambda x, y: (-x, -y),
        3: lambda x, y: (-y, x),
    }
    for action, value in instructions:
        value = int(value)
        if action in "NESW":
            waypoint = move_by_vector(
                waypoint, multiply_by_scalar(directions[action], value)
            )
        elif action in "LR":
            value = (value // 90) % 4 if action == "R" else abs((value // 90) % 4 - 4)
            x, y = waypoint
            waypoint = turns[value](x, y)
        else:
            point = move_by_vector(point, multiply_by_scalar(waypoint, value))
    print(sum(abs(axis) for axis in point))


first()
second()
