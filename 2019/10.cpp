#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include "aoc.h"
#include "dsalgos.h"

typedef std::vector<std::string> AsteroidMap;

// Count seen asteroid from given point
int countSeenAsteroids(AsteroidMap& map, dsalgos::Point point) {
    int height = map.size();
    int width = map[0].size();
    int count = 0;
    std::set<dsalgos::Point> seen;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            if (y == point.y & x == point.x) continue;
            if (map[y][x] == '.') continue;
            if (seen.count(dsalgos::Point(x,y)) != 0) continue;


        }
    }
    return 0;
}

// Brute-force through map and for each point, find all points that can be seen
dsalgos::Point FindBestLocation(AsteroidMap& map) {
    int height = map.size();
    int width = map[0].size();
    dsalgos::Point best_location;
    int seen_in_best = 0;
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            int count = countSeenAsteroids(map, dsalgos::Point(x,y));
            if (count > seen_in_best) {
                seen_in_best = count;
                best_location.y = y;
                best_location.x = x;
            }
        }
    }
    return best_location;
}


void Test() {
    AsteroidMap first_test_map = { ".#..#", ".....", "#####", "....#", "...##" };
    assert((FindBestLocation(first_test_map) == dsalgos::Point(3, 4)));
}

void Solve() {
    std::vector<std::string> puzzle_input = aoc::ReadInputToLines(10);
}

int main() {
    Test();
    Solve();
}
