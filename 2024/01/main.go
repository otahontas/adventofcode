package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
	"sort"
)

//go:embed input.txt
var input string

func main() {
	left, right := make([]int, 0), make([]int, 0)
	appearances := make(map[int]int)
	for _, line := range utils.SplitByDelimiterAndStrip(input) {
		nums := utils.ExtractNumbers(line)
		left = append(left, nums[0])
		right = append(right, nums[1])
		appearances[nums[1]]++
	}
	sort.Ints(left)
	sort.Ints(right)
	ans1, ans2 := 0, 0
	for i := range left {
		ans1 += utils.Abs(left[i] - right[i])
		ans2 += left[i] * appearances[left[i]]
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
