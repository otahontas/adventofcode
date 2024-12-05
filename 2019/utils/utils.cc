#include "utils.h"
#include <fstream>
#include <regex>
#include <string>
#include <vector>

namespace utils {

std::vector<std::string> ReadInputAndSplitByDelimiter(const std::string &day,
                                                      char delimiter) {
  auto filename = "inputs/" + day + ".txt";
  std::ifstream input(filename);
  if (!input.is_open()) {
    throw std::runtime_error("Unable to open file with filename: " + filename);
  }
  std::string line;
  std::vector<std::string> lines;
  while (getline(input, line, delimiter)) {
    lines.push_back(line);
  }
  return lines;
}

template <typename T>
std::vector<T> ExtractNumbers(const std::string &input, bool include_negative) {
  static_assert(std::is_arithmetic<T>::value,
                "ReadNumbers requires a numeric type");
  std::regex extractor(include_negative ? "-?\\d+" : "\\d+");
  std::vector<T> nums;
  auto start = std::sregex_iterator(input.begin(), input.end(), extractor);
  auto end = std::sregex_iterator();
  for (auto iter = start; iter != end; iter++) {
    auto match = iter->str();
    if constexpr (std::is_same<T, int>::value) {
      nums.push_back(std::stoi(match)); // Handle int
    } else if constexpr (std::is_same<T, long long>::value) {
      nums.push_back(std::stoll(match)); // Handle long long
    }
  }
  return nums;
}
template std::vector<int> ExtractNumbers<int>(const std::string &input,
                                              bool include_negative);
template std::vector<long long>
ExtractNumbers<long long>(const std::string &input, bool include_negative);

} // namespace utils
