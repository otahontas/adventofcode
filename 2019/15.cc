#include "data_structures/complex.h"
#include "int_code_comp/int_code_comp.h"
#include "utils/utils.h"
#include <iostream>
#include <map>
#include <queue>
#include <set>

const std::map<int, complex::Complex<int>> directions = {
    {1, complex::Complex<int>(0, -1)},
    {4, complex::Complex<int>(1, 0)},
    {2, complex::Complex<int>(0, 1)},
    {3, complex::Complex<int>(-1, 0)}};

std::tuple<std::set<complex::Complex<int>>, complex::Complex<int>, int>
GetCoordinates(std::vector<long long> &tape) {
  std::set<complex::Complex<int>> open_locations;
  complex::Complex<int> oxygen_system_location(0, 0);
  int steps_to_find_oxygen_system = 0;

  // run bfs, copy the comps since they're stateful
  std::queue<std::tuple<complex::Complex<int>, int_code_comp::IntCodeComp, int>>
      q;
  q.push({complex::Complex<int>(0, 0), int_code_comp::IntCodeComp(tape), 0});
  while (!q.empty()) {
    auto [point, comp, steps] = q.front();
    q.pop();
    if (open_locations.count(point)) {
      continue;
    }
    open_locations.insert(point);
    for (auto [direction, direction_vector] : directions) {
      complex::Complex<int> new_point(point.real(), point.imag());
      new_point += direction_vector;
      auto new_comp = comp;
      new_comp.AddInput(direction);
      new_comp.Run();
      auto output = new_comp.GetOutput();
      if (output == 0) {
        continue;
      }
      if (output == 2) {
        oxygen_system_location = new_point;
        steps_to_find_oxygen_system = steps + 1;
      }
      q.push({new_point, new_comp, steps + 1});
    }
  }
  return {open_locations, oxygen_system_location, steps_to_find_oxygen_system};
}

int GetMinutesToFillWithOxygen(std::set<complex::Complex<int>> &open_locations,
                               complex::Complex<int> oxygen_system_location) {
  // just a basic game of life simulation
  int minutes = 0;
  std::set<complex::Complex<int>> filled = {oxygen_system_location};
  while (filled.size() < open_locations.size()) {
    std::set<complex::Complex<int>> new_filled;
    for (auto &point : filled) {
      for (auto [_, direction_vector] : directions) {
        complex::Complex<int> new_point(point.real(), point.imag());
        new_point += direction_vector;
        if (open_locations.count(new_point)) {
          new_filled.insert(new_point);
        }
      }
    }
    filled.insert(new_filled.begin(), new_filled.end());
    minutes++;
  }
  return minutes;
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("15");
  auto tape = utils::ExtractNumbers<long long>(input[0]);
  auto [open_locations, oxygen_system_location, ans1] = GetCoordinates(tape);
  int ans2 = GetMinutesToFillWithOxygen(open_locations, oxygen_system_location);
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
