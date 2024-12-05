#include "utils/utils.h"
#include <iostream>
#include <numeric>
#include <set>
#include <vector>

std::pair<int, int> GetDirectionVector(std::pair<int, int> source,
                                       std::pair<int, int> destination) {
  int dx = destination.first - source.first;
  int dy = destination.second - source.second;
  int gcd = std::gcd(dx, dy);
  int step_x = dx / gcd;
  int step_y = dy / gcd;
  return {step_x, step_y};
}

std::vector<std::pair<int, int>>
FindAsteroidsInDirection(std::pair<int, int> source,
                         std::pair<int, int> direction_vector, int h, int w,
                         std::set<std::pair<int, int>> &asteroids) {
  std::vector<std::pair<int, int>> asteroids_on_line;
  int nx = source.first;
  int ny = source.second;
  while (nx < w && ny < h && nx >= 0 && ny >= 0) {
    nx += direction_vector.first;
    ny += direction_vector.second;
    if (asteroids.find({nx, ny}) != asteroids.end()) {
      asteroids_on_line.push_back({nx, ny});
    }
  }
  return asteroids_on_line;
}

std::pair<std::pair<int, int>, int>
FindBestLocation(int h, int w, std::set<std::pair<int, int>> &asteroids) {
  std::pair<std::pair<int, int>, int> best_location_and_count = {{0, 0}, 0};
  for (auto &asteroid : asteroids) {
    std::set<std::pair<int, int>> blocked_asteroids;
    for (auto &other : asteroids) {
      if (asteroid.first == other.first && asteroid.second == other.second) {
        continue;
      }
      if (blocked_asteroids.find(other) != blocked_asteroids.end()) {
        continue;
      }
      auto asteroids_in_direction = FindAsteroidsInDirection(
          asteroid, GetDirectionVector(asteroid, other), h, w, asteroids);
      if (asteroids_in_direction.size() > 1) {
        // more than one means that others are blocked
        blocked_asteroids.insert(asteroids_in_direction.begin() + 1,
                                 asteroids_in_direction.end());
      }
    }
    int max_count_from_location =
        asteroids.size() - 1 - blocked_asteroids.size();
    if (max_count_from_location > best_location_and_count.second) {
      best_location_and_count = {asteroid, max_count_from_location};
    }
  }
  return best_location_and_count;
}

int Find200thAsteroidToVaporize(std::pair<int, int> source, int h, int w,
                                std::set<std::pair<int, int>> &asteroids) {
  std::set<std::pair<int, int>> angle_and_destination_added;
  std::vector<std::tuple<double, double, std::pair<int, int>>>
      asteroids_with_angle_and_destination;

  for (auto &asteroid : asteroids) {
    if (asteroid.first == source.first && asteroid.second == source.second) {
      continue;
    }
    if (angle_and_destination_added.find(asteroid) !=
        angle_and_destination_added.end()) {
      continue;
    }
    auto direction_vector = GetDirectionVector(source, asteroid);
    // shift so that upwards (0, -y) is at 0 radians
    double radians =
        M_PI_2 + atan2(direction_vector.second, direction_vector.first);
    // normalize to [0, 2π)
    if (radians < 0) {
      radians += 2 * M_PI;
    }
    auto asteroids_on_direction =
        FindAsteroidsInDirection(source, direction_vector, h, w, asteroids);
    angle_and_destination_added.insert(asteroids_on_direction.begin() + 1,
                                       asteroids_on_direction.end());
    for (auto &asteroid_on_direction : asteroids_on_direction) {
      double distance =
          sqrt(pow(asteroid_on_direction.first - source.first, 2) +
               pow(asteroid_on_direction.second - source.second, 2));

      asteroids_with_angle_and_destination.push_back(
          {radians, distance, asteroid_on_direction}); // so that we can sort
      angle_and_destination_added.insert(asteroid_on_direction);
    }
  }
  std::sort(asteroids_with_angle_and_destination.begin(),
            asteroids_with_angle_and_destination.end());
  std::vector<bool> vaporized(asteroids_with_angle_and_destination.size(),
                              false);
  int count = 0;
  double prev_angle = INT_MAX;
  while (true) {
    for (int i = 0; i < asteroids_with_angle_and_destination.size(); i++) {
      auto [angle, _, asteroid] = asteroids_with_angle_and_destination[i];
      if (angle == prev_angle || vaporized[i]) {
        continue;
      }
      vaporized[i] = true;
      prev_angle = angle;
      count++;
      if (count == 200) {
        return asteroid.first * 100 + asteroid.second;
      }
    }
  }
}

int main() {
  auto input = utils::ReadInputAndSplitByDelimiter("10");
  std::set<std::pair<int, int>> asteroids;
  int h = input.size();
  int w = input[0].size();
  for (int y = 0; y < h; y++) {
    for (int x = 0; x < w; x++) {
      if (input[y][x] == '#') {
        asteroids.insert({x, y});
      }
    }
  }
  auto best_location = FindBestLocation(h, w, asteroids);
  int ans1 = best_location.second;
  int ans2 = Find200thAsteroidToVaporize(best_location.first, h, w, asteroids);
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
