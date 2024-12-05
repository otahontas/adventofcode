#ifndef _UTILS_H
#define _UTILS_H
#include <regex>
#include <string>
#include <vector>

namespace utils {

std::vector<std::string> ReadInputAndSplitByDelimiter(const std::string &day,
                                                      char delimiter = '\n');

template <typename T = int>
std::vector<T> ExtractNumbers(const std::string &input,
                              bool include_negative = true);
extern template std::vector<int> ExtractNumbers<int>(const std::string &input,
                                                     bool include_negative);
extern template std::vector<long long>
ExtractNumbers<long long>(const std::string &input, bool include_negative);

} // namespace utils
#endif
