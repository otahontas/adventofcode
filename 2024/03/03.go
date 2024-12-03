package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("03.txt")
	if err != nil {
		fmt.Println("Can't read file")
		panic(err)
	}
	ans1 := 0
	reg1 := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	for _, line := range lines {
		for _, match_arr := range reg1.FindAllStringSubmatch(line, -1) {
			nums := make([]int, 0)
			for _, num_as_str := range match_arr[1:] {
				num, err := strconv.Atoi(num_as_str)
				if err != nil {
					fmt.Println("Error converting str to int")
					panic(err)
				}
				nums = append(nums, num)
			}
			ans1 += nums[0] * nums[1]
		}
	}
	ans2 := 0
	reg2 := regexp.MustCompile(`mul\(\d+,\d+\)|do\(\)|don't\(\)`)
	reg_nums := regexp.MustCompile(`\d+`)
	enabled := true
	for _, line := range lines {
		for _, match_arr := range reg2.FindAllStringSubmatch(line, -1) {
			match := match_arr[0]
			if enabled && strings.HasPrefix(match, "mul") {
				nums := make([]int, 0)
				for _, num_as_str := range reg_nums.FindAllString(match, -1) {
					num, err := strconv.Atoi(num_as_str)
					if err != nil {
						fmt.Println("Error converting str to int")
						panic(err)
					}
					nums = append(nums, num)
				}
				ans2 += nums[0] * nums[1]
			} else if match == "do()" {
				enabled = true
			} else {
				enabled = false
			}

		}
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
