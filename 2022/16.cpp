// part 2 d 16 cpp
#include <fstream>
#include <iostream>
#include <map>
#include <regex>
#include <set>
#include <unordered_map>
#include <vector>

using namespace std;

int BIG_NUM = 100000000;

map<tuple<int, vector<int>, int, bool>, bool> calculated;
map<tuple<int, vector<int>, int, bool>, int> cache;

int search(int node, vector<int> left, int minutes,
           const map<int, int> flow_rates, const vector<vector<int>> dist,
           int start, bool elephant = false) {

  vector<int> results;
  // calculate key
  tuple<int, vector<int>, int, bool> key;
  key = make_tuple(node, left, minutes, elephant);
  if (calculated.find(key) != calculated.end()) {
    return cache[key];
  }

  // cout << "now at node " << node << "\n";
  // cout << "and left:\n";
  // for (auto other : left) {
  //   cout << "other " << other << "\n";
  // }
  for (auto other : left) {
    // cout << " handling other: " << other << "\n";
    auto fr = flow_rates.at(other);
    auto d = dist[node][other];
    if (d >= minutes) // can't make it in time
      continue;
    vector<int> new_left;
    for (auto l : left) {
      if (l == other)
        continue;
      new_left.push_back(l);
    }
    int new_minutes = minutes - d - 1; // min to open
    results.push_back(fr * new_minutes +

                      search(other, new_left, new_minutes, flow_rates, dist,
                             start, elephant));
  }
  // return greates of results
  int result = 0;
  if (elephant == true) {
    vector<int> new_left;
    for (auto l : left) {
      new_left.push_back(l);
    }
    results.push_back(
        search(start, new_left, 26, flow_rates, dist, start, false));
  }
  if (results.size() > 0) {
    result = *max_element(results.begin(), results.end());
  }
  calculated[key] = true;
  cache[key] = result;
  return result;
}

int main() {
  string filename = "inputs/16.txt";
  ifstream puzzle_input(filename);
  string input_line;
  regex node_extractor("[A-Z]{2}");
  regex int_extractor("\\d+");

  int id_counter = 0;
  map<string, int> name_to_id;
  map<int, int> flow_rates;
  vector<vector<int>> dist;

  // read input
  vector<string> lines;
  while (getline(puzzle_input, input_line)) {
    lines.push_back(input_line);
  }

  // Init distance matrix
  int n = lines.size();
  for (int i = 0; i < n; i++) {
    dist.push_back(vector<int>(n, BIG_NUM));
  }

  // parse graph
  for (auto line : lines) {
    auto nodes_start =
        std::sregex_iterator(line.begin(), line.end(), node_extractor);
    auto nodes_end = std::sregex_iterator();
    int i = 0;
    int node_id;
    for (auto iter = nodes_start; iter != nodes_end; iter++, i++) {
      if (i == 0) {
        auto node_name = iter->str();
        if (name_to_id.find(node_name) == name_to_id.end()) {
          name_to_id[node_name] = id_counter++;
        }
        node_id = name_to_id[node_name];
        dist[node_id][node_id] = 0;
      } else {
        auto neighbor_name = iter->str();
        if (name_to_id.find(neighbor_name) == name_to_id.end()) {
          name_to_id[neighbor_name] = id_counter++;
        }
        auto neighbor_id = name_to_id[neighbor_name];
        dist[node_id][neighbor_id] = 1;
        dist[neighbor_id][node_id] = 1;
      }
    }

    auto flow_rate = stoi(
        std::sregex_iterator(line.begin(), line.end(), int_extractor)->str());
    if (flow_rate > 0)
      flow_rates[node_id] = flow_rate;
  }

  // floyd warshall
  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }

  vector<int> left_at_start;
  for (auto fr : flow_rates) {
    left_at_start.push_back(fr.first);
  }
  int start = name_to_id["AA"];

  auto res1 = search(start, left_at_start, 30, flow_rates, dist, start);
  auto res2 = search(start, left_at_start, 26, flow_rates, dist, start, true);
  cout << "ans1: " << res1 << "\n";
  cout << "ans2: " << res2 << "\n";
}
