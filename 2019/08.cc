#include "utils/utils.h"
#include <iostream>
#include <vector>

std::vector<std::vector<int>> ParseMatrix(std::vector<int> &nums, int width,
                                          int length) {
  std::vector<std::vector<int>> matrix;
  int size = width * length;
  std::vector<int> row;
  for (int i = 0; i < (int)nums.size(); i++) {
    row.push_back(nums[i]);
    if (i % size == size - 1) {
      matrix.push_back(row);
      row.clear();
    }
  }
  return matrix;
}

int FewestZeros(std::vector<std::vector<int>> &matrix) {
  int fewest = INT_MAX;
  int ans = 0;
  for (auto &layer : matrix) {
    std::vector<int> num_count = {0, 0, 0};
    for (auto num : layer) {
      num_count[num]++;
    }
    if (num_count[0] < fewest) {
      fewest = num_count[0];
      ans = num_count[1] * num_count[2];
    }
  }
  return ans;
}

std::vector<int> DecodeImage(std::vector<std::vector<int>> &matrix) {
  int n = matrix[0].size();
  int layers = matrix.size();
  std::vector<int> flattened_image(n);

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < layers; j++) {
      if (matrix[j][i] != 2) {
        flattened_image[i] = matrix[j][i];
        break;
      }
    }
  }

  return flattened_image;
}

void PrintDecodedImage(std::vector<int> &image, int width) {
  for (int i = 0; i < (int)image.size(); i++) {
    if (image[i]) {
      std::cout << "#";
    } else {
      std::cout << " ";
    }
    if (i % width == width - 1) {
      std::cout << "\n";
    }
  }
}

int main() {
  int length = 6;
  int width = 25;
  auto input = utils::ReadInputAndSplitByDelimiter("08");
  std::vector<int> nums;
  for (auto &c : input[0]) {
    nums.push_back(c - '0');
  }
  std::vector<std::vector<int>> matrix = ParseMatrix(nums, width, length);
  std::vector<int> image = DecodeImage(matrix);
  int ans1 = FewestZeros(matrix);
  std::cout << ans1 << std::endl;
  PrintDecodedImage(image, width);
}
