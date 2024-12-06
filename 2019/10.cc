#include "data_structures/complex.h"
#include "utils/utils.h"
#include <iostream>
#include <numeric>
#include <set>
#include <vector>

complex::Complex<int> GetDirectionVector(complex::Complex<int> source,
                                         complex::Complex<int> destination) {
  auto diff = destination - source;
  int gcd = std::gcd(diff.real(), diff.imag());
  return complex::Complex<int>(diff.real() / gcd, diff.imag() / gcd);
}

std::vector<complex::Complex<int>>
FindAsteroidsInDirection(complex::Complex<int> source,
                         complex::Complex<int> direction_vector, int h, int w,
                         std::set<complex::Complex<int>> &asteroids) {
  std::vector<complex::Complex<int>> asteroids_on_line;
  auto current = source;
  while (current.real() < w && current.imag() < h && current.real() >= 0 &&
         current.imag() >= 0) {
    current += direction_vector;
    if (asteroids.find(current) != asteroids.end()) {
      asteroids_on_line.push_back(current);
    }
  }
  return asteroids_on_line;
}

std::pair<complex::Complex<int>, int>
FindBestLocation(int h, int w, std::set<complex::Complex<int>> &asteroids) {
  std::pair<complex::Complex<int>, int> best_location_and_count = {
      complex::Complex<int>(0, 0), 0};
  for (auto &asteroid : asteroids) {
    std::set<complex::Complex<int>> blocked_asteroids;
    for (auto &other : asteroids) {
      if (asteroid == other) {
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

int Find200thAsteroidToVaporize(complex::Complex<int> source, int h, int w,
                                std::set<complex::Complex<int>> &asteroids) {
  std::set<complex::Complex<int>> angle_and_destination_added;
  std::vector<std::tuple<double, double, complex::Complex<int>>>
      asteroids_with_angle_and_destination;

  for (auto &asteroid : asteroids) {
    if (asteroid == source) {
      continue;
    }
    if (angle_and_destination_added.find(asteroid) !=
        angle_and_destination_added.end()) {
      continue;
    }
    auto direction_vector = GetDirectionVector(source, asteroid);
    // shift so that upwards (0, -y) is at 0 radians
    double radians =
        M_PI_2 + atan2(direction_vector.imag(), direction_vector.real());
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
          sqrt(pow(asteroid_on_direction.real() - source.real(), 2) +
               pow(asteroid_on_direction.imag() - source.imag(), 2));

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
        return asteroid.real() * 100 + asteroid.imag();
      }
    }
  }
}

int main() {
  auto grid = utils::ReadInputAndSplitByDelimiter("10");
  std::set<complex::Complex<int>> asteroids;
  int h = grid.size();
  int w = grid[0].size();
  for (int y = 0; y < h; y++) {
    for (int x = 0; x < w; x++) {
      if (grid[y][x] == '#') {
        asteroids.insert(complex::Complex<int>(x, y));
      }
    }
  }
  auto best_location = FindBestLocation(h, w, asteroids);
  int ans1 = best_location.second;
  int ans2 = Find200thAsteroidToVaporize(best_location.first, h, w, asteroids);
  std::cout << ans1 << std::endl;
  std::cout << ans2 << std::endl;
}
