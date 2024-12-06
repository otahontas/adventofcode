#include "int_code_comp/int_code_comp.h"
#include "utils/utils.h"
#include <iostream>

int CountBlockTiles(std::vector<long long> &tape) {
  int_code_comp::IntCodeComp comp(tape);
  comp.Run();
  auto outputs = comp.GetOutputs();
  int count = 0;
  for (int i = 0; i < outputs.size(); i += 3) {
    auto [x, y, tile] =
        std::make_tuple(outputs[i], outputs[i + 1], outputs[i + 2]);
    if (tile == 2) {
      count++;
    }
  }
  return count;
}

int PlayGame(std::vector<long long> &tape) {
  tape[0] = 2;
  int_code_comp::IntCodeComp comp(tape);
  int score = 0;
  int ball_x = 0;
  int paddle_x = 0;
  while (true) {
    comp.Run();
    auto outputs = comp.GetOutputs();
    for (int i = 0; i < outputs.size(); i += 3) {
      auto [x, y, tile] =
          std::make_tuple(outputs[i], outputs[i + 1], outputs[i + 2]);
      if (x == -1 && y == 0) {
        score = tile;
      } else if (tile == 3) {
        paddle_x = x;
      } else if (tile == 4) {
        ball_x = x;
      }
    }
    if (comp.IsHalted()) {
      break;
    }
    int input = ball_x > paddle_x ? 1 : ball_x < paddle_x ? -1 : 0;
    comp.AddInput(input);
  }
  return score;
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("13");
  auto tape = utils::ExtractNumbers<long long>(input[0]);
  int ans1 = CountBlockTiles(tape);
  std::cout << ans1 << std::endl;
  std::cout << PlayGame(tape) << std::endl;
}
