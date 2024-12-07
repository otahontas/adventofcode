package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
)

//go:embed input.txt
var input string

func TryOperation(a int, b int, operation string) int {
	if operation == "+" {
		return a + b
	}
	if operation == "*" {
		return a * b
	}
	a_multiplier := 1
	for tens := b; tens > 0; tens /= 10 {
		a_multiplier *= 10
	}
	return a*a_multiplier + b
}

func Recurse(goal int, operation_map map[int]string, nums []int, current int, current_operations string, allow_concat bool) {
	operations := []string{"+", "*"}
	if allow_concat {
		operations = append(operations, "||")
	}
	if current > goal {
		return
	}
	if len(nums) == 0 {
		operation_map[current] = current_operations
		return
	}
	for _, operation := range operations {
		res := TryOperation(current, nums[0], operation)
		others := nums[1:]
		Recurse(goal, operation_map, others, res, current_operations+operation, allow_concat)
	}
}

func main() {
	lines := utils.SplitByDelimiterAndStrip(input)
	ans1, ans2 := 0, 0
	for _, line := range lines {
		nums := utils.ExtractNumbers(line)
		goal := nums[0]
		operation_map := make(map[int]string)
		Recurse(goal, operation_map, nums[2:], nums[1], "", false)
		if operation_map[goal] != "" {
			ans1 += goal
		}
		operation_map = make(map[int]string)
		Recurse(goal, operation_map, nums[2:], nums[1], "", true)
		if operation_map[goal] != "" {
			ans2 += goal
		}
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
