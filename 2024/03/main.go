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
	lines := utils.ReadLines(input)
	mul_instructions_regex := regexp.MustCompile(`mul\(\d+,\d+\)`)
	ans1 := 0
	for _, line := range lines {
		for _, match := range mul_instructions_regex.FindAllString(line, -1) {
			nums := utils.ReadNumbers(match)
			ans1 += nums[0] * nums[1]
		}
	}
	all_instructions_regex := regexp.MustCompile(`mul\(\d+,\d+\)|do\(\)|don't\(\)`)
	ans2 := 0
	enabled := true
	for _, line := range lines {
		for _, match := range all_instructions_regex.FindAllString(line, -1) {
			if enabled && strings.HasPrefix(match, "mul") {
				nums := utils.ReadNumbers(match)
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
