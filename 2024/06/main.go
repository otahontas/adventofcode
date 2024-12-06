package main

import (
	"adventofcode/utils"
	_ "embed"
	"errors"
	"fmt"
)

//go:embed input.txt
var input string

func getStartingPosition(grid []string) (complex128, error) {
	for y, line := range grid {
		for x, char := range line {
			if char == '^' {
				return complex(float64(x), float64(y)), nil
			}
		}
	}
	return complex(0, 0), errors.New("No starting position found")
}

func simulateRound(grid []string, new_obstacle complex128) (int, bool) {
	h, w := len(grid), len(grid[0])
	visited := make(map[complex128]bool, 0)
	position, err := getStartingPosition(grid)
	if err != nil {
		fmt.Println(err)
		return -1, false
	}
	direction := complex(0, -1)
	check_for_loops := new_obstacle != complex(-1, -1)
	steps := 0
	// greedy guess, if steps exceed this threshold, it's a loop. could be optimized
	steps_threshold := (h * w) / 3
	for {
		visited[position] = true
		new_position := position + direction
		x := int(real(new_position))
		y := int(imag(new_position))
		if x < 0 || x >= w || y < 0 || y >= h {
			break
		}
		if check_for_loops && steps >= steps_threshold {
			return -1, true
		}
		if grid[y][x] == '#' || new_position == new_obstacle {
			direction *= complex(0, 1) // turn right
		} else {
			position = new_position
			steps++
		}
	}
	return len(visited), false
}

func findLoops(grid []string) int {
	loops := 0
	for y, line := range grid {
		for x, char := range line {
			if char == '.' {
				_, is_loop := simulateRound(grid, complex(float64(x), float64(y)))
				if is_loop {
					loops++
				}
			}
		}
	}
	return loops
}

func main() {
	grid := utils.SplitByDelimiterAndStrip(input)
	ans1, _ := simulateRound(grid, complex(-1, -1))
	ans2 := findLoops(grid)
	fmt.Println(ans1)
	fmt.Println(ans2)
}
