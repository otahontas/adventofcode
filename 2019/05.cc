#include "int_code_comp/int_code_comp.h"
#include "utils/utils.h"
#include <iostream>
#include <vector>

long long GetDiagnosticCode(std::vector<long long> &tape, int initial_input) {
  int_code_comp::IntCodeComp comp(tape);
  comp.AddInput(initial_input);
  comp.Run();
  long long output = 0;
  while (output == 0) {
    output = comp.GetOutput();
  }
  return output;
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("05");
  auto tape = utils::ExtractNumbers<long long>(input[0]);
  int ans1 = GetDiagnosticCode(tape, 1);
  int ans2 = GetDiagnosticCode(tape, 5);
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
