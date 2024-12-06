package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
)

//go:embed input.txt
var input string

func getStartingPosition(grid []string) complex128 {
	for y, line := range grid {
		for x, char := range line {
			if char == '^' {
				return complex(float64(x), float64(y))
			}
		}
	}
	return complex(0, 0)
}

func simulateRoundAndReturnVisitedPoints(grid []string) []complex128 {
	h, w := len(grid), len(grid[0])
	visited := make(map[complex128]bool, 0)
	position := getStartingPosition(grid)
	direction := complex(0, -1)
	for {
		visited[position] = true
		new_position := position + direction
		x := int(real(new_position))
		y := int(imag(new_position))
		if x < 0 || x >= w || y < 0 || y >= h {
			break
		}
		if grid[y][x] == '#' {
			direction *= complex(0, 1) // turn right
		} else {
			position = new_position
		}
	}
	visited_points := make([]complex128, len(visited))
	i := 0
	for k := range visited {
		visited_points[i] = k
		i++
	}
	return visited_points
}

func hasLoop(grid []string, new_obstacle complex128) bool {
	h, w := len(grid), len(grid[0])
	visited := make(map[complex128]int, 0)
	position := getStartingPosition(grid)
	direction := complex(0, -1)
	for {
		visited[position]++
		new_position := position + direction
		x := int(real(new_position))
		y := int(imag(new_position))
		if x < 0 || x >= w || y < 0 || y >= h {
			break
		}
		// over 4 visits to the same cell means that we've
		// arrived at least twice from same direction --> loop
		if visited[position] > 4 {
			return true
		}
		if grid[y][x] == '#' || new_position == new_obstacle {
			direction *= complex(0, 1) // turn right
		} else {
			position = new_position
		}
	}
	return false
}

func findLoops(grid []string, visited_points []complex128) int {
	loops := 0
	// faster if we only try to put new obstacles on visited points
	for _, point := range visited_points {
		if hasLoop(grid, point) {
			loops++
		}
	}
	return loops
}

func main() {
	grid := utils.SplitByDelimiterAndStrip(input)
	visited_points := simulateRoundAndReturnVisitedPoints(grid)
	ans1 := len(visited_points)
	ans2 := findLoops(grid, visited_points)
	fmt.Println(ans1)
	fmt.Println(ans2)
}
