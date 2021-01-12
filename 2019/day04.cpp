#include <cassert>
#include <iostream>
#include <regex>
#include "aoc.h"
#include <map>
#include <algorithm>

bool Validate(int num, bool only_allow_two_adj=false) {
    std::string pwd = std::to_string(num);
    std::string pwd_sorted = pwd;
    sort(pwd_sorted.begin(), pwd_sorted.end());
    if (pwd != pwd_sorted) return false;
    int n = pwd.size();
    for (int i = 0; i < n - 1; i++) {
        if (pwd[i] == pwd[i+1]) {
            if (!only_allow_two_adj) return true;
            if ((i == 0 || pwd[i] != pwd[i-1]) &&
                (i == n-2 || pwd[i] != pwd[i+2])) return true;
        }
    }
    return false;
}

void Test() {
    assert(Validate(111111) == true);
    assert(Validate(223450) == false);
    assert(Validate(123789) == false);

    assert(Validate(112233, true) == true);
    assert(Validate(123444, true) == false);
    assert(Validate(111122, true) == true);
}

void Solve() {
    std::vector<int> num_range = aoc::StringToInts(aoc::ReadInputToLine(4));
    aoc::Solution solution;
    for (int i = num_range[0]; i <= num_range[1]; i++) {
        solution.part_one += Validate(i);
        solution.part_two += Validate(i, true);
    }
    std::cout << solution;
}

int main() {
    Test();
    Solve();
}
