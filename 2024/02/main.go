package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
)

//go:embed input.txt
var input string

func increasing(arr []int) bool {
	if len(arr) <= 1 {
		return true
	}
	for i := 0; i < len(arr)-1; i++ {
		if arr[i] >= arr[i+1] {
			return false
		}
	}
	return true
}

func decreasing(arr []int) bool {
	if len(arr) <= 1 {
		return true
	}
	for i := 0; i < len(arr)-1; i++ {
		if arr[i] <= arr[i+1] {
			return false
		}
	}
	return true
}

func diffs_ok(arr []int) bool {
	if len(arr) <= 1 {
		return true
	}
	for i := 0; i < len(arr)-1; i++ {
		abs_diff := utils.Abs(arr[i] - arr[i+1])
		if abs_diff < 1 || abs_diff > 3 {
			return false
		}
	}
	return true
}

func is_safe(arr []int) bool {
	return (increasing(arr) || decreasing(arr)) && diffs_ok(arr)
}

func splice(arr []int, index int) []int {
	new_arr := make([]int, 0)
	for i := range arr {
		if i == index {
			continue
		}
		new_arr = append(new_arr, arr[i])
	}
	return new_arr
}

func make_all_lists_with_one_element_removed(arr []int) [][]int {
	lists := make([][]int, 0)
	for i := range arr {
		lists = append(lists, splice(arr, i))
	}
	return lists
}

func main() {
	ans1 := 0
	ans2_addition := 0
	for _, line := range utils.ReadLines(input) {
		levels := utils.ReadNumbers(line)
		if is_safe(levels) {
			ans1++
			continue
		}
		for _, new_levels := range make_all_lists_with_one_element_removed(levels) {
			if is_safe(new_levels) {
				ans2_addition++
				break
			}
		}
	}
	fmt.Println(ans1)
	fmt.Println(ans1 + ans2_addition)
}
