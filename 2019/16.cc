#include "utils/utils.h"
#include <iostream>
#include <numeric>
#include <vector>

int FirstNDigitsToInt(std::vector<int> &digits, int n) {
  int result = 0;
  for (int i = 0; i < n; i++) {
    result += digits[i] * pow(10, n - i - 1);
  }
  return result;
}

int Run100Phases(std::vector<int> digits) {
  int pattern[] = {0, 1, 0, -1};
  for (int i = 0; i < 100; i++) {
    std::vector<int> new_digits(digits.size());
    for (int j = 0; j < digits.size(); j++) {
      int sum = 0;
      for (int k = j; k < digits.size(); k++) {
        // k+1 shifts the pattern by 1
        // j+1 = pattern repeat j+1 times at step j
        // --> correct pattern digit to use is at (k+1) / (j+1) % 4
        sum += digits[k] * pattern[((k + 1) / (j + 1)) % 4];
      }
      new_digits[j] = (abs(sum) % 10); // the last digit
    }
    digits = new_digits;
  }
  return FirstNDigitsToInt(digits, 8);
}

// since the offset is in the second half of the digits
// each digit is now backwards cumulative sum %10 (1, -1, 0 patterns cancel out)
// e.g. for (1234)5678, last digits are 8, 7+8 = 15 -> %10 = 5, 6+15 = 21 -> %10
// so we can calculate the sum and at each step take %10 and update the sum
int Run100PhasesForOffset(std::vector<int> digits) {
  for (int i = 0; i < 100; i++) {
    std::vector<int> new_digits(digits.size());
    int sum = std::accumulate(digits.begin(), digits.end(), 0);
    for (int j = 0; j < digits.size(); j++) {
      new_digits[j] = sum % 10;
      sum -= digits[j];
    }
    digits = new_digits;
  }
  return FirstNDigitsToInt(digits, 8);
}

int main() {
  auto lines = utils::ReadInputAndSplitByDelimiter("16");
  std::vector<int> digits;
  for (auto c : lines[0]) {
    digits.push_back(c - '0');
  }
  int ans1 = Run100Phases(digits);
  int offset = FirstNDigitsToInt(digits, 7);
  // assert offset > digits.size() / 2
  if (offset < digits.size() / 2) {
    throw std::runtime_error("offset < digits.size() / 2");
    return 1;
  }
  std::vector<int> offset_digits(digits.size() * 10000 - offset);
  for (int i = offset; i < digits.size() * 10000; i++) {
    offset_digits[i - offset] = digits[i % digits.size()];
  }
  int ans2 = Run100PhasesForOffset(offset_digits);
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
