#include "utils/utils.h"
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <vector>

std::map<std::string, std::vector<std::string>>
ParseToAdjacencyList(std::vector<std::string> &input) {
  std::map<std::string, std::vector<std::string>> graph;
  for (const auto &line : input) {
    auto pos = line.find(')');
    auto node = line.substr(0, pos);
    auto neighbour = line.substr(pos + 1);
    graph[node].push_back(neighbour);
    graph[neighbour].push_back(node);
  }
  return graph;
}

int DepthFirstSearch(std::map<std::string, std::vector<std::string>> &graph,
                     const std::string &start, const std::string &goal = "") {
  std::stack<std::pair<std::string, int>> s;
  std::set<std::string> seen;
  int count = 0;
  s.push({start, 0});

  while (!s.empty()) {
    auto node = s.top().first;
    auto dist = s.top().second;
    s.pop();

    if (node == goal) {
      return dist - 2;
    }
    seen.insert(node);

    for (const auto &neighbour : graph[node]) {
      if (seen.count(neighbour)) {
        continue;
      }
      count += dist + 1;
      s.push({neighbour, dist + 1});
    }
  }

  return count;
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("06");
  auto graph = ParseToAdjacencyList(input);
  int ans1 = DepthFirstSearch(graph, "COM");
  int ans2 = DepthFirstSearch(graph, "YOU", "SAN");
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
