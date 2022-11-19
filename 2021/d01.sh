#!/usr/bin/env bash
source "./common.sh"

input=$(read_input "01")

first=$(echo "$input" | awk 'NR > 1 && $0 > prev {count++} {prev=$0} END {print count}')

second=$(echo "$input" | awk 'NR > 3 && sum > prev_sum {count++} {
  a[0] = a[1]
  a[1] = a[2]
  a[2] = $0
  prev_sum = sum
  sum = a[0] + a[1] + a[2]
} END {print count}')

msg "Part 1: $first"
msg "Part 2: $second"
