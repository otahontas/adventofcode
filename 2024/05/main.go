package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
	"sort"
)

//go:embed input.txt
var input string

func isInRightOrder(pages []int, rules_map map[int]map[int]bool) bool {
	for i := 0; i < len(pages)-1; i++ {
		// apparently it's enough to check just the next number :D
		if !rules_map[pages[i]][pages[i+1]] {
			return false
		}
	}
	return true
}

func putToRightOrder(pages []int, rules_map map[int]map[int]bool) []int {
	pages_in_right_order := make([]int, len(pages))
	copy(pages_in_right_order, pages)
	sort.Slice(pages_in_right_order, func(i, j int) bool {
		return rules_map[pages_in_right_order[i]][pages_in_right_order[j]]
	})
	return pages_in_right_order
}

func main() {
	splitted_input := utils.SplitByDelimiterAndStrip(input, "\n\n")
	rules := utils.SplitByDelimiterAndStrip(splitted_input[0])
	updates := utils.SplitByDelimiterAndStrip(splitted_input[1])
	rules_map := make(map[int]map[int]bool)
	for _, rule := range rules {
		rule_parts := utils.ExtractNumbers(rule)
		source, destination := rule_parts[0], rule_parts[1]
		if _, ok := rules_map[source]; !ok {
			rules_map[source] = make(map[int]bool)
		}
		rules_map[source][destination] = true
	}
	ans1, ans2 := 0, 0
	updates_not_in_right_order := make([][]int, 0)
	for _, update := range updates {
		pages := utils.ExtractNumbers(update)
		if isInRightOrder(pages, rules_map) {
			ans1 += pages[len(pages)/2]
		} else {
			updates_not_in_right_order = append(updates_not_in_right_order, pages)
		}
	}
	for _, update := range updates_not_in_right_order {
		update_in_right_order := putToRightOrder(update, rules_map)
		ans2 += update_in_right_order[len(update_in_right_order)/2]
	}
	fmt.Println(ans1)
	fmt.Println(ans2)
}
