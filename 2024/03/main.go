package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
	"regexp"
	"strings"
)

//go:embed input.txt
var input string

func main() {
	lines := utils.SplitByDelimiterAndStrip(input)
	ans1, ans2 := 0, 0
	mul_instructions_regex := regexp.MustCompile(`mul\(\d+,\d+\)`)
	for _, line := range lines {
		for _, match := range mul_instructions_regex.FindAllString(line, -1) {
			nums := utils.ExtractNumbers(match)
			ans1 += nums[0] * nums[1]
		}
	}
	all_instructions_regex := regexp.MustCompile(`mul\(\d+,\d+\)|do\(\)|don't\(\)`)
	enabled := true
	for _, line := range lines {
		for _, match := range all_instructions_regex.FindAllString(line, -1) {
			if enabled && strings.HasPrefix(match, "mul") {
				nums := utils.ExtractNumbers(match)
				ans2 += nums[0] * nums[1]
			} else if match == "do()" {
				enabled = true
			} else if match == "don't()" {
				enabled = false
			}
		}
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
