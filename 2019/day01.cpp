#include <cassert>
#include <iostream>
#include <vector>
#include "aoc.h"

// Calculate fuel requirement for mass.
int FuelRequirement(int mass) {
    return mass / 3 - 2;
}

// Calculate fuel requirement for mass, but with part two rules. Required fuel will be
// 0 when mass drops under 9.
int RecursiveFuelRequirement(int mass) {
    int sum = 0;
    while (mass >= 9) {
        mass = FuelRequirement(mass);
        sum += mass;
    }
    return sum;
}

void Test() {
    assert(FuelRequirement(12)==2);
    assert(FuelRequirement(14)==2);
    assert(FuelRequirement(1969)==654);
    assert(FuelRequirement(100756)==33583);

    assert(RecursiveFuelRequirement(14)==2);
    assert(RecursiveFuelRequirement(1969)==966);
    assert(RecursiveFuelRequirement(100756)==50346);
}

void Solve() {
    std::vector<int> numbers = aoc::ReadInputToInts(1);
    aoc::Solution solution;
    for (auto num: numbers) {
        solution.part_one += FuelRequirement(num);
        solution.part_two += RecursiveFuelRequirement(num);
    }
    std::cout << solution;
}

int main() {
    Test();
    Solve();
}
