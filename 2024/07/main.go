package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
)

//go:embed input.txt
var input string

func Find1(goal int, nums []int, current int) bool {
	if current > goal {
		return false
	}
	if len(nums) == 0 {
		return current == goal
	}
	return Find1(goal, nums[1:], current+nums[0]) || Find1(goal, nums[1:], current*nums[0])
}

func Find2(goal int, nums []int, current int) bool {
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
	return Find2(goal, nums[1:], current+nums[0]) || Find2(goal, nums[1:], current*nums[0]) || Find2(goal, nums[1:], d+nums[0])
}

func main() {
	lines := utils.SplitByDelimiterAndStrip(input)
	ans1, ans2 := 0, 0
	for _, line := range lines {
		nums := utils.ExtractNumbers(line)
		goal := nums[0]
		if Find1(goal, nums[2:], nums[1]) {
			ans1 += goal
		}
		if Find2(goal, nums[2:], nums[1]) {
			ans2 += goal
		}
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
