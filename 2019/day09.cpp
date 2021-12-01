#include <cassert>
#include <iostream>
#include <vector>
#include "aoc.h"


// Get signal (computer output) based on input
long long GetSignal(std::vector<long long>& puzzle_input, int initial_input) {
    aoc::IntCodeComp comp(puzzle_input);
    comp.AddInput(initial_input);
    comp.Run();
    return comp.GetOutput();
}

void Test() {
    std::vector<long long >example = { 109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,
                                       101,0,99 };
    std::vector<long long> digit_example = { 1102,34915192,34915192,7,4,7,99,0 };
    std::vector<long long> big_num_example = { 104,1125899906842624,99 };
    aoc::IntCodeComp comp(example);
    aoc::IntCodeComp digit_comp(digit_example);
    aoc::IntCodeComp big_num_comp(big_num_example);
    comp.Run();
    for (auto& num : example) {
        assert(comp.GetOutput() == num);
    }
    digit_comp.Run();
    assert(std::to_string(digit_comp.GetOutput()).length() == 16);
    big_num_comp.Run();
    assert(big_num_comp.GetOutput() == big_num_example[1]);
}

void Solve() {
    std::vector<long long> puzzle_input = aoc::ReadInputToLongs(9);
    std::cout << aoc::Solution(GetSignal(puzzle_input, 1),
                               GetSignal(puzzle_input, 2));
}

int main() {
    Test();
    Solve();
}
