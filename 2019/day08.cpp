#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
#include "aoc.h"

typedef std::vector<std::vector<int>> Matrix;

// Parse input to matrix where its row is flattened image layer, layer 1 as
// first row.
Matrix ParseToMatrix(std::vector<int> &puzzle_input, int width, int length) {
    Matrix matrix;
    int size = width * length;
    std::vector<int> row;
    for (int i = 0; i < (int) puzzle_input.size(); i++) {
        row.push_back(puzzle_input[i]);
        if (i % size == size - 1) {
            matrix.push_back(row);
            row.clear();
        }
    }
    return matrix;
}

// Find layer with fewest zeros, return number of 1s multiplied by number of 2s.
int FewestZeros(Matrix &matrix) {
    int fewest = INT_MAX;
    int ans = 0;
    for (int i = 0; i < (int) matrix.size(); i++) {
        std::vector<int> num_count = { 0, 0, 0};
        for (auto num : matrix[i]) {
            num_count[num]++;
        }
        if (num_count[0] < fewest) {
            fewest = num_count[0];
            ans = num_count[1] * num_count[2];
        }
    }
    return ans;
}

// Go through pixel layer-by-layer until 0 or 1 is found. Return vector
// containing final pixels (flattened).
std::vector<int> DecodeImage(Matrix &matrix) {
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

// Print the flattened image to stdout.
void PrintDecodedImage(std::vector<int> &image, int width) {
    for (int i = 0; i < (int) image.size(); i++) {
        if (image[i]) {
            std::cout << image[i];
        } else {
            std::cout << " ";
        }
        if (i % width == width - 1) {
            std::cout << "\n";
        }
    }
}

void Test() {
    std::vector<int> example = {0,2,2,2,1,1,2,2,2,2,1,2,0,0,0,0};
    int width = 2;
    int length = 2;
    Matrix example_matrix = ParseToMatrix(example, width, length);
    assert(FewestZeros(example_matrix) == 4);
    assert(DecodeImage(example_matrix) == std::vector<int>({ 0, 1, 1, 0 }));
}

void Solve() {
    std::vector<int> puzzle_input = aoc::ReadDigitInputToInts(8);
    int width = 25;
    int length = 6;

    Matrix matrix = ParseToMatrix(puzzle_input, width, length);
    std::cout << FewestZeros(matrix) << "\n";
    std::vector<int> image = DecodeImage(matrix);
    PrintDecodedImage(image, width);
}

int main() {
    Test();
    Solve();
}
