#include "int_code_comp/int_code_comp.h"
#include "utils/utils.h"
#include <iostream>
#include <vector>

long long GetLargestOutputWithoutFeedback(std::vector<long long> &tape) {
  int base[] = {0, 1, 2, 3, 4};
  std::sort(base, base + 5);
  long long max_signal = 0;

  do {
    long long signal = 0;
    for (int phase_setting : base) {
      int_code_comp::IntCodeComp comp(tape);
      comp.AddInput(phase_setting);
      comp.AddInput(signal);
      comp.Run();
      signal = comp.GetOutput();
    }
    max_signal = std::max(max_signal, signal);
  } while (std::next_permutation(base, base + 5));
  return max_signal;
}

long long GetLargestOutputWithFeedback(std::vector<long long> &tape) {
  int base[] = {5, 6, 7, 8, 9};
  std::sort(base, base + 5);
  long long max_signal = 0;

  do {
    std::vector<int_code_comp::IntCodeComp> comps;
    for (int phase_setting : base) {
      int_code_comp::IntCodeComp comp(tape);
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
  } while (std::next_permutation(base, base + 5));
  return max_signal;
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("07");
  auto tape = utils::ExtractNumbers<long long>(input[0]);
  int ans1 = GetLargestOutputWithoutFeedback(tape);
  int ans2 = GetLargestOutputWithFeedback(tape);
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
