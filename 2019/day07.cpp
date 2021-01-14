#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
#include "aoc.h"

// Go through possible permutations, get feedbacks and report highest of them.
int GetLargestOutputWithoutFeedback(std::vector<int> &puzzle_input) {
    int base[] = {0, 1, 2, 3, 4};
    std::sort(base, base + 5);
    int max_signal = 0;

    do {
        int signal = 0;
        for (int i = 0; i < 5; i++) {
            aoc::IntCodeComp comp(puzzle_input);
            comp.AddInput(base[i]);
            comp.AddInput(signal);
            comp.Run();
            signal = comp.GetOutput();
        }
        max_signal = std::max(max_signal, signal);
    } while(std::next_permutation(base, base + 5));
    return max_signal;
}

// Go through possible permutations, loop computers until they halt, get feedbacks and report highest of them.
int GetLargestOutputWithFeedback(std::vector<int> &puzzle_input) {
    int base[] = {5, 6, 7, 8, 9};
    std::sort(base, base + 5);
    int max_signal = 0;

    do {
        std::vector<aoc::IntCodeComp> comps;
        for (int i = 0; i < 5; i++) {
            aoc::IntCodeComp comp(puzzle_input);
            comp.AddInput(base[i]);
            comps.push_back(comp);
        }
        int signal = 0;
        while (!comps[4].IsHalted()) {
            for (int i = 0; i < 5; i++) {
                comps[i].AddInput(signal);
                comps[i].Run();
                signal = comps[i].GetOutput();
            }
        }
        max_signal = std::max(max_signal, signal);
    } while(std::next_permutation(base, base + 5));
    return max_signal;
}


void Test() {
    std::vector<int> example = {3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0};
    assert(GetLargestOutputWithoutFeedback(example) == 43210);
    std::vector<int> second_example = {3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,
                                       4,27,1001,28,-1,28,1005,28,6,99,0,0,5, 3,15,3,
                                       16,1002,16,10,16,1,16,15,15,4,15,99,0,0,5};
    assert(GetLargestOutputWithFeedback(second_example) == 139629729);
}

void Solve() {
    std::vector<int> puzzle_input = aoc::ReadInputToInts(7);
    aoc::Solution solution;
    solution.part_one = GetLargestOutputWithoutFeedback(puzzle_input);
    solution.part_two = GetLargestOutputWithFeedback(puzzle_input);
    std::cout << solution;
}

int main() {
    Test();
    Solve();
}
