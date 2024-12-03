package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

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
		abs_diff := abs(arr[i] - arr[i+1])
		if abs_diff < 1 || abs_diff > 3 {
			return false
		}
	}
	return true
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
	data, err := os.ReadFile("02.txt")
	if err != nil {
		fmt.Println("Can't read file")
		panic(err)
	}
	ans1 := 0
	ans2_addition := 0
	for _, line := range strings.Split(strings.TrimSpace(string(data)), "\n") {
		nums_as_str := strings.Fields(line)
		nums := make([]int, 0)
		for j := range nums_as_str {
			num, err := strconv.Atoi(nums_as_str[j])
			if err != nil {
				fmt.Println("Error converting str to int")
				panic(err)
			}
			nums = append(nums, num)
		}
		if (increasing(nums) || decreasing(nums)) && diffs_ok(nums) {
			ans1 += 1
			continue
		}
		for _, list := range make_all_lists_with_one_element_removed(nums) {
			if (increasing(list) || decreasing(list)) && diffs_ok(list) {
				ans2_addition += 1
				break
			}
		}
	}
	fmt.Println(ans1)
	fmt.Println(ans1 + ans2_addition)

}
