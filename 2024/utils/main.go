package utils

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

// Strips the whitespace and returns the input splitted by newlines
func ReadLines(input string) []string {
	return strings.Split(strings.TrimSpace(string(input)), "\n")
}

var numbers_regex = regexp.MustCompile(`\d+`)

// Reads the numbers from any input string
func ReadNumbers(input string) []int {
	nums_as_str := numbers_regex.FindAllString(input, -1)
	nums := make([]int, 0)
	for _, num_as_str := range nums_as_str {
		num, err := strconv.Atoi(num_as_str)
		if err != nil {
			fmt.Println("Error converting str to int")
			panic(err)
		}
		nums = append(nums, num)
	}
	return nums
}

// Returns the absolute value of x
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
