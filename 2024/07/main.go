package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
	"strconv"
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
	res, err := strconv.Atoi(strconv.Itoa(a) + strconv.Itoa(b))
	if err != nil {
		panic(err)
	}
	return res
}

func Recurse(operation_map map[int]string, nums []int, result int, result_operations string, allow_concat bool) {
	operations := []string{"+", "*"}
	if allow_concat {
		operations = append(operations, "||")
	}
	if len(nums) == 0 {
		operation_map[result] = result_operations
		return
	}
	for _, operation := range operations {
		res := TryOperation(result, nums[0], operation)
		others := nums[1:]
		Recurse(operation_map, others, res, result_operations+operation, allow_concat)
	}
}

func main() {
	lines := utils.SplitByDelimiterAndStrip(input)
	ans1, ans2 := 0, 0
	for _, line := range lines {
		nums := utils.ExtractNumbers(line)
		result := nums[0]
		operation_map := make(map[int]string)
		Recurse(operation_map, nums[2:], nums[1], "", false)
		if operation_map[result] != "" {
			ans1 += result
		}
		operation_map = make(map[int]string)
		Recurse(operation_map, nums[2:], nums[1], "", true)
		if operation_map[result] != "" {
			ans2 += result
		}
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
