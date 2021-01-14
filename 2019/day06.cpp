#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <regex>
#include <vector>
#include "aoc.h"

typedef std::map<std::string, std::vector<std::string>> Graph;
typedef std::pair<std::string, int> NodePair;

// Parse puzzle input to undirected graph represented as adjacency list.
Graph ParseToGraph(std::vector<std::string>& puzzle_input) {
    Graph graph;
    for (const auto& line : puzzle_input) {
        auto pos = line.find(')');
        auto node = line.substr(0, pos);
        auto neighbour = line.substr(pos+1);
        graph[node].push_back(neighbour);
        graph[neighbour].push_back(node);
    }
    return graph;
}

// Both parts can be solved with simple depth-first search. 
// - In the first part, at each object total amount is increased by number of
// neighbours (=direct orbits) plus number of neighbours multiplied by length from
// COM (=indirect orbits).
// - In the second part, code finds shortest path from YOU to SAN.
int dfs(Graph& graph, const std::string& start, const std::string& goal = "") {
    std::stack<NodePair> s;
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

void Test() {
    std::vector<std::string> example = { "COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", 
                                         "G)H", "D)I", "E)J", "J)K", "K)L" };
    auto graph = ParseToGraph(example);
    assert(dfs(graph, "COM") == 42);
    std::vector<std::string> second_example = { "COM)B", "B)C", "C)D", "D)E", "E)F",
                                                "B)G", "G)H", "D)I", "E)J", "J)K",
                                                "K)L", "K)YOU", "I)SAN" };
    auto second_graph = ParseToGraph(second_example);
    assert(dfs(second_graph, "YOU", "SAN") == 4);
}

void Solve() {
    std::vector<std::string> puzzle_input = aoc::ReadInputToLines(6);
    auto graph = ParseToGraph(puzzle_input);
    std::cout << aoc::Solution(dfs(graph, "COM"),
                          dfs(graph, "YOU", "SAN"));
}

int main() {
    Test();
    Solve();
}
