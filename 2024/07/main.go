package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
)

//go:embed input.txt
var input string

func goalCanBeFormed(goal int, nums []int, current int) bool {
	if current > goal {
		return false
	}
	if len(nums) == 0 {
		return current == goal
	}
	return goalCanBeFormed(goal, nums[1:], current+nums[0]) || goalCanBeFormed(goal, nums[1:], current*nums[0])
}

func goalCanBeFormedWithConcat(goal int, nums []int, current int) bool {
	if current > goal {
		return false
	}
	if len(nums) == 0 {
		return current == goal
	}
	d := current
	for tens := nums[0]; tens > 0; tens /= 10 {
		d *= 10
	}
	return goalCanBeFormedWithConcat(goal, nums[1:], current+nums[0]) ||
		goalCanBeFormedWithConcat(goal, nums[1:], current*nums[0]) ||
		goalCanBeFormedWithConcat(goal, nums[1:], d+nums[0])
}

func main() {
	lines := utils.SplitByDelimiterAndStrip(input)
	ans1, ans2 := 0, 0
	for _, line := range lines {
		nums := utils.ExtractNumbers(line)
		goal := nums[0]
		if goalCanBeFormed(goal, nums[2:], nums[1]) {
			ans1 += goal
		}
		if goalCanBeFormedWithConcat(goal, nums[2:], nums[1]) {
			ans2 += goal
		}
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
