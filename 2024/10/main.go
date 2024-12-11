package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
)

//go:embed input.txt
var input string
var directions = []complex128{1, -1, 1i, -1i}

type Options struct {
	count_once bool
	found      map[complex128]bool
}

func CountWaysTo9(point complex128, steps int, grid [][]int, options Options) int {
	if grid[int(imag(point))][int(real(point))] == 9 {
		if options.count_once {
			if options.found[point] {
				return 0
			}
			options.found[point] = true
		}
		return 1
	}
	count := 0
	for _, dir := range directions {
		new_point := point + dir
		x, y := int(real(new_point)), int(imag(new_point))
		if x < 0 || x >= len(grid) || y < 0 || y >= len(grid[0]) {
			continue
		}
		if grid[y][x] == steps+1 {
			count += CountWaysTo9(new_point, steps+1, grid, options)
		}
	}
	return count
}

func main() {
	string_grid := utils.SplitByDelimiterAndStrip(input)
	// convert
	grid := make([][]int, len(string_grid))
	for y, string_row := range string_grid {
		row := make([]int, len(string_row))
		for x, char := range string_row {
			row[x] = int(char) - 48
		}
		grid[y] = row
	}
	// dfs
	ans1, ans2 := 0, 0
	for y, row := range grid {
		for x, num := range row {
			if num == 0 {
				found := make(map[complex128]bool)
				ans1 += CountWaysTo9(complex(float64(x), float64(y)), 0, grid, Options{count_once: true, found: found})
				ans2 += CountWaysTo9(complex(float64(x), float64(y)), 0, grid, Options{count_once: false})
			}
		}
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
