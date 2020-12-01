from collections import Counter
import json
import math


class Moon:
    def __init__(self, inp):
        inp = inp[1:-1]
        x, y, z = inp.split(", ")
        self.pos = {
            "x": int(x.split("=")[1]),
            "y": int(y.split("=")[1]),
            "z": int(z.split("=")[1]),
        }
        self.vel = {"x": 0, "y": 0, "z": 0}

    def calc_vel_change(self, other_moon):
        for axis in other_moon.pos:
            if self.pos[axis] < other_moon.pos[axis]:
                self.vel[axis] += 1
            elif self.pos[axis] > other_moon.pos[axis]:
                self.vel[axis] -= 1

    def apply_velocity(self):
        c = Counter()
        c.update(self.pos)
        c.update(self.vel)
        self.pos = dict(c)

    def calc_potential(self):
        return sum((abs(value) for value in self.pos.values()))

    def calc_kinetic(self):
        return sum((abs(value) for value in self.vel.values()))

    def calc_total(self):
        return self.calc_potential() * self.calc_kinetic()


moons = [Moon(line) for line in open("inputs/d12.txt").read().splitlines()]


def calc_one_step(moons):

    for moon in moons:
        for other_moon in moons:
            if other_moon is moon:
                continue
            moon.calc_vel_change(other_moon)

    for moon in moons:
        moon.apply_velocity()

    return moons

def first(moons):
    for _ in range(1000):
        moons = calc_one_step(moons)

    print(sum(moon.calc_total() for moon in moons))


def second(moons):
    hist_x = {}
    hist_y = {}
    hist_z = {}
    steps = 0
    x_steps = 0
    y_steps = 0
    z_steps = 0

    # simulate and if axis pos & vel seen, count the diff between this and last time
    while True:
        moons = calc_one_step(moons)
        steps += 1

        if x_steps == 0:
            x = tuple(
                [*[moon.pos["x"] for moon in moons], *[moon.vel["x"] for moon in moons]]
            )
            if x in hist_x:
                x_steps = steps - hist_x[x]
            else:
                hist_x[x] = steps

        if y_steps == 0:
            y = tuple(
                [*[moon.pos["y"] for moon in moons], *[moon.vel["y"] for moon in moons]]
            )
            if y in hist_y:
                y_steps = steps - hist_y[y]
            else:
                hist_y[y] = steps

        if z_steps == 0:
            z = tuple(
                [*[moon.pos["z"] for moon in moons], *[moon.vel["z"] for moon in moons]]
            )
            if z in hist_z:
                z_steps = steps - hist_z[z]
            else:
                hist_z[z] = steps

        if x_steps != 0 and y_steps != 0 and z_steps != 0:
            break
    # Count least common multiple
    tmp = int((abs(x_steps * y_steps) / math.gcd(x_steps, y_steps)))
    res = int((abs(tmp * z_steps) / math.gcd(tmp, z_steps)))
    print(res)

first(moons)
second(moons)
