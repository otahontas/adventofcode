#include "utils/utils.h"
#include <iostream>
#include <map>
#include <regex>

std::pair<int, int> SumPairs(std::pair<int, int> a, std::pair<int, int> b) {
  return std::make_pair(a.first + b.first, a.second + b.second);
}

const std::map<std::string, std::pair<int, int>> directions = {
    {"U", std::make_pair(0, -1)},
    {"R", std::make_pair(1, 0)},
    {"D", std::make_pair(0, 1)},
    {"L", std::make_pair(-1, 0)}};

std::map<std::pair<int, int>, int>
Intersection(const std::map<std::pair<int, int>, int> &first_map,
             const std::map<std::pair<int, int>, int> &second_map) {
  std::map<std::pair<int, int>, int> intersection;
  for (auto &it : first_map) {
    std::pair<int, int> point = it.first;
    if (second_map.count(point) != 0) {
      intersection[point] = it.second + second_map.at(point);
    }
  }
  return intersection;
}
std::map<std::pair<int, int>, int>
CollectVisitedPoints(std::string &wire_path) {
  std::regex extractor("\\w\\d+");
  std::map<std::pair<int, int>, int> visited;
  std::pair<int, int> point;
  int steps = 0;
  auto start =
      std::sregex_iterator(wire_path.begin(), wire_path.end(), extractor);
  auto end = std::sregex_iterator();
  for (auto iter = start; iter != end; iter++) {
    std::string direction = iter->str().substr(0, 1);
    int distance = stoi(iter->str().substr(1));
    for (int i = 1; i <= distance; i++) {
      point = SumPairs(point, directions.at(direction));
      steps++;
      if (visited.count(point) == 0) {
        visited[point] = steps;
      }
    }
  }
  return visited;
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("03");
  auto intersection = Intersection(CollectVisitedPoints(input[0]),
                                   CollectVisitedPoints(input[1]));
  int ans1 = INT_MAX;
  int ans2 = INT_MAX;
  for (auto &it : intersection) {
    auto point = it.first;
    ans1 = std::min(ans1, abs(point.first) + abs(point.second));
    ans2 = std::min(ans2, it.second);
  }
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
