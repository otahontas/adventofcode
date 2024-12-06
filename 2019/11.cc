#include "data_structures/complex.h"
#include "int_code_comp/int_code_comp.h"
#include "utils/utils.h"
#include <iostream>
#include <map>
#include <vector>

std::map<complex::Complex<int>, int>
GetPanelColours(std::vector<long long> &tape, int initial_input) {
  int_code_comp::IntCodeComp comp(tape);
  std::map<complex::Complex<int>, int> panel_colours;
  complex::Complex<int> direction(0, -1);
  complex::Complex<int> position(0, 0);

  comp.AddInput(initial_input);
  while (true) {
    if (comp.IsHalted()) {
      break;
    }
    comp.Run();
    int color_output = comp.GetOutput();
    panel_colours[position] = color_output;
    int direction_output = comp.GetOutput();
    auto direction_multiplier =
        direction_output ? complex::Complex<int>(0, 1)   // 90 degrees right
                         : complex::Complex<int>(0, -1); // 90 degrees left
    direction *= direction_multiplier;
    position += direction;
    int current_colour = panel_colours[position];
    comp.AddInput(current_colour);
  }
  return panel_colours;
}

void PrintPanel(std::map<complex::Complex<int>, int> panel_colours) {
  int min_x = INT_MAX;
  int min_y = INT_MAX;
  int max_x = INT_MIN;
  int max_y = INT_MIN;
  for (const auto &pair : panel_colours) {
    min_x = std::min(min_x, pair.first.real());
    min_y = std::min(min_y, pair.first.imag());
    max_x = std::max(max_x, pair.first.real());
    max_y = std::max(max_y, pair.first.imag());
  }
  for (int y = min_y; y <= max_y; y++) {
    for (int x = min_x; x <= max_x; x++) {
      char c = panel_colours[complex::Complex<int>(x, y)] == 1 ? '#' : ' ';
      std::cout << c;
    }
    std::cout << std::endl;
  }
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("11");
  auto tape = utils::ExtractNumbers<long long>(input[0]);
  int ans1 = GetPanelColours(tape, 0).size();
  std::cout << ans1 << std::endl;
  PrintPanel(GetPanelColours(tape, 1));
}
