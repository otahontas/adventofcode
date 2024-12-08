package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
)

//go:embed input.txt
var input string

func collectAntennas(grid []string) map[rune][]complex128 {
	antennas := map[rune][]complex128{}
	for y, row := range grid {
		for x, cell := range row {
			if cell != '.' {
				antennas[cell] = append(antennas[cell], complex(float64(x), float64(y)))
			}
		}
	}
	return antennas
}

func pointIsWithinBounds(point complex128, h, w int) bool {
	x, y := int(real(point)), int(imag(point))
	return x >= 0 && x < w && y >= 0 && y < h
}

func markAllAntinodesInLine(point complex128, direction complex128, taken map[complex128]bool, h, w int) {
	for pointIsWithinBounds(point, h, w) {
		taken[point] = true
		point += direction
	}
}
func countUniqueAntinodes(antennas map[rune][]complex128, h, w int) (int, int) {
	nearby_antinodes := map[complex128]bool{}
	antinodes_in_line := map[complex128]bool{}
	for _, v := range antennas {
		for i := 0; i < len(v)-1; i++ {
			for j := i + 1; j < len(v); j++ {
				dist := v[i] - v[j]
				a, b := v[i]+dist, v[j]-dist
				if pointIsWithinBounds(a, h, w) {
					nearby_antinodes[a] = true
				}
				if pointIsWithinBounds(b, h, w) {
					nearby_antinodes[b] = true
				}
				markAllAntinodesInLine(v[i], dist, antinodes_in_line, h, w)
				markAllAntinodesInLine(v[j], -dist, antinodes_in_line, h, w)
			}
		}
	}
	return len(nearby_antinodes), len(antinodes_in_line)
}

func main() {
	grid := utils.SplitByDelimiterAndStrip(input)
	h, w := len(grid), len(grid[0])
	antennas := collectAntennas(grid)
	ans1, ans2 := countUniqueAntinodes(antennas, h, w)
	fmt.Println(ans1)
	fmt.Println(ans2)
}
