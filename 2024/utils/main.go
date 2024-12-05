package utils

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

// Delimiter is optional, see https://stackoverflow.com/a/23650312
// Default delimiter is \n
func SplitByDelimiterAndStrip(input string, delimiter ...string) []string {
	resolved_delimiter := "\n"
	if len(delimiter) > 1 {
		panic("Too many variadic arguments for delimiter, call the function with args (string, delimiter")
	}
	if len(delimiter) == 1 && delimiter[0] != "" {
		resolved_delimiter = delimiter[0]
	}
	return strings.Split(strings.TrimSpace(string(input)), resolved_delimiter)
}

var numbers_regex = regexp.MustCompile(`\d+`)

// Reads the numbers from any input string
func ExtractNumbers(input string) []int {
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
