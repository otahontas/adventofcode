#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
#include "aoc.h"

// Go through possible permutations, get feedbacks and report highest of them.
long long GetLargestOutputWithoutFeedback(std::vector<long long>& puzzle_input) {
    int base[] = {0, 1, 2, 3, 4};
    std::sort(base, base + 5);
    long long max_signal = 0;

    do {
        long long signal = 0;
        for (int phase_setting : base) {
            aoc::IntCodeComp comp(puzzle_input);
            comp.AddInput(phase_setting);
            comp.AddInput(signal);
            comp.Run();
            signal = comp.GetOutput();
        }
        max_signal = std::max(max_signal, signal);
    } while(std::next_permutation(base, base + 5));
    return max_signal;
}

// Go through possible permutations, loop computers until they all halt in order, get
// feedbacks and report highest of them.
long long GetLargestOutputWithFeedback(std::vector<long long>& puzzle_input) {
    int base[] = {5, 6, 7, 8, 9};
    std::sort(base, base + 5);
    long long max_signal = 0;

    do {
        std::vector<aoc::IntCodeComp> comps;
        for (int phase_setting : base) {
            aoc::IntCodeComp comp(puzzle_input);
            comp.AddInput(phase_setting);
            comps.push_back(comp);
        }
        long long signal = 0;
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
    std::vector<long long> example = { 3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0 };
    assert(GetLargestOutputWithoutFeedback(example) == 43210);
    std::vector<long long> second_example = { 3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,
                                              26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,
                                              5,3,15,3,16,1002,16,10,16,1,16,15,15,4,15,
                                              99,0,0,5 };
    assert(GetLargestOutputWithFeedback(second_example) == 139629729);
}

void Solve() {
    std::vector<long long> puzzle_input = aoc::ReadInputToLongs(7);
    std::cout << aoc::Solution(GetLargestOutputWithoutFeedback(puzzle_input),
                               GetLargestOutputWithFeedback(puzzle_input));
}

int main() {
    Test();
    Solve();
}
