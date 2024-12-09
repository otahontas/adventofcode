package main

import (
	"adventofcode/utils"
	_ "embed"
	"fmt"
	"slices"
)

//go:embed input.txt
var input string

func compactHardDriveOneByOneAndReturnCheckSum(input string) int {
	disk := make([]int, 0)
	for i := 0; i < len(input); i += 2 {
		file_input, free_space_input := input[i], input[i+1]
		file_len := int(file_input - '0')
		for j := 0; j < file_len; j++ {
			disk = append(disk, i/2)
		}
		free_space_len := int(free_space_input - '0')
		for j := 0; j < free_space_len; j++ {
			disk = append(disk, -1)
		}
	}
	free_space_pointer, file_pointer := 0, len(disk)-1
	for free_space_pointer < file_pointer {
		for disk[free_space_pointer] == -1 && disk[file_pointer] != -1 {
			disk[free_space_pointer] = disk[file_pointer]
			disk[file_pointer] = -2
			free_space_pointer++
			file_pointer--
		}
		for disk[file_pointer] == -1 {
			file_pointer--
		}
		for disk[free_space_pointer] != -1 {
			free_space_pointer++
		}
	}
	checksum := 0
	for pos := 0; pos < len(disk); pos++ {
		if disk[pos] < 0 {
			continue
		}
		checksum += pos * disk[pos]
	}
	return checksum
}

type Block struct {
	id       int
	size     int
	position int
}

func compactHardDriveByMovingWholeFiles(input string) int {
	files, free_spaces, pos, checksum := make([]Block, 0), make([]Block, 0), 0, 0
	for i := 0; i < len(input); i += 2 {
		file_input, free_space_input := input[i], input[i+1]
		file_len := int(file_input - '0')
		files = append(files, Block{id: i / 2, size: file_len, position: pos})
		pos += file_len
		free_space_len := int(free_space_input - '0')
		free_spaces = append(free_spaces, Block{id: i / 2, size: free_space_len, position: pos})
		pos += free_space_len
	}
	slices.Reverse(files)
	for i := 0; i < len(files); i++ {
		for j := 0; j < len(free_spaces); j++ {
			if free_spaces[j].position > files[i].position {
				break
			}
			if free_spaces[j].size >= files[i].size {
				files[i].position = free_spaces[j].position
				free_spaces[j].size -= files[i].size     // shrink
				free_spaces[j].position += files[i].size // move
				break
			}
		}
		for offset := range files[i].size {
			checksum += (files[i].position + offset) * files[i].id
		}
	}
	return checksum
}

func main() {
	input := utils.SplitByDelimiterAndStrip(input)[0]
	if len(input)%2 != 0 {
		input += "0" // add a free space at the end
	}
	ans1 := compactHardDriveOneByOneAndReturnCheckSum(input)
	ans2 := compactHardDriveByMovingWholeFiles(input)
	fmt.Println(ans1)
	fmt.Println(ans2)
}
