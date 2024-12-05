#include "int_code_comp/int_code_comp.h"
#include "utils/utils.h"
#include <iostream>
#include <vector>

long long GetSignal(std::vector<long long> &tape, int initial_input) {
  int_code_comp::IntCodeComp comp(tape);
  comp.AddInput(initial_input);
  comp.Run();
  return comp.GetOutput();
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("09");
  auto tape = utils::ExtractNumbers<long long>(input[0]);
  long long ans1 = GetSignal(tape, 1);
  long long ans2 = GetSignal(tape, 2);
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
