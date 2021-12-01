#!/bin/sh

echo "Part 1:"
awk 'NR > 1 && $0 > prev {count++} {prev=$0} END {print count}' inputs/d01.txt

echo "Part 2:"
awk 'NR > 3 && sum > prev_sum {count++} {
  a[0] = a[1]
  a[1] = a[2]
  a[2] = $0
  prev_sum = sum
  sum = a[0] + a[1] + a[2]
} END {print count}' inputs/d01.txt
