#include "utils/utils.h"
#include <algorithm>
#include <iostream>

bool Validate(int num, bool only_allow_two_adj = false) {
  std::string password = std::to_string(num);
  std::string sorted_password = password;
  sort(sorted_password.begin(), sorted_password.end());
  if (password != sorted_password) {
    return false;
  }
  int n = password.size();
  for (int i = 0; i < n - 1; i++) {
    if (password[i] == password[i + 1]) {
      if (!only_allow_two_adj) {
        return true;
      }
      if ((i == 0 || password[i] != password[i - 1]) &&
          (i == n - 2 || password[i] != password[i + 2])) {
        return true;
      }
    }
  }
  return false;
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("04");
  auto num_range = utils::ExtractNumbers(input[0], false);
  int ans1 = 0;
  int ans2 = 0;
  for (int i = num_range[0]; i <= num_range[1]; i++) {
    ans1 += Validate(i);
    ans2 += Validate(i, true);
  }
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
