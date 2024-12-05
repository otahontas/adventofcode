#include "utils/utils.h"
#include <iostream>

int FuelRequirement(int mass) { return mass / 3 - 2; }

int RecursiveFuelRequirement(int mass) {
  int sum = 0;
  while (mass >= 9) {
    mass = FuelRequirement(mass);
    sum += mass;
  }
  return sum;
}

int main() {
  auto lines = utils::ReadInputAndSplitByDelimiter("01");
  int ans1 = 0;
  int ans2 = 0;
  for (auto line : lines) {
    auto numbers = utils::ExtractNumbers(line);
    auto num = numbers[0];
    ans1 += FuelRequirement(num);
    ans2 += RecursiveFuelRequirement(num);
  }
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
