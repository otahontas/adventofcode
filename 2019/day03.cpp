#include <cassert>
#include <iostream>
#include <map>
#include <regex>
#include "aoc.h"
#include "dsalgos.h"

typedef std::map<dsalgos::Point, int> PointMap;


// Return all points that are in both maps with their step values combined.
PointMap Intersection(PointMap first_map,  PointMap second_map) {
    PointMap intersection;
    for (auto it = first_map.begin(); it != first_map.end(); it++) {
        dsalgos::Point point = it->first;
        if (second_map.count(point) != 0) {
            intersection[point] = it->second + second_map[point];
        }
    }
    return intersection;
}


// Collect each visited point with steps taken from (0,0) into a map.
PointMap CollectVisitedPoints(std::string &wire_path) {
    std::regex extractor("\\w\\d+");
    PointMap visited;
    dsalgos::Point point;
    int steps = 0;
    auto start = std::sregex_iterator(wire_path.begin(), wire_path.end(), extractor);
    auto end = std::sregex_iterator();
    for (auto iter = start; iter != end; iter++) {
        std::string direction = iter->str().substr(0,1);
        int distance = stoi(iter->str().substr(1));
        for (int i = 1; i <= distance; i++) {
            point += dsalgos::kDirections.at(direction);
            steps++;
            if (visited.count(point) == 0) {
                visited[point] = steps;
            }
        }
    }
    return visited;
}

// Get points where wires intersect, then find point with lowest manhattan distance
// to (0,0) and point reached with lowest number of steps.
aoc::Solution SolveParts(std::vector<std::string> lines) {
    PointMap intersection = Intersection(
            CollectVisitedPoints(lines[0]),
            CollectVisitedPoints(lines[1])
    );
    aoc::Solution solution;
    solution.part_one = INT_MAX;
    solution.part_two = INT_MAX;
    for (auto it = intersection.begin(); it != intersection.end(); it++) {
        auto point = it->first;
        solution.part_one = std::min(solution.part_one, abs(point.x) + abs(point.y));
        solution.part_two = std::min(solution.part_two, it->second);
    }
    return solution;
}

void Test() {
    std::vector<std::string> example = {
        "R75,D30,R83,U83,L12,D49,R71,U7,L72",
        "U62,R66,U55,R34,D71,R55,D58,R83"
    };
    aoc::Solution solution = SolveParts(example);
    assert(solution.part_one == 159);
    assert(solution.part_two == 610);
}

void Solve() {
    std::cout << SolveParts(aoc::ReadInputToLines(3));
}

int main() {
    Test();
    Solve();
}
