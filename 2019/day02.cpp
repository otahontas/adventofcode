#include <cassert>
#include <iostream>
#include "aoc.h"

// Replace input at positions, report value at position 0.
int ReportValueForPartOne(std::vector<int> tape) {
    tape[1] = 12;
    tape[2] = 2;
    aoc::IntCodeComp comp(tape);
    comp.Run();
    return comp.ValueAtAddress(0);
}

// Try every possible combination for noun and verb in range 0-99 to find match
// against goal value.
int FindValueThatProduceGoal(std::vector<int> tape) {
    int goal = 19690720;
    for (int i = 0; i <= 99; i++) {
        for (int j = 0; j <= 99; j++) {
            tape[1] = i;
            tape[2] = j;
            aoc::IntCodeComp comp(tape);
            comp.Run();
            if (comp.ValueAtAddress(0) == goal) {
                return 100 * i + j;
            }
        }
    }
    std::cout << "Not able to find values that produce" << goal << "\n";
    return 0;
}

void Test() {
    std::vector<int> example = { 1,9,10,3,2,3,11,0,99,30,40,50 };
    aoc::IntCodeComp comp(example);
    comp.Run();
    assert(comp.ValueAtAddress(0) == 3500);
}

void Solve() {
    std::vector<int> puzzle_input = aoc::ReadInputToInts(2);
    aoc::Solution solution;

    solution.part_one = ReportValueForPartOne(puzzle_input);
    solution.part_two = FindValueThatProduceGoal(puzzle_input);
    std::cout << solution;
}

int main() {
    Test();
    Solve();
}
