#include "int_code_comp/int_code_comp.h"
#include "utils/utils.h"
#include <iostream>

long long RunTapeAndReportValue(std::vector<long long> &tape) {
  tape[1] = 12;
  tape[2] = 2;
  int_code_comp::IntCodeComp comp(tape);
  comp.Run();
  return comp.ValueAtAddress(0);
}

long long FindValuesThatProduceGoal(std::vector<long long> &tape) {
  int goal = 19690720;
  // just a guess that the values are found between 0 and 99
  for (int i = 0; i <= 99; i++) {
    for (int j = 0; j <= 99; j++) {
      tape[1] = i;
      tape[2] = j;
      int_code_comp::IntCodeComp comp(tape);
      comp.Run();
      if (comp.ValueAtAddress(0) == goal) {
        return 100 * i + j;
      }
    }
  }
  std::cout << "Not able to find values that produce" << goal << "\n";
  return 0;
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("02");
  auto tape = utils::ExtractNumbers<long long>(input[0]);
  int ans1 = RunTapeAndReportValue(tape);
  int ans2 = FindValuesThatProduceGoal(tape);
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
