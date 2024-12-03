package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	data, err := os.ReadFile("01.txt")
	if err != nil {
		fmt.Println("Can't read file")
		panic(err)
	}
	left := make([]int, 0)
	right := make([]int, 0)
	appearances := make(map[int]int)

	for _, line := range strings.Split(strings.TrimSpace(string(data)), "\n") {
		nums_as_str := strings.Fields(line)
		nums := make([]int, 0)
		for j := 0; j < len(nums_as_str); j++ {
			num, err := strconv.Atoi(nums_as_str[j])
			if err != nil {
				fmt.Println("Error converting str to int")
				panic(err)
			}
			nums = append(nums, num)
		}
		left = append(left, nums[0])
		right = append(right, nums[1])
		appearances[nums[1]] += 1
	}
	sort.Sort(sort.IntSlice(left))
	sort.Sort(sort.IntSlice(right))
	var ans1 = 0
	var ans2 = 0
	for i := range left {
		ans1 += abs(left[i] - right[i])
		ans2 += left[i] * appearances[left[i]]
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
