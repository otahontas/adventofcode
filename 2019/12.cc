#include "utils/utils.h"
#include <algorithm>
#include <functional>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>

void SimulateGravity(
    std::vector<std::pair<std::vector<int>, std::vector<int>>> &moons) {
  for (int i = 0; i < moons.size() - 1; i++) {
    for (int j = i + 1; j < moons.size(); j++) {
      for (int axis = 0; axis < 3; axis++) {
        if (moons[i].first[axis] < moons[j].first[axis]) {
          moons[i].second[axis]++;
          moons[j].second[axis]--;
        } else if (moons[i].first[axis] > moons[j].first[axis]) {
          moons[i].second[axis]--;
          moons[j].second[axis]++;
        }
      }
    }
  }
}

void SimulateVelocity(
    std::vector<std::pair<std::vector<int>, std::vector<int>>> &moons) {
  for (auto &moon : moons) {
    std::transform(moon.first.begin(), moon.first.end(), moon.second.begin(),
                   moon.first.begin(), std::plus<int>());
  }
}

int SumOfAbsoluteValues(const std::vector<int> &vec) {
  return std::accumulate(vec.begin(), vec.end(), 0,
                         [](int acc, int val) { return acc + std::abs(val); });
}

int CalculateEnergy(std::pair<std::vector<int>, std::vector<int>> &moon) {
  return SumOfAbsoluteValues(moon.first) * SumOfAbsoluteValues(moon.second);
}

int SimulateAndGetEnergy(
    std::vector<std::pair<std::vector<int>, std::vector<int>>> &moons,
    int steps) {
  for (int i = 0; i < steps; i++) {
    SimulateGravity(moons);
    SimulateVelocity(moons);
  }
  return std::accumulate(
      moons.begin(), moons.end(), 0,
      [](int acc, auto &moon) { return acc + CalculateEnergy(moon); });
}

long long SafeLCM(long long a, long long b) {
  return std::abs(a) * (std::abs(b) / std::gcd(a, b));
}

long long GetLCMForVector(std::vector<long long> &numbers) {
  return std::accumulate(numbers.begin(), numbers.end(), 1LL, SafeLCM);
}

std::vector<int>
GetAxisState(std::vector<std::pair<std::vector<int>, std::vector<int>>> &moons,
             int axis) {
  std::vector<int> axis_state;
  for (auto &moon : moons) {
    axis_state.push_back(moon.first[axis]);
    axis_state.push_back(moon.second[axis]);
  }
  return axis_state;
}

long long SimulateUntilSameState(
    std::vector<std::pair<std::vector<int>, std::vector<int>>> &moons) {
  std::vector<std::set<std::vector<int>>> axis_states;
  for (int axis = 0; axis < 3; axis++) {
    axis_states.push_back({GetAxisState(moons, axis)});
  }

  std::vector<long long> steps_until_repeat = {0, 0, 0};
  long long steps = 0;
  while (true) {
    SimulateGravity(moons);
    SimulateVelocity(moons);
    steps++;

    // optimization: if we have found the repeat for all axes,
    // we can just return the LCM of the steps. There the whole system
    // is back in its original state
    bool all_repeated = true;
    for (int axis = 0; axis < 3; axis++) {
      if (steps_until_repeat[axis] != 0) {
        continue;
      }
      if (axis_states[axis].count(GetAxisState(moons, axis))) {
        steps_until_repeat[axis] = steps;
      } else {
        all_repeated = false;
        axis_states[axis].insert(GetAxisState(moons, axis));
      }
    }

    if (all_repeated) {
      return GetLCMForVector(steps_until_repeat);
    }
  }
  return 0;
}

int main() {
  auto lines = utils::ReadInputAndSplitByDelimiter("12");
  std::vector<std::pair<std::vector<int>, std::vector<int>>> moons;
  for (auto &line : lines) {
    moons.push_back({utils::ExtractNumbers(line), {0, 0, 0}});
  }
  int ans1 = SimulateAndGetEnergy(moons, 1000);
  long long ans2 = SimulateUntilSameState(moons);
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
