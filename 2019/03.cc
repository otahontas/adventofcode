#include "data_structures/complex.h"
#include "utils/utils.h"
#include <complex>
#include <iostream>
#include <map>
#include <regex>

typedef std::map<complex::Complex<int>, int> PointMap;

const std::map<std::string, complex::Complex<int>> directions = {
    {"U", {0, -1}}, {"R", {1, 0}}, {"D", {0, 1}}, {"L", {-1, 0}}};

PointMap GetIntersections(const PointMap &a, const PointMap &b) {
  PointMap intersection;
  for (const auto &[point, steps] : a) {
    if (b.count(point) != 0) {
      intersection[point] = steps + b.at(point);
    }
  }
  return intersection;
}

PointMap CollectVisitedPoints(const std::string &path) {
  std::regex extractor("\\w\\d+");
  PointMap visited;
  complex::Complex<int> point(0, 0);
  int steps = 0;
  auto start = std::sregex_iterator(path.begin(), path.end(), extractor);
  auto end = std::sregex_iterator();
  for (auto iter = start; iter != end; ++iter) {
    std::string direction = iter->str().substr(0, 1);
    int distance = stoi(iter->str().substr(1));
    for (int i = 1; i <= distance; ++i) {
      point += directions.at(direction);
      ++steps;
      if (visited.count(point) == 0) {
        visited[point] = steps;
      }
    }
  }
  return visited;
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("03");
  auto intersections = GetIntersections(CollectVisitedPoints(input[0]),
                                        CollectVisitedPoints(input[1]));
  int ans1 = INT_MAX;
  int ans2 = INT_MAX;
  for (const auto &[point, steps] : intersections) {
    ans1 = std::min(ans1, abs(point.real()) + abs(point.imag()));
    ans2 = std::min(ans2, steps);
  }
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
