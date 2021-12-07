#!/usr/bin/env bash
mapfile -t nums < <(<inputs/d07.txt tr "," "\n" | sort -n)
median=${nums[$(( ${#nums[@]} / 2 ))]}
sol1=0
sum=0
for num in "${nums[@]}"; do
  diff=$((num - median))
  abs_diff=${diff#-}
  sol1=$(( sol1 + abs_diff))
  sum=$(( sum + num))
done
echo "Part 1: $sol1"

sol2=0
mean=$(( sum / ${#nums[@]} ))

for num in "${nums[@]}"; do
  diff=$((num - mean))
  abs_diff=${diff#-}
  sol2=$(( sol2 + abs_diff * (abs_diff + 1) / 2 ))
done

echo "Part 2: $sol2"
