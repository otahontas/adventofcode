from collections import defaultdict

Point = tuple[int, int]


class Lobby:
    _DIRECTIONS: dict[str, Point] = {
        "nw": (0, -1),
        "ne": (1, -1),
        "e": (1, 0),
        "se": (0, 1),
        "sw": (-1, 1),
        "w": (-1, 0)
    }

    def __init__(self, tiles_to_be_flipped: list[str]) -> None:
        self.black_tiles = self._get_first_black_tiles(tiles_to_be_flipped)

    def execute_daily_flipping(self, times_to_execute: int) -> None:
        for _ in range(times_to_execute):
            neighbours_of_current_tiles = {
                self._move_point_to_direction(point, direction) for point
                in self.black_tiles for direction in self._DIRECTIONS
            }
            potential_tiles = self.black_tiles.union(neighbours_of_current_tiles)
            amount_of_neighbours = {
                point: self._count_black_neighbour_tiles(point) for point in
                potential_tiles
            }
            self.black_tiles = {point for point in potential_tiles if
                                (point in self.black_tiles and 1 <=
                                 amount_of_neighbours[point] <= 2) or
                                (point not in self.black_tiles and
                                 amount_of_neighbours[point] == 2)
            }

    def _get_first_black_tiles(self, tiles_to_be_flipped: list[str]) -> set[Point]:
        toggles_per_point = defaultdict(int)
        for steps in tiles_to_be_flipped:
            i, point = 0, (0, 0)
            while i < len(steps):
                direction, step = (steps[i:i + 2], 2) if steps[i] in "sn" else (
                    steps[i], 1)
                point = self._move_point_to_direction(point, direction)
                i += step
            toggles_per_point[point] += 1
        return {point for point, toggle_amount in toggles_per_point.items()
                if toggle_amount % 2 == 1}

    def _count_black_neighbour_tiles(self, point: Point) -> int:
        return sum(self._move_point_to_direction(point, direction)
                   in self.black_tiles for direction in self._DIRECTIONS)

    def _move_point_to_direction(self, point: Point, direction: str) -> Point:
        return tuple(a + b for a,b in zip(point, self._DIRECTIONS[direction]))


    @property
    def amount_of_black_tiles(self) -> int:
        return len(self.black_tiles)


def main():
    lines = open("inputs/d24.txt").read().splitlines()
    lobby = Lobby(lines)
    print(lobby.amount_of_black_tiles)
    lobby.execute_daily_flipping(100)
    print(lobby.amount_of_black_tiles)


if __name__ == "__main__":
    main()
