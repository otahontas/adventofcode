package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
	"math"
)

//go:embed input.txt
var input string

func SplitToHalves(stone int) (int, int, bool) {
	digits := 0
	for i := stone; i > 0; i /= 10 {
		digits++
	}
	if digits%2 != 0 {
		return 0, 0, false
	}
	divisor := int(math.Pow10(digits / 2))
	return stone / divisor, stone % divisor, true
}

var cache = make(map[complex128]int)

func Blink(stone int, curr int, goal int) int {
	if curr == goal {
		return 1
	}
	key := complex(float64(stone), float64(goal-curr)) // memoize
	if cache[key] != 0 {
		return cache[key]
	}
	curr++
	if stone == 0 {
		res := Blink(1, curr, goal)
		cache[key] = res
		return res
	}
	first_half, second_half, can_be_split := SplitToHalves(stone)
	if can_be_split {
		res := Blink(first_half, curr, goal) + Blink(second_half, curr, goal)
		cache[key] = res
		return res
	}
	res := Blink(stone*2024, curr, goal)
	cache[key] = res
	return res
}

func main() {
	nums := utils.ExtractNumbers((utils.SplitByDelimiterAndStrip(input)[0]))
	ans1, ans2 := 0, 0
	for _, num := range nums {
		ans1 += Blink(num, 0, 25)
	}
	for _, num := range nums {
		ans2 += Blink(num, 0, 75)
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
