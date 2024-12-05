package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
	"sort"
)

//go:embed input.txt
var input string

func step(y int, x int, dy int, dx int, grid []string, chars string, goal string) int {
	if chars == goal {
		return 1
	}
	if y < 0 || y >= len(grid) || x < 0 || x >= len(grid[0]) {
		return 0
	}
	if grid[y][x] == goal[len(chars)] {
		ny := y + dy
		nx := x + dx
		return step(ny, nx, dy, dx, grid, chars+string(grid[y][x]), goal)
	}
	return 0
}

func main() {
	grid := utils.SplitByDelimiterAndStrip(input)
	ans1, ans2 := 0, 0
	for y, line := range grid {
		for x, char := range line {
			if char == 'X' {
				for _, dy := range []int{-1, 0, 1} {
					for _, dx := range []int{-1, 0, 1} {
						ans1 += step(y+dy, x+dx, dy, dx, grid, "X", "XMAS")
					}

				}
			}
			not_in_bounds := y > 0 && x > 0 && y < len(grid)-1 && x < len(grid[0])-1
			if char == 'A' && not_in_bounds {
				diagonals := []string{
					string(grid[y-1][x-1]),
					string(grid[y-1][x+1]),
					string(grid[y+1][x-1]),
					string(grid[y+1][x+1]),
				}
				sorted_diagonals := make([]string, len(diagonals))
				copy(sorted_diagonals, diagonals)
				sort.Strings(sorted_diagonals)
				correct_positions :=
					(diagonals[0] == diagonals[1] && diagonals[2] == diagonals[3]) ||
						(diagonals[0] == diagonals[2] && diagonals[1] == diagonals[3])
				correct_chars := sorted_diagonals[0] == "M" && sorted_diagonals[2] == "S"
				if correct_positions && correct_chars {
					ans2++
				}

			}
		}
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
