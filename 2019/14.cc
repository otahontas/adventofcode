#include "utils/utils.h"
#include <iostream>
#include <map>
#include <regex>
#include <string>

class Chemical {
private:
  std::string name;
  long long needed = 0;
  long long produced = 0;
  std::map<std::string, int> ingredients;
  int output_amount = 0;

public:
  Chemical() = default;
  Chemical(std::map<std::string, int> ingredients, int output_amount)
      : needed(0), produced(0), ingredients(std::move(ingredients)),
        output_amount(output_amount) {}

  void SetNeeded(long long needed) { this->needed = needed; }
  void SetProduced(long long produced) { this->produced = produced; }
  long long GetNeeded() const { return needed; }
  long long GetProduced() const { return produced; }
  int GetOutputAmount() const { return output_amount; }
  std::map<std::string, int> GetIngredients() const { return ingredients; }
};

std::pair<int, std::string> ExtractAmountAndName(const std::string &input) {
  std::regex extractor("(\\d+) (\\w+)");
  auto matches = std::sregex_iterator(input.begin(), input.end(), extractor);
  auto match = *matches;
  return {std::stoi(match[1].str()), match[2].str()};
}
std::map<std::string, Chemical>
CreateChemicalsMap(const std::vector<std::string> &lines,
                   long long fuel_amount) {
  std::map<std::string, Chemical> chemicals;
  auto recipe_extractor = std::regex("\\d+ \\w+");
  for (auto line : lines) {
    std::vector<std::string> parts;
    auto start =
        std::sregex_iterator(line.begin(), line.end(), recipe_extractor);
    auto end = std::sregex_iterator();
    for (auto iter = start; iter != end; iter++) {
      auto match = iter->str();
      parts.push_back(match);
    }
    auto [output_amount, output_name] = ExtractAmountAndName(parts.back());
    std::map<std::string, int> ingredients;
    std::vector<std::string> input = {parts.begin(), parts.end() - 1};
    for (auto part : input) {
      auto [amount, name] = ExtractAmountAndName(part);
      ingredients[name] = amount;
    }
    chemicals[output_name] = Chemical(ingredients, output_amount);
  }
  chemicals["ORE"] = Chemical({}, 1);
  chemicals["FUEL"].SetNeeded(fuel_amount);
  return chemicals;
}

long long CalculateOreAmount(std::map<std::string, Chemical> &chemicals) {
  while (true) {
    bool everything_produced = true;
    for (auto &[name, chemical] : chemicals) {
      if (chemical.GetProduced() >= chemical.GetNeeded()) {
        continue;
      }
      everything_produced = false;
      double create_multiplier =
          std::ceil((double)(chemical.GetNeeded() - chemical.GetProduced()) /
                    (double)chemical.GetOutputAmount());
      chemical.SetProduced(chemical.GetProduced() +
                           create_multiplier * chemical.GetOutputAmount());
      for (auto &[ingredient_name, ingredient_amount] :
           chemical.GetIngredients()) {
        chemicals[ingredient_name].SetNeeded(
            chemicals[ingredient_name].GetNeeded() +
            create_multiplier * ingredient_amount);
      }
    }
    if (everything_produced) {
      return chemicals["ORE"].GetNeeded();
    }
  }
}

// binary search
long long FindMaxFuel(const std::vector<std::string> &lines, int start_value) {
  long long ores = 1000000000000;
  long long lower = ores / start_value;
  long long higher = 2 * lower;

  while (higher > lower + 1) {
    long long middle = (lower + higher) / 2;
    auto new_map = CreateChemicalsMap(lines, middle);
    long long new_amount = CalculateOreAmount(new_map);
    if (new_amount <= ores) {
      lower = middle;
    } else {
      higher = middle;
    }
  }
  return lower;
}

int main() {
  auto lines = utils::ReadInputAndSplitByDelimiter("14");
  auto chemicals_for_one_fuel = CreateChemicalsMap(lines, 1);
  int ans1 = CalculateOreAmount(chemicals_for_one_fuel);
  long long ans2 = FindMaxFuel(lines, ans1);
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
